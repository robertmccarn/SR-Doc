"""Silver derivation from immutable Bronze captures."""
from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
HEADING = re.compile(r"^(={2,6})\s*(.*?)\s*\1\s*$", re.MULTILINE)
YEAR = re.compile(r"(?<!\d)(1[5-9]\d{2}|20\d{2}|21\d{2}|22\d{2})(?!\d)")


def load_json(path: Path, default: Any) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "untitled"


def parse_page(record: dict[str, Any], source_files: dict[str, str]) -> tuple[dict[str, Any], str]:
    raw = (ROOT / record["raw_path"]).read_text(encoding="utf-8")
    headings = [{"level": len(match.group(1)) - 1, "title": match.group(2), "offset": match.start()} for match in HEADING.finditer(raw)]
    links = [{"target": match.group(1).strip(), "label": (match.group(2) or match.group(1)).strip(), "offset": match.start()} for match in WIKILINK.finditer(raw)]
    warnings = []
    if raw.count("{{") != raw.count("}}"):
        warnings.append("unbalanced_template_braces")
    if raw.count("[[") != raw.count("]]" ):
        warnings.append("unbalanced_wikilink_brackets")
    years = sorted(set(YEAR.findall(raw)))
    page = record | {"headings": headings, "parsed_links": links, "years_mentioned": years, "parser_warnings": warnings}
    body = raw
    def render_link(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        label = (match.group(2) or target).strip()
        filename = source_files.get(target) or source_files.get(target.replace("_", " "))
        if filename:
            return f"[{label}]({filename})"
        upstream = "https://second-renaissance.fandom.com/wiki/" + target.replace(" ", "_")
        return f"[{label}]({upstream})"
    body = re.sub(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]", render_link, body)
    body = re.sub(r"^={2,6}\s*(.*?)\s*=+\s*$", lambda m: "#" * (len(m.group(0)) - len(m.group(0).lstrip('=')) - 1) + " " + m.group(1), body, flags=re.MULTILINE)
    markdown = "---\n" + "\n".join([
        f"page_id: {record['page_id']}", f"revision_id: {record['revision_id']}", f"source_url: {record['source_url']}", f"raw_sha256: {record['raw_sha256']}", "---",
        "", f"# {record['title']}", "", "## Preserved source", "", "```wikitext", body, "```",
        "", "## Provenance", "", f"Raw source: `{record['raw_path']}` · revision `{record['revision_id']}` · [upstream]({record['source_url']})", "",
    ])
    return page, markdown


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records), encoding="utf-8")


def build(args: argparse.Namespace) -> None:
    manifest = ROOT / "bronze" / "manifests" / "pages.json"
    records = load_json(manifest, [])
    if not records and not args.allow_empty:
        raise SystemExit("No Bronze manifest. Run `python -m sr_doc.archive sync` first.")
    pages, relations, timeline = [], [], []
    markdown_dir = ROOT / "silver" / "markdown"
    site_source_dir = ROOT / "site" / "generated" / "source"
    source_files = {record["title"]: f"{record['page_id']}-{slug(record['title'])}.md" for record in records}
    for record in records:
        if not (ROOT / record["raw_path"]).exists():
            continue
        page, markdown = parse_page(record, source_files)
        pages.append(page)
        (markdown_dir / f"{record['page_id']}-{slug(record['title'])}.md").parent.mkdir(parents=True, exist_ok=True)
        (markdown_dir / f"{record['page_id']}-{slug(record['title'])}.md").write_text(markdown, encoding="utf-8")
        site_source_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(markdown_dir / f"{record['page_id']}-{slug(record['title'])}.md", site_source_dir / f"{record['page_id']}-{slug(record['title'])}.md")
        for link in page["parsed_links"]:
            relations.append({"id": f"wiki-link:{record['page_id']}:{link['offset']}", "type": "wiki_link", "from_page_id": record["page_id"], "to_title": link["target"], "source": {"page_id": record["page_id"], "revision_id": record["revision_id"], "offset": link["offset"]}})
        for year in page["years_mentioned"]:
            timeline.append({"id": f"year-mention:{record['page_id']}:{year}", "year": int(year), "type": "mentioned_year", "source": {"page_id": record["page_id"], "revision_id": record["revision_id"]}})
    write_jsonl(ROOT / "silver" / "pages.jsonl", pages)
    write_jsonl(ROOT / "silver" / "relations.jsonl", relations)
    write_jsonl(ROOT / "silver" / "timeline.jsonl", timeline)
    conflicts = Counter(item["year"] for item in timeline)
    report = ["# Continuity report", "", f"Source pages: {len(pages)}", f"Extracted wiki links: {len(relations)}", f"Year mentions: {len(timeline)}", "", "## High-density years", ""]
    report += [f"- {year}: {count} source-page mentions" for year, count in conflicts.most_common(20)] or ["- No Bronze corpus has been captured yet."]
    report_text = "\n".join(report) + "\n"
    (ROOT / "silver" / "continuity-report.md").write_text(report_text, encoding="utf-8")
    print(f"Generated Silver artifacts for {len(pages)} pages.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(required=True)
    build_parser = sub.add_parser("build"); build_parser.add_argument("--allow-empty", action="store_true"); build_parser.set_defaults(func=build)
    args = parser.parse_args(); args.func(args)


if __name__ == "__main__":
    main()
