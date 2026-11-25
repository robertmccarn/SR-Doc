# SR-Doc research workspace

**Last reconciled:** 2026-11-24  
**Working branch:** `experiment/corrected-realism`

This directory contains source-grounded audit ledgers, tranche evidence, dependency analysis, and continuity investigations. It does not alter or replace Bronze captures, Silver transformations, or Gold proposals. Bronze source files and manifests remain immutable.

## Start here

- **[AI session swap memory](../.ai/swap.md)** — compact current-state handoff for fresh ChatGPT windows; verify its claims against Git.
- **[Swap memory standards](continuity/DOCUMENTATION-GOVERNANCE.md#12-repo-backed-ai-swap-memory)** — required memory boundaries, update cadence, authority, and security rules.

0. **[Research assistant protocol](continuity/RESEARCH-ASSISTANT-PROTOCOL.md)** — mandatory evidence, citation, contradiction, and abstention contract for lore answers.
1. **[RAG implementation plan](rag/README.md)** — architecture and next build steps. A local read-only lexical retrieval prototype is implemented; exact-title/redirect lookup and date-bearing contrast retrieval are available.
2. **[Evidence packet schema](rag/evidence-packet.schema.json)** — machine-readable handoff format.
3. **[Initial evaluation set](rag/evaluation-set-001.md)** — 20-case baseline approved by the maintainer; all ten source identities, 51 locator/content ranges, and seven title/map-boundary checks passed. Retrieval pass 001 found all expected pages within top five unique candidates, with 47/55 first-stage locator coverage and 55/55 after full-page expansion. Manual answer-generation pass 001 now records 20/20 answer-key-compliant outputs, including all required contradiction disclosures and abstentions; this is not a runtime or independent-scoring result. See [locator validation](rag/evaluation-locator-validation-001.json), [retrieval benchmark](rag/retrieval-benchmark-pass-001.json), and [answer-generation evaluation](rag/answer-generation-pass-001.md).
- **[Infobox claim schema](rag/infobox-claim.schema.json)** — provenance-preserving derived parameter claim contract.
- **[Infobox extractor](rag/extract_infobox_claims.py)** and **[conservative comparison](rag/evaluate_infobox_claims.py)** — raw values and explicitly scoped candidate review; five parser/comparison regression tests passed in GitHub Actions, and the committed extractor ran against the pinned archive with 4,381/4,381 claims passing schema and offset/provenance validation. See [validation report](rag/infobox-claim-validation-001.json) and [pass-001 evidence](rag/infobox-claims-pass-001.md).
- **[Retrieval benchmark pass 001](rag/retrieval-benchmark-pass-001.json)** — approved 20-case baseline; page recall, first-stage/full-page locator coverage, exact-title/redirect resolution, schema findings, precision caveats, and unscored answer metrics.
- **[Answer-generation evaluation pass 001](rag/answer-generation-pass-001.md)** — 20 source-grounded manual answers; 20/20 answer-key compliance, contradiction disclosure, and abstention checks, with explicit runtime/independence limitations.

5. **[Documentation governance](continuity/DOCUMENTATION-GOVERNANCE.md)** — required protocol for all agent documentation changes.
6. **[Master research register](continuity/MASTER-RESEARCH-REGISTER.md)** — canonical status, evidence hierarchy, reconciled counts, findings, full note inventory, and next work.
7. **[Agent operating guide](../agents.md)** — concise instructions for future sessions.
8. **[Session log](session-log.md)** — append-only chronology. Earlier entries are historical and may contain checkpoint counts superseded by later work.
9. Detailed evidence is retained in the tranche and thematic notes listed below.

## Current verified status

| Workstream | Current result |
|---|---|
| Page corpus | 3,579/3,579 records directly read and SHA-256 verified |
| Main namespace | 507/507 |
| Media manifest | 900 records |
| Physical media | 899 available; one missing/failed asset (entry 815, page ID 3525, `File:K8ch1z55ucnz.png`) |
| Media integrity | 728 exact SHA-1/size matches; 171 mismatches; zero decode/parse failures among 899 available files |
| Media visual triage | All 899 available files visually triaged at contact-sheet thumbnail scale; not forensic or semantic validation |
| Media/page cross-reference | 792 exact extracted references; 11 literal-only mentions; 97 with no discovered mention; 1,696 exact-reference edges |
| File namespace | 906 File pages; all 900 media-record page IDs resolve; six File pages outside media manifest |
| Extracted image titles | 933 distinct titles; 141 have no exact counterpart in the 900-record media manifest |

See the master register for definitions and interpretation limits. In particular, raw mentions do not prove rendered use, extracted metadata is not a complete rendered dependency graph, and no discovered reference does not prove orphan status.

## Research assistant / RAG

The RAG workstream now includes a source-grounded answer protocol, evidence packet schema, maintainer-approved 20-question evaluation baseline, archive validator, section-aware chunk builder, SQLite FTS5 index builder, and evidence-packet search CLI. The initial build produced 7,598 unique chunks across 3,092 text-bearing pages, with metadata for all 3,579 page records. 487 records have no non-whitespace text, including three empty main-namespace pages. Default search is main namespace only; context namespaces require explicit inclusion. The packaged index is a local artifact, not committed as a binary; detailed build results are in `rag/chunk-build-report-001.json`, with smoke tests in `rag/retrieval-smoke-tests-001.json`. Alias resolution is implemented. First-pass contrast retrieval surfaces date-bearing review candidates without adjudicating them. Source-aware infobox parameter extraction has been executed against the pinned archive: 507 main-namespace pages, 143 infobox invocations, and 4,381 parameter claims; all records passed the claim schema and raw-offset/provenance checks, and a repeat run was byte-identical. Comparison requires the same page subject, an explicit reviewed event-scope ID, template family, and exact field name; the two repeated-field groups without event-scope alignment remain unresolved. Retrieval benchmark pass 001 found all expected page IDs within the top five unique page candidates, but first-stage locator coverage was 47/55 and required full-page expansion to reach 55/55. The evidence-packet resolution-status schema mismatch was corrected and the new contract tests passed in GitHub Actions. Generated-answer/citation scoring remains outstanding; see `rag/retrieval-benchmark-pass-001.json`.

## Lore graph/index

- `lore-index/README.md` — graph/index scope and evidence safeguards.
- `lore-index/AGENT_NAVIGATION_GUIDE.md` — graph-first retrieval protocol.
- `lore-index/RELATIONSHIP_MATRIX.md` — directional predicate definitions and temporal/contradiction rules.
- `lore-index/schema.json` — machine-readable node/edge contract.
- The graph completion script, semantic infobox extractor, and validation reports are committed. The latest semantic graph/entity index are distributed as a ZIP artifact; see the lore-index README for counts and limitations.

## Corpus inventory and ledgers

- `page-ledger.csv` — 3,579 page records, source identifiers, SHA-256, review status, and notes.
- `media-ledger.csv` — 900 media records, source URL, SHA-1, size, mapping, and visual-inspection results.
- `session-log.md` — chronological record of work actually performed.

### Page-manifest tranche notes

- `page-notes/main-181-210.md`
- `page-notes/main-211-240.md`
- `page-notes/manifest-001-300.md`
- `page-notes/manifest-301-600.md`
- `page-notes/manifest-601-900.md`
- `page-notes/manifest-901-1200.md`
- `page-notes/manifest-1201-1500.md`
- `page-notes/manifest-1501-1800.md`
- `page-notes/manifest-1801-2100.md`
- `page-notes/manifest-2101-2400.md`
- `page-notes/manifest-2401-2700.md`
- `page-notes/manifest-2701-3000.md`
- `page-notes/manifest-3001-3300.md`
- `page-notes/manifest-3301-3579.md`

### Media binary audit

- `media-notes/manifest-001-300.md`
- `media-notes/manifest-301-600.md`
- `media-notes/manifest-601-900.md`

### Media cross-reference and dependency notes

- `media-notes/crossref-001-300.md`
- `media-notes/crossref-301-600.md`
- `media-notes/crossref-601-900.md`
- `media-notes/dependency-reconciliation-pass-001.md`
- `media-notes/targeted-unmatched-dependencies-001.md`

### Continuity research

- `continuity/china-political-history-pass-001.md` — Chinese civil-war/state-succession timeline and source-level contradictions.
- `continuity/DOCUMENTATION-GOVERNANCE.md` — normative, self-referencing documentation maintenance protocol.
- `continuity/MASTER-RESEARCH-REGISTER.md` — canonical synthesis and complete note inventory.
- `continuity/agents-md-history-2026-11-20.md` — verbatim preservation of the former long `agents.md`; archival only, not current guidance.

## Non-canon editorial experiment

- **[Corrected-realism proposal, 2024–2034](continuity/corrected-realism-proposal-001.md)** — alternate-history editorial proposal to make the Flood, Great Famine, Market Crash, White Tide, geopolitical fragmentation, American Renewal, and space-exploration chronology more consistent with external scientific and institutional context. Proposal only; no canon or Bronze/Silver source data changed.

## Method and status definitions

- **Page read/verified:** exact Bronze Wikitext path was opened/read and SHA-256 matched the page manifest.
- **Exact extracted media reference:** exact File title occurs in extracted page `images` metadata.
- **Literal-only media mention:** absent from exact extracted references but filename occurs in raw source; this may be prose, template/module configuration, alias, or Thread content.
- **No discovered mention:** neither exact extracted metadata nor the defined raw filename search found a match; not an orphan determination.
- **Visual triage:** contact-sheet thumbnail review of available decoded files; not authenticity or semantic validation.

Talk, Thread, User, and other community namespaces are editorial/contextual evidence, not automatically canon. Contradictory source values must be recorded, not silently corrected.

## Workflow rules

1. Use the original Bronze Wikitext and manifests as source evidence.
2. Preserve exact source/manifests; do not overwrite or normalize them.
3. Separate page read/hash status, media checksum status, visual triage, semantic review, and continuity validation.
4. For dependencies, distinguish explicit wikilinks, extracted metadata, template/module aliases, File redirects, and rendered output.
5. For continuity claims, record date, source, exact claim, confidence, and conflicting evidence.
6. Preserve detailed tranche notes; consolidate through indexing and cross-linking, not deletion.
7. Update the master register and this README when status materially changes; append to the session log.
8. No merge, PR, branch promotion, or canon edits without explicit user approval.


### RAG retrieval update — 2026-11-20

The local SQLite FTS5 prototype now supports exact page IDs, lexical main-namespace search, exact captured titles, and direct Wikitext redirect resolution. Run `build_alias_index.py` after the base index build to populate title/redirect keys. Redirect aliases preserve original page ID and target provenance; unresolved and ambiguous targets are not guessed. See [RAG implementation details](rag/README.md).


### RAG retrieval update — contrast pass 001

The search CLI now accepts `--contrast` to diversify lexical matches across pages and surface passages containing multiple year ranges for manual comparison. Four regression checks pass locally, including the Second Chinese Civil War 2027–2048 / 2105–2111 conflict on page 1413. This feature produces review candidates, not adjudicated contradictions. See [RAG implementation details](rag/README.md) and [test_search.py](rag/test_search.py).
