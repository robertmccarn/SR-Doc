# SR-Doc research — master register and audit status

**Last reconciled:** 2026-11-20  
**Working branch:** `audit/continuity-research`  
**Purpose:** Canonical navigation, status, definitions, findings, and handoff for the research notes. This register supersedes stale progress summaries in older append-only notes, but does not replace their detailed evidence.

## Research assistant / RAG workstream

- Answer contract: `research/continuity/RESEARCH-ASSISTANT-PROTOCOL.md` — normative retrieval, evidence, citation, contradiction, and abstention rules for lore answers.
- Implementation plan: `research/rag/README.md` — staged architecture, corpus contract, retrieval design, evaluation criteria, risks, and next coding task.
- Evidence transport: `research/rag/evidence-packet.schema.json` — JSON Schema 1.0 for portable retrieved evidence packets.
- Evaluation seed: `research/rag/evaluation-set-001.md` — 20 candidate questions across direct facts, entity resolution, timelines, relationships, contradictions, and abstention. Not yet scored or fully source-keyed.
- **Current status:** protocol/schema/evaluation seed, read-only archive validator, section-aware chunker, SQLite FTS5 index builder, exact-title/redirect index builder, evidence-packet search CLI, source-aware infobox claim extractor, claim schema, and conservative same-scope comparison CLI are committed. Archive SHA-256: `d1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8`. Corpus: 3,579 page metadata rows, 7,598 unique chunks, 7,598 FTS rows; 3,092 pages have text chunks. 487 captured records have no non-whitespace text, including three empty main-namespace pages. Default lexical search is main namespace only; context namespaces require explicit inclusion. Exact title/redirect lookup is opt-in via `--title` and preserves redirect provenance. Smoke tests passed; no benchmark score yet.

## Documentation governance

- Normative maintenance protocol: `research/continuity/DOCUMENTATION-GOVERNANCE.md`.
- Every agent must read it before editing research documentation.
- `agents.md` is the concise entry point; this register is canonical current factual status; README is the concise mirror; session log is append-only; detailed notes preserve evidence.

## Authority and precedence

When notes conflict, use this order:

1. Original Bronze source files and their manifests are evidence of what was captured.
2. Current audit ledgers and detailed tranche notes record checks actually performed.
3. This register and `research/README.md` provide the current reconciled status.
4. `research/session-log.md` is an append-only chronology; older entries are historical and may contain progress statements later superseded.
5. `research/continuity/agents-md-history-2026-11-20.md` is a verbatim archive of the former long `agents.md`; it is historical, not current instructions.
6. Conversational summaries and prior handoff claims are not substitutes for source evidence.

Do not silently alter Bronze captures, manifest contents, source Wikitext, or canon. This work is an audit, not an editorial rewrite.

## Current verified progress

### Page corpus

- Page manifest: **3,579 records** across all namespaces.
- Raw Wikitext paths in supplied archive: **3,579 / 3,579 present**.
- Direct reads and SHA-256 verification: **3,579 / 3,579**.
- Main namespace: **507 / 507**.
- Final completed tranche: manifest entries 3301–3579; 279 records in tranche, 270 new unique reads because of previously reviewed overlap.
- Page review is complete. Do not restart bulk page tranches unless a targeted cross-reference or a reproducibility check requires it.

### Media binary corpus

- Asset manifest: **900 records**.
- Physical files: **899**; one missing/failed record is manifest entry 815, page ID 3525, `File:K8ch1z55ucnz.png`.
- All 899 available assets were decoded/parsed and visually triaged at contact-sheet thumbnail scale.
- SHA-1 and byte-size results: **728 exact matches; 171 mismatches; one unavailable asset**.
- Zero decode/parse failures among the 899 physical files.
- Thumbnail inspection is not forensic validation, source authenticity verification, or semantic/canon verification.

### Media-to-page cross-reference

The three ordered 300-record tranches are complete:

| Manifest range | Exact extracted refs | Literal-only | No discovered mention | Exact edges |
|---|---:|---:|---:|---:|
| 1–300 | 268 | 6 | 26 | 876 |
| 301–600 | 284 | 1 | 15 | 525 |
| 601–900 | 240 | 4 | 56 | 295 |
| **Total** | **792** | **11** | **97** | **1,696** |

