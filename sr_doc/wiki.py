"""Build a browseable static wiki from Fandom's rendered MediaWiki API output."""
from __future__ import annotations

import argparse
import concurrent.futures
import html
import json
import re
import shutil
from pathlib import Path
from typing import Any

from .archive import ROOT, api, write_json


def load(path: Path, default: Any) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "page"


def page_name(page: dict[str, Any]) -> str:
    return f"{page['page_id']}-{slug(page['title'])}.html"


def capture_one(page: dict[str, Any]) -> dict[str, Any]:
    target = ROOT / "bronze" / "rendered" / f"{page['page_id']}.json"
    if target.exists():
        return {"page_id": page["page_id"], "status": "existing"}
    try:
        result = api({"action": "parse", "pageid": page["page_id"], "prop": "text|categories|links", "format": "json"})
        parsed = result["parse"]
        payload = {"page_id": page["page_id"], "revision_id": page["revision_id"], "title": parsed["title"], "html": parsed["text"].get("*", ""), "categories": parsed.get("categories", []), "links": parsed.get("links", [])}
        write_json(target, payload)
        return {"page_id": page["page_id"], "status": "captured"}
    except Exception as error:
        return {"page_id": page["page_id"], "status": "failed", "error": str(error)}


def render(args: argparse.Namespace) -> None:
    pages = load(ROOT / "bronze" / "manifests" / "pages.json", [])
    if args.limit:
        pages = pages[:args.limit]
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        results = list(executor.map(capture_one, pages))
    write_json(ROOT / "bronze" / "manifests" / "rendered.json", results)
    counts = {state: sum(item["status"] == state for item in results) for state in {item["status"] for item in results}}
    print(f"Rendered capture: {counts}")


def stylesheet() -> str:
    return """
:root{--blue:#0b4b82;--nav:#17385d;--gold:#f5c518;--ink:#222;--muted:#667}*{box-sizing:border-box}body{margin:0;background:#f5f5f5;color:var(--ink);font:15px/1.55 Arial,sans-serif}a{color:#2166a6;text-decoration:none}a:hover{text-decoration:underline}.top{height:58px;background:var(--nav);color:#fff;display:flex;align-items:center;padding:0 28px;gap:24px}.brand{font-size:20px;font-weight:700;color:#fff}.top a{color:#fff}.search{margin-left:auto;width:290px;padding:9px 12px;border:0;border-radius:3px}.layout{max-width:1440px;margin:auto;display:grid;grid-template-columns:230px minmax(0,1fr);min-height:calc(100vh - 58px)}aside{background:#fff;border-right:1px solid #ddd;padding:26px 20px}aside h3{font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin:22px 0 8px}aside a{display:block;padding:5px 0}main{background:#fff;margin:24px;padding:32px 42px;box-shadow:0 1px 4px #bbb;min-width:0}.title{border-bottom:3px solid var(--gold);padding-bottom:14px;margin:0 0 24px;font-size:34px}.article img{max-width:100%;height:auto}.article .infobox{float:right;clear:right;margin:0 0 18px 24px;max-width:340px;border:1px solid #a2a9b1;background:#f8f9fa;font-size:13px}.article .infobox th,.article .infobox td{padding:6px 9px;border-bottom:1px solid #ddd}.article table{border-collapse:collapse;max-width:100%}.article td,.article th{padding:6px;border:1px solid #ccc}.article h2{border-bottom:1px solid #bbb;padding-bottom:5px}.article .thumb{border:1px solid #ccc;background:#f8f9fa;padding:4px;margin:8px}.article .thumb.tright{float:right;margin-left:18px}.article .thumb.tleft{float:left;margin-right:18px}.meta{color:var(--muted);font-size:12px;border-top:1px solid #ddd;margin-top:30px;padding-top:12px}.home-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}.card{border:1px solid #ddd;padding:14px;background:#fafafa}.category{display:inline-block;background:#e9f2fb;border:1px solid #b8d0e7;padding:3px 8px;margin:3px;font-size:12px}@media(max-width:800px){.layout{display:block}aside{display:none}main{margin:0;box-shadow:none;padding:22px}.search{width:160px}.top{padding:0 15px}.title{font-size:28px}}
"""


def rewrite_html(source: str, title_map: dict[str, str], media_map: dict[str, str]) -> str:
    def wiki_link(match: re.Match[str]) -> str:
        prefix, target = match.group(1), match.group(2)
        decoded = target.replace("_", " ")
        return f'{prefix}{title_map.get(decoded, "https://second-renaissance.fandom.com/wiki/" + target)}'
    source = re.sub(r'(href=["\'])/wiki/([^"\'#?]+)', wiki_link, source)
    def image_link(match: re.Match[str]) -> str:
        url = html.unescape(match.group(0))
        filename = re.search(r'/([^/?]+)/(?:revision|scale-to-width-down)', url)
        if filename:
            candidate = filename.group(1).replace("_", " ")
            local = media_map.get(candidate)
            if local:
                return local
        return url
    return re.sub(r'https?://static\.wikia\.nocookie\.net/[^"\'\s>]+', image_link, source)


