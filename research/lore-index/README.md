# SR-Doc lore index

Version 1.0.0 design and navigation contract.

## Deliverables

- [AGENT_NAVIGATION_GUIDE.md](AGENT_NAVIGATION_GUIDE.md) — graph-first retrieval instructions.
- [RELATIONSHIP_MATRIX.md](RELATIONSHIP_MATRIX.md) — predicate semantics, hub/matrix policy, and audit caveats.
- [schema.json](schema.json) — machine-readable node/edge contract.
- Generated datasets to be added after the build is validated: `ENTITY_INDEX.md`, `entity_index.json`, `relationship_graph.json`, and `diagnostics.json`.

## Source inventory

The supplied archive contains 3,579 Bronze Wikitext page records and a Silver extraction layer (`pages.jsonl`, `relations.jsonl`, `timeline.jsonl`). The Silver relation inventory contains 11,462 parsed link records; the year timeline contains 4,447 year mentions. These are extraction-layer counts, not counts of semantic in-world relationships.

## Evidence safeguards

- Main-namespace pages are candidate lore entities; Talk, Thread, User, Template, File, and other namespaces remain source-context unless explicitly classified otherwise.
- A wiki link is navigational/mention evidence, not proof of alliance, control, causation, membership, or ownership.
- Category membership is wiki taxonomy, not necessarily an in-world classification.
- Year mentions are not event dates or temporal validity intervals.
- Preserve source contradictions. Do not resolve aliases or merge entities unless evidence supports the identity match.
- Do not generate transitive semantic edges without validating every hop.
- Every claim-bearing edge must preserve source page ID/title/path, revision, and a locator.

The generated graph is a retrieval aid, not a canon rewrite or substitute for source verification.