Definitions:
- **Exact extracted reference:** exact File title occurs in the page manifest's extracted `images` metadata.
- **Literal-only:** no exact extracted reference, but a filename mention was found in raw source text. This includes template/module/prose/Thread contexts and does not prove rendered use.
- **No discovered mention:** neither exact extracted metadata nor the defined raw filename search found a match. This does not prove an orphan.
- **Exact edge:** one asset-to-page reference in extracted metadata.

Independent raw-Wikitext scan found 441 distinct media-manifest titles in explicit `[[File:...]]`/`[[Image:...]]` wikilinks (749 occurrences). None of the 108 assets without exact extracted metadata had an exact normalized explicit File/Image wikilink in raw source. Extracted metadata and raw wikilinks measure different things; do not conflate them.

### File pages and extracted image-title inventory

- File namespace: **906 page records**.
- Every one of the 900 media-manifest asset page IDs resolves to a File-namespace page.
- Six File pages are outside the media manifest: `File:Example.jpg`, `File:Communitylogo.png`, `File:Wiki.png`, and three redirects:
  - `File:180px-Gerald Ford.jpg` → `File:Gerald Ford.jpg`
  - `File:465px-William McKinley 1.png` → `File:William McKinley 1.png`
  - `File:Eagle 7 Booster.png` → `File:Eagle 9 Booster.png`
- Extracted page metadata contains **933 distinct image titles**, of which 141 have no exact counterpart in the 900-record media manifest.
- Those 141 unmatched titles are primarily template/module dependencies: 128 referenced only from Template namespace, five only Module, three only main namespace, two Template+Module, and one each User, Thread, and File namespace.
- Do not interpret 141 unmatched titles as 141 missing article images.

## Canonical note inventory

### Research assistant / RAG
- `research/rag/validate_archive.py` — read-only archive structure, page SHA-256, manifest count, and Silver JSONL validator.
- `research/rag/archive-validation-001.json` — passing report for the supplied `SR-Doc-Audit.zip` snapshot.\n- `research/rag/build_index.py` — section-aware, provenance-preserving chunk and SQLite FTS5 builder.\n- `research/rag/search.py` — lexical search, exact-title/redirect resolution, and schema-shaped evidence packet CLI.
- `research/rag/build_alias_index.py` — post-build exact-title and captured redirect index builder.\n- `research/rag/chunk-build-report-001.json` — chunk coverage and index build results.
- `research/rag/retrieval-smoke-tests-001.json` — initial lexical, page-ID, and namespace-safety smoke tests.
- `research/continuity/RESEARCH-ASSISTANT-PROTOCOL.md` — normative answer and evidence-handling contract.
- `research/rag/README.md` — architecture and staged implementation plan.
- `research/rag/evidence-packet.schema.json` — machine-readable evidence packet schema.
- `research/rag/evaluation-set-001.md` — initial 20-question evaluation set; authoring template, not scored.
- `research/rag/extract_infobox_claims.py` — read-only, provenance-preserving infobox parameter claim extractor.
- `research/rag/infobox-claim.schema.json` — machine-readable claim record contract.
- `research/rag/evaluate_infobox_claims.py` — conservative comparison of repeated values in the same page/infobox/field scope.
- `research/rag/test_infobox_claims.py` — parser/comparison regression tests; execution remains pending.


### Core navigation and ledgers
- `research/README.md` — concise project status and navigation.
- `research/session-log.md` — append-only work chronology; read with historical-status caveat.
- `research/page-ledger.csv` — page-level read/hash/review ledger.
- `research/media-ledger.csv` — all 900 media records and audit results.
- `agents.md` — current operating instructions and short handoff only.
- `research/continuity/DOCUMENTATION-GOVERNANCE.md` — normative rules for maintaining this documentation system.
- `research/continuity/MASTER-RESEARCH-REGISTER.md` — this canonical register.
- `research/continuity/agents-md-history-2026-11-20.md` — verbatim archival copy of former long agents.md.

### Page review tranches
- `research/page-notes/main-181-210.md`
- `research/page-notes/main-211-240.md`
- `research/page-notes/manifest-001-300.md`
- `research/page-notes/manifest-301-600.md`
- `research/page-notes/manifest-601-900.md`
- `research/page-notes/manifest-901-1200.md`
- `research/page-notes/manifest-1201-1500.md`
- `research/page-notes/manifest-1501-1800.md`
- `research/page-notes/manifest-1801-2100.md`
- `research/page-notes/manifest-2101-2400.md`
- `research/page-notes/manifest-2401-2700.md`
- `research/page-notes/manifest-2701-3000.md`
- `research/page-notes/manifest-3001-3300.md`
- `research/page-notes/manifest-3301-3579.md`

