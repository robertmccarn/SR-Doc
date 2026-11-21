#!/usr/bin/env python3
"""Conservatively compare infobox claims only when event scope is explicitly aligned."""
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
    scoped_groups = defaultdict(list)
    unscoped_groups = defaultdict(list)

    for claim in claims:
        subject_id = str(claim.get("page_id"))
        event_scope_id = claim.get("event_scope_id")
        template_name = claim.get("template_name")
        field_name = claim.get("normalized_parameter_name")
        if event_scope_id:
            key = (subject_id, str(event_scope_id), template_name, field_name)
            scoped_groups[key].append(claim)
        else:
            # Repeated parameter names in one template are not enough to prove
            # a shared event scope: officeholder infoboxes can encode multiple roles.
            key = (subject_id, claim.get("template_instance_id"), template_name, field_name)
            unscoped_groups[key].append(claim)

    candidates = []
    for (page_id, event_scope_id, template_name, field_name), items in scoped_groups.items():
        distinct = defaultdict(list)
        for item in items:
            distinct[value_key(item.get("raw_parameter_value", ""))].append(item)
        if len(distinct) < 2:
            continue
        candidates.append({
            "candidate_id": f"IC{len(candidates) + 1:04d}",
            "subject_page_id": page_id,
            "subject_title": items[0].get("title"),
            "event_scope_id": event_scope_id,
            "template_name": template_name,
            "parameter_name": items[0].get("parameter_name"),
            "normalized_parameter_name": field_name,
            "comparison_basis": {
                "subject": "same captured page ID",
                "event_scope": "explicit shared event_scope_id supplied by reviewed annotation",
                "field_semantics": "same exact normalized parameter name within the same template family",
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
            "warning": "Competing values are surfaced, not adjudicated. Confirm source context and field semantics before classifying them.",
        })

    unresolved = []
    for (page_id, instance_id, template_name, field_name), items in unscoped_groups.items():
        distinct = defaultdict(list)
        for item in items:
            distinct[value_key(item.get("raw_parameter_value", ""))].append(item)
        if len(distinct) < 2:
            continue
        unresolved.append({
            "subject_page_id": page_id,
            "subject_title": items[0].get("title"),
            "template_instance_id": instance_id,
            "template_name": template_name,
            "parameter_name": items[0].get("parameter_name"),
            "normalized_parameter_name": field_name,
            "status": "not_compared_event_scope_unresolved",
            "distinct_raw_values": [
                {
                    "comparison_value": normalized,
                    "claim_ids": [item.get("claim_id") for item in value_items],
                    "raw_values": [item.get("raw_parameter_value") for item in value_items],
                    "locators": [item.get("provenance", {}).get("locator") for item in value_items],
                }
                for normalized, value_items in distinct.items()
            ],
            "reason": "Repeated values share a page, infobox invocation, and parameter name, but may represent different roles/events or a multi-valued field. No event scope is inferred.",
        })

    return {
        "schema_version": "1.0",
        "claims_evaluated": len(claims),
        "comparison_policy": {
            "compares_only": "claims sharing page ID, explicit reviewed event_scope_id, template family, and exact normalized parameter name",
            "does_not_compare": [
                "claims without an explicit event_scope_id",
                "different page subjects without an explicit entity-equivalence mapping",
                "different parameter names, even when both contain dates",
                "different template families",
            ],
            "normalization": "whitespace collapse only; original raw values remain in evidence",
        },
        "candidate_conflicts": candidates,
        "candidate_count": len(candidates),
        "unresolved_comparisons": unresolved,
        "unresolved_comparison_count": len(unresolved),
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
