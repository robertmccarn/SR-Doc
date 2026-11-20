#!/usr/bin/env python3
"""Complete the SR-Doc lore graph from the first prototype and Silver JSONL inputs.

Preserves every parsed wiki-link and year-mention record, adds year-token nodes,
retains empty link targets as unresolved, and validates all edge endpoints.
Does not modify Bronze/Silver inputs or infer transitive semantic claims.
"""
import argparse, json, hashlib, re
from pathlib import Path
from collections import Counter

def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def write_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-graph", required=True)
    ap.add_argument("--pages", required=True)
    ap.add_argument("--relations", required=True)
    ap.add_argument("--timeline", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    graph = json.loads(Path(args.base_graph).read_text(encoding="utf-8"))
    pages = read_jsonl(args.pages)
    relations = read_jsonl(args.relations)
    timeline = read_jsonl(args.timeline)
    page_by_id = {p["page_id"]: p for p in pages}
    nodes = {n["id"]: n for n in graph["nodes"]}
    entity_by_page = {n["page_id"]: n["id"] for n in graph["nodes"] if n.get("page_id") is not None}
    # Replace the prototype's aggregate year edges with one edge per source record.
    edges = {e["id"]: e for e in graph["edges"] if e.get("predicate") != "MENTIONS_YEAR"}

    # Preserve all parsed wiki-link records. The sole empty target is represented
    # by a stable unresolved placeholder, not silently discarded.
    for rel in relations:
        pid = rel["from_page_id"]
        page = page_by_id[pid]
        target_title = rel.get("to_title") or ""
        target_id = ("unresolved_link_target:empty-title" if not target_title else
                     "unresolved_link_target:" + hashlib.sha1(target_title.encode()).hexdigest()[:16])
        nodes.setdefault(target_id, {
            "id": target_id, "canonical_name": target_title or "[empty link target]",
            "entity_type": "unresolved_link_target", "namespace": "unresolved",
            "aliases": [], "summary": None,
            "classification_method": "parsed_link_target_unresolved", "status": "unresolved"
        })
        source_id = entity_by_page.get(pid, f"page:{pid}")
        edges[rel["id"]] = {
            "id": rel["id"], "source": source_id, "predicate": "WIKI_LINKS_TO",
            "target": target_id, "bidirectional": False, "inverse_predicate": "LINKED_FROM",
            "temporal_scope": None, "certainty": "explicit_link",
            "evidence_strength": "direct_structural",
            "evidence": {
                "source_path": page["raw_path"], "source_page_id": pid,
                "source_title": page["title"], "revision_id": page["revision_id"],
                "offset": rel.get("source", {}).get("offset"),
                "target_title": target_title,
                "unresolved_reason": "empty_target_title" if not target_title else "target_not_resolved_by_base_graph"
            }, "weight": 0.5
        }

    # Preserve every timeline row, including community/template/file namespaces.
    years = sorted({str(row["year"]) for row in timeline}, key=int)
    for row in timeline:
        pid = row["source"]["page_id"]
        page = page_by_id[pid]
        edges[row["id"]] = {
            "id": row["id"], "source": entity_by_page.get(pid, f"page:{pid}"),
            "predicate": "MENTIONS_YEAR", "target": f"year:{row['year']}",
            "bidirectional": False, "inverse_predicate": "YEAR_MENTIONED_IN",
            "temporal_scope": None, "certainty": "explicit_text_extraction",
            "evidence_strength": "mention_only",
            "evidence": {
                "source_path": page["raw_path"], "source_page_id": pid,
                "source_title": page["title"], "revision_id": page["revision_id"],
                "year": str(row["year"])
            }, "weight": 0.35
        }
    for year in years:
        nid = f"year:{year}"
        nodes.setdefault(nid, {
            "id": nid, "canonical_name": year, "entity_type": "year_token",
            "namespace": "timeline", "aliases": [],
            "summary": "Extracted year token; not an event or validity interval.",
            "classification_method": "explicit_text_extraction", "status": "mention_only"
        })

    graph["nodes"] = sorted(nodes.values(), key=lambda n: n["id"])
    graph["edges"] = sorted(edges.values(), key=lambda e: e["id"])
    graph["source_corpus"]["silver_relation_records"] = len(relations)
    graph["source_corpus"]["silver_timeline_records"] = len(timeline)
    graph["semantics"]["empty_link_policy"] = "Empty parsed targets are retained as unresolved placeholder nodes."
    graph["semantics"]["timeline_policy"] = "Every extracted year mention is retained across all namespaces; year tokens are nodes, not event dates."

    node_ids = {n["id"] for n in graph["nodes"]}
    missing = [e["id"] for e in graph["edges"] if e["source"] not in node_ids or e["target"] not in node_ids]
    predicates = Counter(e["predicate"] for e in graph["edges"])
    report = {
        "source_counts": {"pages": len(pages), "parsed_links": len(relations), "year_mentions": len(timeline)},
        "graph_counts": {"nodes": len(graph["nodes"]), "edges": len(graph["edges"]),
                         "predicates": dict(predicates), "year_nodes": len(years)},
        "validation": {
            "duplicate_node_ids": len(graph["nodes"]) - len(node_ids),
            "duplicate_edge_ids": len(graph["edges"]) - len(edges),
            "edges_with_missing_endpoints": len(missing),
            "all_relation_records_preserved": all(r["id"] in edges for r in relations),
            "all_timeline_records_preserved": all(t["id"] in edges for t in timeline)
        },
        "limitations": ["Year mentions are not event dates.", "Empty link target remains unresolved.",
                        "No transitive semantic edges are generated."]
    }
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "relationship_graph.json", graph)
    write_json(out / "build_validation.json", report)
    print(json.dumps(report, indent=2))
    if missing or not report["validation"]["all_relation_records_preserved"] or not report["validation"]["all_timeline_records_preserved"]:
        raise SystemExit("Graph validation failed")

if __name__ == "__main__":
    main()