### Media binary audit
- `research/media-notes/manifest-001-300.md`
- `research/media-notes/manifest-301-600.md`
- `research/media-notes/manifest-601-900.md`

### Cross-reference and dependency review
- `research/media-notes/crossref-001-300.md`
- `research/media-notes/crossref-301-600.md`
- `research/media-notes/crossref-601-900.md`
- `research/media-notes/dependency-reconciliation-pass-001.md`
- `research/media-notes/targeted-unmatched-dependencies-001.md`

### Continuity synthesis
- `research/continuity/china-political-history-pass-001.md`

The page/media tranche notes remain the detailed evidence record. This index is not a replacement for them.

## Reconciled substantive findings

### Dependency audit
- Three unmatched extracted titles received direct context review:
  - `Blank.png` on Al-Hasa: extracted metadata artifact is likely; raw infobox `image_map` is empty.
  - `Republic of China (orthographic projection historical).svg`: explicitly assigned as `image_map` on both United Federation of China and Federal Republic of China. This is a genuine intended dependency, but the binary and File page are absent from the supplied archive; actual map content remains unknown.
  - `Slider` on Second Renaissance Wikia: bare token within `<gallery type="slider">`, not a conventional missing file.
- Of 11 literal-only media mentions, contexts include legacy country-data naming, one direct Xanthe flag-alias configuration, portal module mapping, Thread welcome-message links, and filename near-matches. See the detailed dependency note for each case. None should be automatically upgraded to confirmed rendered use.

### Chinese political-history audit
Source-level inconsistencies requiring follow-up:
1. Second Chinese Civil War infobox dates 2027–2048, but its combatant block includes 2105–2111, overlapping the separately named Third Chinese Civil War.
2. Third Chinese Civil War begins 2105 and continues in phases through 2126; United Federation of China is dated 2058–2108; Federal Republic of China is dated 2108–2139. The post-2108 government/war succession is underexplained.
3. United Federation and Federal Republic infoboxes retain Republic of China historical events from 1911–1949. UFC era is labelled 20th century. Federal Republic has BLANK leaders with 1912/1949 years and 1912 statistics; its prose/history is a stub.
4. Association of East Asia is asserted as successor/integrator, but no substantive page under the exact queried title was located in the reviewed corpus. Verify canonical title/variant before calling the article absent.
5. World War III chronology and the 2048 Japanese campaign in China may be reconcilable as pre-global-war hostilities, but the relationship needs explicit source explanation.

These are audit findings, not permission to rewrite canon. The Chinese audit is based on the named pages listed in its note; it is not yet a full audit of all related Talk/Thread editorial context.

## Important corrections to stale summaries

Older portions of README and the archived agents handoff contained progress statements that were true at earlier checkpoints but later became obsolete. The current values above supersede statements such as:
- media visual inspection 0/900 or 300/900 / 600/900;
- media physical mapping incomplete;
- page corpus incomplete or only prior-claim verified;
- cross-reference phase still underway;
- next media tranche not yet reviewed.

The append-only session log deliberately retains chronology. It should not be rewritten to erase earlier statements; add dated correction/reconciliation entries instead.

## Method and interpretation rules

1. Distinguish manifest record counts, unique titles, physical files, page references, and reference edges.
2. Distinguish raw source mentions, extracted `images` metadata, explicit wikilinks, template aliases, and actual rendered dependencies.
3. Do not label a file orphaned solely because no extracted/raw mention was found.
4. Do not label an image rendered solely because a template parameter or filename mention exists.
5. Talk, Thread, User, and other community namespaces are editorial/contextual evidence, not automatically canon.
6. Preserve contradictory values in source notes and describe conflicts without silently choosing a correction.
7. Cite exact source pages/manifest records in new findings wherever possible.
8. Preserve Bronze files and manifests; never normalize or overwrite source captures during audit.
9. Keep detailed tranche notes intact; summarize them here without dropping information from the repository.
10. When adding work, update this register, README, and session log only when status meaningfully changes. Keep `agents.md` operational and concise.

## Lore graph/index initiative — initial schema and navigation layer

