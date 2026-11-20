# SR-Doc lore index

Version 1.0.0 design and navigation contract.

## Deliverables

- [AGENT_NAVIGATION_GUIDE.md](AGENT_NAVIGATION_GUIDE.md) — graph-first retrieval instructions.
- [RELATIONSHIP_MATRIX.md](RELATIONSHIP_MATRIX.md) — predicate semantics, hub/matrix policy, and audit caveats.
- [schema.json](schema.json) — machine-readable node/edge contract.
- The validated prototype package includes `ENTITY_INDEX.md`, `entity_index.json`, `relationship_graph.json`, `build_validation.json`, and `build_lore_graph.py`. The large graph JSON is currently distributed as a package artifact; the repository stores the reproducible completion script and validation report.

## Source inventory

The supplied archive contains 3,579 Bronze Wikitext page records and a Silver extraction layer (`pages.jsonl`, `relations.jsonl`, `timeline.jsonl`). The Silver relation inventory contains 11,462 parsed link records; the year timeline contains 4,447 year mentions. The corrected graph preserves all 11,462 links and all 4,447 year mentions, including non-main namespaces. It contains 7,073 nodes and 15,967 edges, including 456 explicit year-token nodes. These are extraction-layer counts, not counts of semantic in-world relationships.

## Evidence safeguards

- Main-namespace pages are candidate lore entities; Talk, Thread, User, Template, File, and other namespaces remain source-context unless explicitly classified otherwise.
- A wiki link is navigational/mention evidence, not proof of alliance, control, causation, membership, or ownership.
- Category membership is wiki taxonomy, not necessarily an in-world classification.
- Year mentions are not event dates or temporal validity intervals.
- Preserve source contradictions. Do not resolve aliases or merge entities unless evidence supports the identity match.
- Do not generate transitive semantic edges without validating every hop.
- Every claim-bearing edge must preserve source page ID/title/path, revision, and a locator. `build-validation.json` records zero duplicate IDs and zero missing edge endpoints.

The generated graph is a retrieval aid, not a canon rewrite or substitute for source verification.


## Semantic extraction status — pass 001

- `extract_infobox_edges.py` extracts conservative, source-grounded relationships from five recognized infobox templates.
- `semantic-extraction-001.json` records the pass counts and limitations.
- `RELATIONSHIP-MATRIX-SEMANTIC-001.md` documents the 58 added edges.
- The graph package `SR-Doc-Lore-Graph-Semantic-001.zip` contains the expanded graph with 7,073 nodes and 16,025 edges (116 structured infobox edges).
- Only exact linked field values resolving to main-namespace entity nodes are emitted; no plain-text alias resolution or transitive inference is performed.