def shell(title: str, body: str, page: dict[str, Any] | None = None) -> str:
    prefix = "../" if page else ""
    provenance = ""
    if page:
        provenance = f'<div class="meta">Mirrored from <a href="{html.escape(page["source_url"])}">Fandom</a> · revision {page["revision_id"]} · page ID {page["page_id"]}</div>'
    return f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} | Second Renaissance</title><link rel="stylesheet" href="{prefix}assets/wiki.css"></head><body><header class="top"><a class="brand" href="{prefix}index.html">Second Renaissance Wikia</a><a href="{prefix}all-pages.html">Explore</a><a href="{prefix}categories.html">Categories</a><input id="search" class="search" placeholder="Search this wiki" oninput="findPage(this.value)"></header><div class="layout"><aside><h3>Navigation</h3><a href="{prefix}index.html">Main page</a><a href="{prefix}all-pages.html">All pages</a><a href="{prefix}categories.html">Categories</a><h3>Archive</h3><a href="{prefix}continuity.html">Continuity report</a><a href="{prefix}source-corpus.html">Source provenance</a></aside><main><h1 class="title">{html.escape(title)}</h1><article class="article">{body}</article>{provenance}</main></div><script src="{prefix}assets/wiki.js"></script></body></html>'


def build(_: argparse.Namespace) -> None:
    pages = load(ROOT / "bronze" / "manifests" / "pages.json", [])
    if not pages:
        raise SystemExit("No Bronze page manifest; run archive sync first.")
    out = ROOT / "build" / "wiki"; pages_dir = out / "pages"; assets_dir = out / "assets"
    if out.exists(): shutil.rmtree(out)
    pages_dir.mkdir(parents=True); assets_dir.mkdir()
    (assets_dir / "wiki.css").write_text(stylesheet(), encoding="utf-8")
    title_map = {page["title"]: f"pages/{page_name(page)}" for page in pages}
    assets = load(ROOT / "bronze" / "manifests" / "assets.json", [])
    media_map: dict[str, str] = {}
    for item in assets:
        filename = f"{item['page_id']}-{item['title'].split(':', 1)[-1].replace('/', '_')}"
        source = ROOT / "bronze" / "assets" / filename
        if source.exists():
            target = assets_dir / filename
            shutil.copy2(source, target)
            media_map[item["title"].split(":", 1)[-1]] = f"../assets/{filename}"
    items = []
    for page in pages:
        render_path = ROOT / "bronze" / "rendered" / f"{page['page_id']}.json"
        if not render_path.exists():
            continue
        rendered = load(render_path, {})
        content = rewrite_html(rendered.get("html", ""), title_map, media_map)
        (pages_dir / page_name(page)).write_text(shell(page["title"], content, page), encoding="utf-8")
        items.append(page)
    cards = "".join(f'<div class="card"><a href="pages/{page_name(page)}">{html.escape(page["title"])}</a></div>' for page in items[:60])
    home = '<p>A local, source-attributed mirror of the Second Renaissance Wikia.</p><h2>Explore the universe</h2><div class="home-grid">' + cards + '</div>'
    (out / "index.html").write_text(shell("Second Renaissance Wikia", home), encoding="utf-8")
    all_pages = "".join(f'<li><a href="pages/{page_name(page)}">{html.escape(page["title"])}</a></li>' for page in items)
    (out / "all-pages.html").write_text(shell("All pages", f'<p>{len(items)} rendered pages.</p><ul>{all_pages}</ul>'), encoding="utf-8")
    categories = sorted({category for page in pages for category in page.get("categories", [])})
    (out / "categories.html").write_text(shell("Categories", "".join(f'<span class="category">{html.escape(category)}</span>' for category in categories)), encoding="utf-8")
    (assets_dir / "wiki.js").write_text("const pages=" + json.dumps([{ "t": p["title"], "u": "pages/" + page_name(p)} for p in items], ensure_ascii=False) + ";function findPage(q){q=q.toLowerCase();let p=pages.find(x=>x.t.toLowerCase().includes(q));if(q&&p)location.href=(location.pathname.includes('/pages/')?'../':'')+p.u}", encoding="utf-8")
    report_path = ROOT / "silver" / "continuity-report.md"
    report = report_path.read_text(encoding="utf-8") if report_path.exists() else "No report generated."
    (out / "continuity.html").write_text(shell("Continuity report", f"<pre>{html.escape(report)}</pre>"), encoding="utf-8")
    (out / "source-corpus.html").write_text(shell("Source provenance", f"<p>{len(pages)} current page revisions captured from the public MediaWiki API. Rendered pages: {len(items)}.</p>"), encoding="utf-8")
    print(f"Built static wiki with {len(items)} rendered pages at {out}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__); sub = parser.add_subparsers(required=True)
    capture = sub.add_parser("render"); capture.add_argument("--workers", type=int, default=4); capture.add_argument("--limit", type=int); capture.set_defaults(func=render)
    build_parser = sub.add_parser("build"); build_parser.set_defaults(func=build)
    args = parser.parse_args(); args.func(args)


if __name__ == "__main__": main()