- Added `research/lore-index/README.md`, `AGENT_NAVIGATION_GUIDE.md`, `RELATIONSHIP_MATRIX.md`, and `schema.json` on 2026-11-20.
- The supplied archive includes 3,579 Bronze page records and a Silver extraction layer with 11,462 parsed-link records and 4,447 year mentions. These are source/extraction counts, not semantic relationship counts.
- The committed schema deliberately separates navigational links, category taxonomy, year mentions, and structured infobox claims. It requires directional edges, inverse predicates, temporal scope, certainty, evidence strength, and source locators.
- Full graph/index generation and validation remain pending repository integration. Do not describe the graph JSON or entity index as committed until the generated artifacts are present and fetched back from GitHub.
- This initiative is an indexing layer only; it does not modify canon or resolve existing continuity conflicts.

## Lore graph/index initiative — corrected extraction coverage

- Initial graph prototype was audited against the exact Silver JSONL source records. The earlier displayed count of 117 category nodes was incorrect; the prototype contains 116.
- The prototype omitted one parsed wiki-link record because its target title was empty. It also emitted only main-namespace year mentions (3,665 of 4,447), and lacked explicit year-token nodes, leaving all 3,665 year edges with unresolved endpoints.
- Corrected build restores all 11,462 parsed link records, retaining the empty target as an unresolved placeholder; replaces aggregated year edges with all 4,447 source timeline records across namespaces; and adds 456 year-token nodes.
- Corrected graph totals: **7,073 nodes; 15,967 edges** (11,462 wiki links, 4,447 year mentions, 58 infobox-derived edges). Validation: zero duplicate node IDs, zero duplicate edge IDs, zero missing edge endpoints.
- Added `research/lore-index/build_lore_graph.py` and `build-validation.json`. The full corrected graph and entity index are distributed in the corrected prototype ZIP; the large graph JSON has not yet been committed as a repository file.
- This is still a graph completion pass over the first prototype, not a full rebuild of entity resolution or semantic extraction. Year mentions are not event dates; infobox edges remain source claims, not adjudicated truth.

## Lore graph/index — semantic infobox expansion pass 001

- Scanned all 507 main-namespace pages and identified 119 calls across five recognized templates: officeholder (29), military conflict (18), country (34), former country (33), and political party (5).
- Extracted 113 exact wikilinked field candidates. Fifty-five equivalent claims were already present; 58 new edges were added: 29 `MEMBER_OF`, 11 `HAS_COMMANDER`, 10 `HAS_COMBATANT`, five `HOLDS_OFFICE_IN`, and three `HAS_STATED_RESULT`.
- Expanded graph: **7,073 nodes; 16,025 edges; 116 structured infobox edges**. Validation: unique edge IDs and all endpoints resolve.
- Added `research/lore-index/extract_infobox_edges.py`, `semantic-extraction-001.json`, and `RELATIONSHIP-MATRIX-SEMANTIC-001.md`.
- Scope limitations: five of ten observed infobox template families modeled; 23 calls across election, government agency, company, military unit, and international-organization templates remain unmodeled. Only exact wikilinks are resolved; plain-text values are not guessed. Raw Wikitext parameters are inspected, not MediaWiki-rendered. Edges are source claims, not adjudicated canon.

## Next recommended work

1. Review relevant Talk/Thread editorial discussions for the Chinese succession and civil-war chronology, distinguishing creator intent from canon text.
2. Resolve canonical title and source availability for Association of East Asia.
3. Recover the historical orthographic projection map from an authorized captured/source location if available; do not infer or redraw its territorial content.
4. Build a claim/evidence matrix for the Chinese succession (dates, government, leaders, territorial claims, war phases, successor entities) before proposing any edits.
5. Continue other high-impact continuity audits only after choosing a bounded topic and enumerating the exact source pages.

## Safety rails

- Branch: `audit/continuity-research`.
- No merge, PR, branch promotion, or canon edits without explicit user approval.
- Bronze source data is immutable.
- Report only work actually performed and distinguish confirmed source facts from hypotheses.


## RAG — exact title and redirect resolution pass 001

