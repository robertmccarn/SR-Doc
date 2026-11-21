#!/usr/bin/env python3
"""Conservatively identify repeated infobox-field values within one source scope."""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


def value_key(value: str) -> str:
    """Ignore whitespace-only formatting differences; preserve all other markup."""
    return re.sub(r"\s+", " ", value).strip()


def evaluate_claims(claims: list[dict]) -> dict:
    groups = defaultdict(list)
    for claim in claims:
        # A page is the subject identity; one exact infobox invocation and one exact
        # parameter name provide the narrowest defensible event/field comparison scope.
        key = (
            str(claim.get("page_id")),
            claim.get("template_instance_id"),
            claim.get("normalized_parameter_name"),
        )
        groups[key].append(claim)

    candidates = []
    for (page_id, instance_id, field_name), items in groups.items():
        distinct = {}
        for item in items:
            distinct.setdefault(value_key(item.get("raw_parameter_value", "")), []).append(item)
        if len(distinct) < 2:
            continue
        candidates.append({
            "candidate_id": f"IC{len(candidates) + 1:04d}",
            "subject_page_id": page_id,
            "subject_title": items[0].get("title"),
            "template_name": items[0].get("template_name"),
            "template_instance_id": instance_id,
            "parameter_name": items[0].get("parameter_name"),
            "normalized_parameter_name": field_name,
            "comparison_basis": {
                "subject": "same captured page ID",
                "event_scope": "same infobox invocation",
                "field_semantics": "same exact normalized parameter name",
            },
            "distinct_raw_values": [
                {
                    "comparison_value": normalized,
                    "claim_ids": [item.get("claim_id") for item in value_items],
                    "raw_values": [item.get("raw_parameter_value") for item in value_items],
                    "locators": [item.get("provenance", {}).get("locator") for item in value_items],
                }
                for normalized, value_items in distinct.items()
            ],
            "status": "candidate_conflict_requires_source_review",
            "warning": "Competing values are surfaced, not adjudicated. Confirm template semantics and source context before classifying them.",
        })

    return {
        "schema_version": "1.0",
        "claims_evaluated": len(claims),
        "comparison_policy": {
            "compares_only": "claims sharing page ID, exact infobox invocation, and exact normalized parameter name",
            "does_not_compare": [
                "different page subjects without an explicit entity-equivalence mapping",
                "different parameter names, even when both contain dates",
                "claims with unknown or unaligned event scope",
            ],
            "normalization": "whitespace collapse only; original raw values remain in evidence",
        },
        "candidate_conflicts": candidates,
        "candidate_count": len(candidates),
        "adjudication": "none",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("claims", help="JSONL produced by extract_infobox_claims.py")
    parser.add_argument("--output", default="infobox-claim-comparison.json")
    args = parser.parse_args()
    claims = []
    with Path(args.claims).open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, 1):
            if line.strip():
                try:
                    claims.append(json.loads(line))
                except json.JSONDecodeError as error:
                    raise SystemExit(f"Invalid JSON on line {line_number}: {error}")
    result = evaluate_claims(claims)
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
