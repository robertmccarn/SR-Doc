"""Bronze acquisition: resumable MediaWiki API capture with provenance."""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

API = "https://second-renaissance.fandom.com/api.php"
UA = "SRDocArchive/0.1 (+local narrative archive)"
ROOT = Path(__file__).resolve().parents[1]


def api(params: dict[str, Any], retries: int = 4) -> dict[str, Any]:
    query = urllib.parse.urlencode(params, doseq=True)
    request = urllib.request.Request(f"{API}?{query}", headers={"User-Agent": UA, "Accept": "application/json"})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
            if attempt + 1 == retries:
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError("unreachable")


def paged(params: dict[str, Any]) -> Iterator[dict[str, Any]]:
    continuation: dict[str, Any] = {}
    while True:
        result = api(params | continuation)
        yield result
        continuation = result.get("continue", {})
        if not continuation:
            return
        time.sleep(0.15)


def public_namespaces() -> list[int]:
    result = api({"action": "query", "meta": "siteinfo", "siprop": "namespaces", "format": "json"})
    namespaces = result["query"]["namespaces"]
    # Special and Media are virtual endpoints rather than stored public content pages.
    return [int(key) for key in namespaces if int(key) not in {-2, -1}]


def inventory() -> list[dict[str, Any]]:
    pages: list[dict[str, Any]] = []
    for namespace in public_namespaces():
        for response in paged({"action": "query", "list": "allpages", "apnamespace": namespace, "aplimit": "max", "format": "json"}):
            pages.extend(response.get("query", {}).get("allpages", []))
    return sorted(pages, key=lambda page: page["pageid"])


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def capture_pages(pages: list[dict[str, Any]], run_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for offset in range(0, len(pages), 50):
        ids = [str(page["pageid"]) for page in pages[offset : offset + 50]]
        response = api({
            "action": "query", "pageids": "|".join(ids),
            "prop": "revisions|categories|links|images|templates|info",
            "rvprop": "ids|timestamp|content|contentmodel",
            "rvslots": "main", "cllimit": "max", "pllimit": "max", "imlimit": "max", "tllimit": "max", "format": "json",
        })
        write_json(run_dir / "api" / f"pages-{offset:06d}.json", response)
        for page_id, page in response.get("query", {}).get("pages", {}).items():
            revision = (page.get("revisions") or [{}])[0]
            slot = revision.get("slots", {}).get("main", {})
            raw = slot.get("*", "")
            revision_id = revision.get("revid", "none")
            raw_path = ROOT / "bronze" / "pages" / str(page_id) / f"{revision_id}.wikitext"
            raw_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path.write_text(raw, encoding="utf-8", newline="")
            record = {
                "page_id": int(page_id), "title": page.get("title"), "namespace": page.get("ns"),
                "revision_id": revision.get("revid"), "parent_revision_id": revision.get("parentid"),
                "timestamp": revision.get("timestamp"), "content_model": slot.get("contentmodel"),
                "redirect": "redirect" in page, "raw_path": raw_path.relative_to(ROOT).as_posix(),
                "raw_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
                "categories": [x.get("title") for x in page.get("categories", [])],
                "links": [x.get("title") for x in page.get("links", [])],
                "images": [x.get("title") for x in page.get("images", [])],
                "templates": [x.get("title") for x in page.get("templates", [])],
                "source_url": f"https://second-renaissance.fandom.com/wiki/{urllib.parse.quote(page.get('title', '').replace(' ', '_'))}",
            }
            records.append(record)
        time.sleep(0.15)
    return sorted(records, key=lambda record: record["page_id"])


def asset_inventory() -> list[dict[str, Any]]:
    assets: list[dict[str, Any]] = []
    for response in paged({"action": "query", "generator": "allimages", "gailimit": "max", "prop": "imageinfo", "iiprop": "url|size|mime|sha1", "format": "json"}):
        for page in response.get("query", {}).get("pages", {}).values():
            info = (page.get("imageinfo") or [{}])[0]
            assets.append({"page_id": page["pageid"], "title": page["title"], **info})
    return sorted(assets, key=lambda asset: asset["page_id"])


def _download_asset(asset: dict[str, Any]) -> dict[str, Any]:
    filename = f"{asset['page_id']}-{asset['title'].split(':', 1)[-1].replace('/', '_')}"
    target = ROOT / "bronze" / "assets" / filename
    entry = {"page_id": asset["page_id"], "title": asset["title"], "url": asset.get("url"), "size": int(asset.get("size") or 0), "sha1": asset.get("sha1")}
    if target.exists() and hashlib.sha1(target.read_bytes()).hexdigest() == asset.get("sha1"):
        entry["status"] = "existing_verified"
        return entry
    try:
        # Fandom content-negotiates WebP by default. `format=original` is required for the
        # byte stream whose SHA-1 the MediaWiki API reports.
        original_url = asset["url"] + ("&" if "?" in asset["url"] else "?") + "format=original"
        entry["url"] = original_url
        request = urllib.request.Request(original_url, headers={"User-Agent": UA, "Accept": "*/*"})
        with urllib.request.urlopen(request, timeout=60) as response:
            data = response.read()
        actual_sha1 = hashlib.sha1(data).hexdigest()
        entry["actual_sha1"] = actual_sha1
        entry["response_mime"] = response.headers.get_content_type()
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        # Some old Fandom assets are irreversibly recompressed by the CDN even with
        # format=original. Retain those bytes, but make the provenance discrepancy explicit.
        entry["status"] = "downloaded_verified" if actual_sha1 == asset.get("sha1") else "downloaded_checksum_mismatch"
    except Exception as error:  # manifest failures instead of hiding them
        entry["status"] = "failed"
        entry["error"] = str(error)
    return entry


def download_assets(assets: list[dict[str, Any]], budget_mib: int, manifest: list[dict[str, Any]]) -> None:
    used = 0
    limit = budget_mib * 1024 * 1024
    selected: list[dict[str, Any]] = []
    for asset in assets:
        size = int(asset.get("size") or 0)
        if used + size > limit:
            manifest.append({"page_id": asset["page_id"], "title": asset["title"], "url": asset.get("url"), "size": size, "sha1": asset.get("sha1"), "status": "omitted_budget"})
            continue
        used += size
        selected.append(asset)
    # Four workers are intentionally conservative for Fandom's asset CDN. Existing files are re-hashed,
    # making an interrupted run safe to restart.
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for entry in executor.map(_download_asset, selected):
            manifest.append(entry)


def sync(args: argparse.Namespace) -> None:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = ROOT / "bronze" / "runs" / run_id
    pages = inventory()
    write_json(run_dir / "inventory.json", pages)
    records = capture_pages(pages, run_dir)
    assets = asset_inventory()
    asset_manifest: list[dict[str, Any]] = []
    if not args.no_media:
        download_assets(assets, args.media_budget_mib, asset_manifest)
    write_json(ROOT / "bronze" / "manifests" / "pages.json", records)
    write_json(ROOT / "bronze" / "manifests" / "assets.json", asset_manifest or assets)
    write_json(run_dir / "run.json", {"run_id": run_id, "page_count": len(records), "asset_count": len(assets), "media_budget_mib": args.media_budget_mib, "completed_at": datetime.now(timezone.utc).isoformat()})
    print(f"Captured {len(records)} pages and inventoried {len(assets)} assets in {run_dir}")


def plan(_: argparse.Namespace) -> None:
    pages = inventory()
    assets = asset_inventory()
    print(json.dumps({"pages": len(pages), "assets": len(assets), "asset_bytes": sum(int(a.get("size") or 0) for a in assets), "namespaces": public_namespaces()}, indent=2))


def media(args: argparse.Namespace) -> None:
    """Resume media alone without re-querying every page revision."""
    assets = asset_inventory()
    asset_manifest: list[dict[str, Any]] = []
    download_assets(assets, args.media_budget_mib, asset_manifest)
    write_json(ROOT / "bronze" / "manifests" / "assets.json", asset_manifest)
    verified = sum(item["status"] in {"downloaded_verified", "existing_verified"} for item in asset_manifest)
    transformed = sum(item["status"] == "downloaded_checksum_mismatch" for item in asset_manifest)
    failed = sum(item["status"] == "failed" for item in asset_manifest)
    print(f"Verified {verified}/{len(asset_manifest)} originals; retained {transformed} CDN-transformed files; {failed} unavailable upstream.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(required=True)
    plan_parser = sub.add_parser("plan"); plan_parser.set_defaults(func=plan)
    sync_parser = sub.add_parser("sync")
    sync_parser.add_argument("--media-budget-mib", type=int, default=320)
    sync_parser.add_argument("--no-media", action="store_true")
    sync_parser.set_defaults(func=sync)
    media_parser = sub.add_parser("media", help="resume original-media download only")
    media_parser.add_argument("--media-budget-mib", type=int, default=320)
    media_parser.set_defaults(func=media)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
