#!/usr/bin/env python3
"""Read-only structural and integrity validator for an SR-Doc audit ZIP."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import sys
import zipfile
from collections import Counter
from pathlib import PurePosixPath
from typing import Any

EXPECTED = {"pages": 3579, "relations": 11462, "timeline": 4447, "assets": 900}
MANIFESTS = {"pages": "bronze/manifests/pages.json", "assets": "bronze/manifests/assets.json"}
JSONL = {"pages": "silver/pages.jsonl", "relations": "silver/relations.jsonl", "timeline": "silver/timeline.jsonl"}


def sha256_stream(stream) -> str:
    digest = hashlib.sha256()
    for block in iter(lambda: stream.read(1024 * 1024), b""):
        digest.update(block)
    return digest.hexdigest()


def normalize(name: str) -> str:
    return str(PurePosixPath(name.replace("\\", "/"))).lstrip("./")


def read_jsonl(zf: zipfile.ZipFile, names: dict[str, str], path: str) -> tuple[int, list[str]]:
    count, errors = 0, []
    with zf.open(names[path]) as raw:
        for line_no, line in enumerate(raw, 1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
                if not isinstance(item, dict):
                    raise ValueError("record is not a JSON object")
                count += 1
            except Exception as exc:
                errors.append(f"{path}:{line_no}: {exc}")
    return count, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", help="Path to SR-Doc-Audit.zip")
    parser.add_argument("--report", help="Write JSON report to this path (default: stdout)")
    parser.add_argument("--expected-pages", type=int, default=EXPECTED["pages"])
    parser.add_argument("--expected-relations", type=int, default=EXPECTED["relations"])
    parser.add_argument("--expected-timeline", type=int, default=EXPECTED["timeline"])
    parser.add_argument("--expected-assets", type=int, default=EXPECTED["assets"])
    args = parser.parse_args()

    report: dict[str, Any] = {
        "validator": "sr-doc-archive-validator/1.0",
        "archive": os.path.basename(args.archive),
        "archive_sha256": None,
        "zip_entries": 0,
        "counts": {},
        "checks": {},
        "errors": [],
        "warnings": [],
        "read_only": True,
    }
    expected = {"pages": args.expected_pages, "relations": args.expected_relations,
                "timeline": args.expected_timeline, "assets": args.expected_assets}
    try:
        with open(args.archive, "rb") as f:
            report["archive_sha256"] = sha256_stream(f)
        with zipfile.ZipFile(args.archive) as zf:
            infos = zf.infolist()
            report["zip_entries"] = len(infos)
            normalized: dict[str, list[str]] = {}
            for info in infos:
                normalized.setdefault(normalize(info.filename), []).append(info.filename)
            duplicate_paths = [k for k, v in normalized.items() if len(v) > 1]
            if duplicate_paths:
                report["errors"].append({"duplicate_normalized_paths": duplicate_paths[:100], "total": len(duplicate_paths)})
            lookup = {key: values[0] for key, values in normalized.items() if len(values) == 1}

            required = list(MANIFESTS.values()) + list(JSONL.values())
            for path in required:
                if path not in lookup:
                    report["errors"].append(f"Missing required archive member: {path}")
            if any(path not in lookup for path in required):
                raise ValueError("required manifest or JSONL member missing; see errors")

            pages = json.loads(zf.read(lookup[MANIFESTS["pages"]]))
            assets = json.loads(zf.read(lookup[MANIFESTS["assets"]]))
            if not isinstance(pages, list) or not isinstance(assets, list):
                raise ValueError("Bronze manifests must be JSON arrays")
            report["counts"]["pages_manifest"] = len(pages)
            report["counts"]["assets_manifest"] = len(assets)

            ids = [str(row.get("page_id")) for row in pages]
            dup_ids = [k for k, v in Counter(ids).items() if v > 1]
            report["checks"]["unique_page_ids"] = not dup_ids
            if dup_ids:
                report["errors"].append({"duplicate_page_ids": dup_ids[:100], "total": len(dup_ids)})

            missing_paths, hash_mismatches, missing_hash_fields = [], [], []
            verified = 0
            for row in pages:
                rel = normalize(row.get("raw_path", ""))
                if not rel or rel not in lookup:
                    missing_paths.append({"page_id": row.get("page_id"), "raw_path": row.get("raw_path")})
                    continue
                expected_hash = row.get("raw_sha256")
                if not expected_hash:
                    missing_hash_fields.append(row.get("page_id"))
                    continue
                with zf.open(lookup[rel]) as stream:
                    actual = sha256_stream(stream)
                if actual.lower() != str(expected_hash).lower():
                    hash_mismatches.append({"page_id": row.get("page_id"), "path": rel,
                                            "expected": expected_hash, "actual": actual})
                else:
                    verified += 1
            report["counts"]["page_source_files_verified"] = verified
            report["counts"]["page_source_files_missing"] = len(missing_paths)
            report["counts"]["page_hash_mismatches"] = len(hash_mismatches)
            report["checks"]["all_page_sources_present"] = not missing_paths
            report["checks"]["all_page_hashes_match"] = not hash_mismatches and not missing_hash_fields
            if missing_paths:
                report["errors"].append({"missing_page_sources": missing_paths[:100], "total": len(missing_paths)})
            if hash_mismatches:
                report["errors"].append({"page_hash_mismatches": hash_mismatches[:100], "total": len(hash_mismatches)})
            if missing_hash_fields:
                report["errors"].append({"missing_page_hash_fields": missing_hash_fields[:100], "total": len(missing_hash_fields)})

            for logical, path in JSONL.items():
                count, errors = read_jsonl(zf, lookup, path)
                report["counts"][f"silver_{logical}"] = count
                if errors:
                    report["errors"].extend(errors[:100])
                report["checks"][f"silver_{logical}_jsonl_valid"] = not errors
                if count != expected[logical]:
                    report["errors"].append({"count_mismatch": logical, "expected": expected[logical], "actual": count})

            for logical, actual in (("pages", len(pages)), ("assets", len(assets))):
                if actual != expected[logical]:
                    report["errors"].append({"count_mismatch": f"{logical}_manifest", "expected": expected[logical], "actual": actual})

            asset_names = [n for n in lookup if n.startswith("bronze/assets/")]
            report["counts"]["physical_asset_files"] = len(asset_names)
            if len(assets) == expected["assets"] and len(asset_names) != expected["assets"] - 1:
                report["warnings"].append({"asset_file_count_note": "Historical baseline is 899 physical files for 900 manifest records; observed count differs.", "observed": len(asset_names)})
            report["checks"]["required_members_present"] = True
    except Exception as exc:
        report["errors"].append(f"Fatal validation error: {type(exc).__name__}: {exc}")

    report["status"] = "PASS" if not report["errors"] else "FAIL"
    output = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.report:
        with open(args.report, "w", encoding="utf-8", newline="\n") as f:
            f.write(output)
    else:
        sys.stdout.write(output)
    return 0 if report["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
