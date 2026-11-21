#!/usr/bin/env python3
"""Extract source-aware, non-adjudicative infobox parameter claims from Bronze Wikitext."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from collections import Counter
from pathlib import PurePosixPath
from pathlib import Path

ARCHIVE_HASH = "d1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8"
LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]")


def archive_key(value: str) -> str:
    return str(PurePosixPath(str(value).replace("\\", "/"))).lstrip("./")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _skip_comment(text: str, i: int) -> int:
    if text.startswith("<!--", i):
        end = text.find("-->", i + 4)
        return len(text) if end < 0 else end + 3
    return i


def find_template_end(text: str, start: int) -> int | None:
    """Return the exclusive end of a balanced {{...}} template, or None."""
    if not text.startswith("{{", start) or text.startswith("{{{", start):
        return None
    stack = [2]
    i = start + 2
    while i < len(text):
        skipped = _skip_comment(text, i)
        if skipped != i:
            i = skipped
            continue
        if text.startswith("{{{", i):
            stack.append(3)
            i += 3
        elif text.startswith("{{", i):
            stack.append(2)
            i += 2
        elif text.startswith("}}}", i) and stack and stack[-1] == 3:
            stack.pop()
            i += 3
            if not stack:
                return i
        elif text.startswith("}}", i) and stack and stack[-1] == 2:
            stack.pop()
            i += 2
            if not stack:
                return i
        else:
            i += 1
    return None


def split_top_level_ranges(text: str, start: int, end: int, delimiter: str) -> list[tuple[int, int]]:
    """Split on a delimiter outside nested templates, parameters, and wikilinks."""
    ranges = []
    stack = []
    link_depth = 0
    segment_start = start
    i = start
    while i < end:
        skipped = _skip_comment(text, i)
        if skipped != i:
            i = min(skipped, end)
            continue
        if text.startswith("{{{", i):
            stack.append(3)
            i += 3
        elif text.startswith("{{", i):
            stack.append(2)
            i += 2
        elif text.startswith("}}}", i) and stack and stack[-1] == 3:
            stack.pop()
            i += 3
        elif text.startswith("}}", i) and stack and stack[-1] == 2:
            stack.pop()
            i += 2
        elif text.startswith("[[", i):
            link_depth += 1
            i += 2
        elif text.startswith("]]", i) and link_depth:
            link_depth -= 1
            i += 2
        elif text.startswith(delimiter, i) and not stack and link_depth == 0:
            ranges.append((segment_start, i))
            i += len(delimiter)
            segment_start = i
        else:
            i += 1
    ranges.append((segment_start, end))
    return ranges


def parse_template_parameters(text: str, start: int, end: int) -> tuple[str, list[dict]]:
    """Parse a balanced template invocation, retaining exact value slices."""
    inner_start, inner_end = start + 2, end - 2
    segments = split_top_level_ranges(text, inner_start, inner_end, "|")
    name_start, name_end = segments[0]
    template_name = text[name_start:name_end].strip()
    parameters = []
    for index, (seg_start, seg_end) in enumerate(segments[1:], 1):
        equals = split_top_level_ranges(text, seg_start, seg_end, "=")
        if len(equals) > 1:
            key_start, key_end = equals[0]
            value_start = key_end + 1
            raw_name = text[key_start:key_end].strip()
            name = raw_name if raw_name else None
        else:
            value_start = seg_start
            name = None
        parameters.append({
            "parameter_index": index,
            "parameter_name": name,
            "normalized_parameter_name": re.sub(r"\s+", " ", name.strip()).casefold() if name else f"#{index}",
            "raw_value": text[value_start:seg_end],
            "value_start": value_start,
            "value_end": seg_end,
        })
    return template_name, parameters


def iter_infoboxes(text: str):
    """Yield infobox invocations, including their nested-template-safe parameters."""
    i = 0
    while i < len(text) - 1:
        skipped = _skip_comment(text, i)
        if skipped != i:
            i = skipped
            continue
        if text.startswith("{{", i) and not text.startswith("{{{", i):
            end = find_template_end(text, i)
            if end is not None:
                name, parameters = parse_template_parameters(text, i, end)
                normalized_name = name.casefold().replace("_", " ").strip()
                if normalized_name.startswith("template:"):
                    normalized_name = normalized_name[len("template:"):].strip()
                if normalized_name.startswith("infobox"):
                    yield i, end, name, parameters
                i += 2
                continue
        i += 1


def linked_entities(raw_value: str, absolute_start: int) -> list[dict]:
    links = []
    for match in LINK_RE.finditer(raw_value):
        target = match.group(1).strip()
        display = match.group(2)
        links.append({
            "target": target,
            "display": display,
            "raw": match.group(0),
            "char_start": absolute_start + match.start(),
            "char_end": absolute_start + match.end(),
        })
    return links


def extract_page_claims(page: dict, raw_text: str, capture_id: str) -> list[dict]:
    claims = []
    page_id = str(page["page_id"])
    source_path = archive_key(page["raw_path"])
    source_hash = hashlib.sha256(raw_text.encode("utf-8")).hexdigest()
    if page.get("raw_sha256") and source_hash != page["raw_sha256"]:
        raise ValueError(f"Source hash mismatch for page {page_id}: {source_path}")
    for template_start, template_end, template_name, parameters in iter_infoboxes(raw_text):
        instance_seed = f"{capture_id}:{page_id}:{template_start}:{template_end}"
        instance_id = hashlib.sha256(instance_seed.encode()).hexdigest()[:24]
        for parameter in parameters:
            value_start, value_end = parameter["value_start"], parameter["value_end"]
            identity = f"{instance_seed}:{parameter['parameter_index']}:{value_start}:{value_end}"
            claim_id = hashlib.sha256(identity.encode()).hexdigest()[:24]
            claims.append({
                "claim_id": claim_id,
                "source_class": "primary" if page.get("namespace", 0) == 0 else "context",
                "page_id": page_id,
                "title": page["title"],
                "namespace": page.get("namespace"),
                "revision_id": page.get("revision_id"),
                "capture_id": capture_id,
                "source_path": source_path,
                "source_sha256": source_hash,
                "template_name": template_name,
                "template_instance_id": instance_id,
                "template_char_start": template_start,
                "template_char_end": template_end,
                "parameter_index": parameter["parameter_index"],
                "parameter_name": parameter["parameter_name"],
                "normalized_parameter_name": parameter["normalized_parameter_name"],
                "raw_parameter_value": parameter["raw_value"],
                "value_char_start": value_start,
                "value_char_end": value_end,
                "linked_entities": linked_entities(parameter["raw_value"], value_start),
                "provenance": {
                    "archive_sha256": capture_id,
                    "source_path": source_path,
                    "source_sha256": source_hash,
                    "locator": f"chars {value_start}-{value_end}",
                    "template_locator": f"chars {template_start}-{template_end}",
                },
            })
    return claims


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", help="Validated SR-Doc Bronze/Silver source ZIP")
    parser.add_argument("--output", default="infobox-claims.jsonl")
    parser.add_argument("--report", default="infobox-claims-report.json")
    parser.add_argument("--include-context", action="store_true", help="also extract non-main namespaces")
    parser.add_argument("--allow-unpinned-archive", action="store_true")
    args = parser.parse_args()

    archive = Path(args.archive)
    capture_id = sha256_file(archive)
    if capture_id != ARCHIVE_HASH and not args.allow_unpinned_archive:
        raise SystemExit(f"Archive hash mismatch: {capture_id}")

    with zipfile.ZipFile(archive) as source:
        manifest = json.loads(source.read("bronze\\manifests\\pages.json"))
        members = {archive_key(item.filename): item.filename for item in source.infolist()}
        claims = []
        errors = []
        pages_scanned = 0
        template_counts = Counter()
        for page in manifest:
            if page.get("namespace", 0) != 0 and not args.include_context:
                continue
            pages_scanned += 1
            source_path = archive_key(page["raw_path"])
            member = members.get(source_path)
            if member is None:
                errors.append(f"missing source: {source_path}")
                continue
            raw_bytes = source.read(member)
            try:
                raw_text = raw_bytes.decode("utf-8")
            except UnicodeDecodeError:
                errors.append(f"UTF-8 decode failure: {source_path}")
                continue
            actual_hash = hashlib.sha256(raw_bytes).hexdigest()
            if page.get("raw_sha256") and actual_hash != page["raw_sha256"]:
                errors.append(f"SHA-256 mismatch: {source_path}")
                continue
            page_claims = extract_page_claims(page, raw_text, capture_id)
            claims.extend(page_claims)
            for claim in page_claims:
                template_counts[claim["template_name"]] += 1

    if errors:
        raise SystemExit("Extraction aborted; source validation errors:\n" + "\n".join(errors[:50]))

    with Path(args.output).open("w", encoding="utf-8", newline="\n") as output:
        for claim in claims:
            output.write(json.dumps(claim, ensure_ascii=False) + "\n")

    report = {
        "status": "PASS",
        "archive_sha256": capture_id,
        "namespace_scope": "all" if args.include_context else "main (namespace 0)",
        "pages_scanned": pages_scanned,
        "infobox_parameter_claims": len(claims),
        "unique_claim_ids": len({claim["claim_id"] for claim in claims}),
        "template_parameter_counts": dict(sorted(template_counts.items())),
        "output": str(Path(args.output)),
        "source_errors": [],
        "interpretation": "Derived extraction only. Raw values and source locators are preserved; no claim is asserted as canon or adjudicated truth.",
    }
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