- Added `research/rag/build_alias_index.py` and extended `research/rag/search.py` with exact title lookup (`--title`) and direct captured Wikitext redirect resolution.
- Local build against the pinned archive: 3,579 title-key rows, 3,575 distinct normalized titles; 83 redirects resolved uniquely, 101 unresolved, one ambiguous. Exact title keys normalize underscores/whitespace and case only.
- Smoke-tested Main Page → Second Renaissance Wikia (page 84 → page 2), File:180px-Gerald Ford.jpg → File:Gerald Ford.jpg (page 288 → page 285), exact page title Third Chinese Civil War → page 1408, and an unknown title (abstains). Non-main namespace title results carry an explicit context warning.
- Redirect targets are candidate navigation mappings, not merged entities. Unresolved/ambiguous redirects retain source identity; no fuzzy aliases or redirect-chain traversal is performed.
- The base FTS5 index remains locally generated; the alias table is populated by running `build_alias_index.py` after `build_index.py`. No binary DB committed.


## RAG — date-bearing contrast retrieval pass 001

- Extended `research/rag/search.py` with lexical `--contrast` retrieval. It diversifies candidate passages across page IDs, adds further date-bearing passages, and returns heuristic date signals plus `contradiction_candidates` for review.
- Candidate status is deliberately non-adjudicative. Multiple year ranges in one passage and differing dates across chunks are surfaced for source review; they are not automatically declared contradictions. The retrieval warning explicitly states that the feature does not determine semantic incompatibility or source correctness.
- Added `research/rag/test_search.py`; four local regression checks passed against the uploaded version-002 SQLite index: exact title/page identity; the Second Chinese Civil War lead's 2027–2048 and 2105–2111 ranges; main-namespace default; explicit community-context opt-in.
- Known example: page 1413, `Second Chinese Civil War`, contains infobox date 2027–2048 and a combatant block marked 2105–2111. The contrast query surfaces this same-passage multi-range candidate. The Third Chinese Civil War page 1408 is also returned for cross-page comparison.
- Limitations: this is lexical candidate retrieval with heuristic date extraction, not a semantic claim parser or contradiction adjudicator. The 20-question benchmark still lacks fully reviewed evidence keys; no recall/precision score or reliability percentage is claimed.
- Changed files: `research/rag/search.py`, `research/rag/test_search.py`, and this RAG documentation. No Bronze/Silver source data, canon, or binary database changed. No merge, PR, or branch promotion.


## AI session swap memory

- `.ai/swap.md` is the compact, mutable, cross-window handoff snapshot. It records active work, verified branch/HEAD, durable working decisions, blockers, and immediate next steps. It is not a source of canon, detailed findings, or chronological history.
- `research/continuity/DOCUMENTATION-GOVERNANCE.md` section 12 now defines the memory boundaries, read/update cadence, size/freshness hygiene, authority/conflict order, security rules, and handoff contract.
- `agents.md` requires new sessions to verify Git state and read the swap first, then follow the existing documentation governance and source hierarchy.
- Initial swap established on `audit/continuity-research` at 2026-11-20. It identifies source-aware infobox claim extraction and reviewed benchmark evidence as the next RAG work.
- The swap is deliberately concise and replaceable; durable decisions must be promoted to permanent docs/ADRs and completed milestones to the append-only session log.


## RAG — source-aware infobox claims and conservative comparison pass 001

- Added a derived JSONL extractor that retains page ID/title, namespace, revision, archive snapshot hash, source path/hash, exact infobox template and invocation locator, parameter name/index, raw value, value character offsets, linked wikilink targets/display text/offsets, and explicit provenance.
- Added a JSON Schema contract and a separate comparison CLI. Candidate comparisons require the same captured page subject, exact infobox invocation, and exact normalized parameter name. This avoids treating different date-bearing fields (for example, an event `date` field versus a date string inside `combatant1`) as equivalent claims.
- Different page subjects are not compared absent an explicit entity-equivalence mapping. Different infobox invocations are not assumed to share event scope. Duplicate values in the same narrow scope are surfaced as candidates requiring source review; no claim is adjudicated.
- Parser design uses brace-stack-aware Wikitext template scanning to handle nested templates and triple-brace parameters. A local parser-equivalent probe against the pinned archive identified 143 infobox invocations and 4,381 parameter candidates across 507 main-namespace pages. This is not a committed-CLI execution or a formal test result.
- Runtime verification of the committed extractor/evaluator/tests is pending. The two repeated-field candidate groups from the probe require inspection. The 20-question evaluation seed remains unkeyed/unscored.
- No Bronze/Silver source data, manifests, canon pages, or generated binary index were changed.
