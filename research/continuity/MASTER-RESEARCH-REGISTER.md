# SR-Doc research — master register and audit status

**Last reconciled:** 2026-11-25  
**Working branch:** `experiment/corrected-realism`  
**Purpose:** Canonical navigation, status, definitions, findings, and handoff for the research notes. This register supersedes stale progress summaries in older append-only notes, but does not replace their detailed evidence.

## Non-canon editorial experiment — realism-first retcon
- **Geopolitical forecast integration:** [Geopolitical forecast research and multi-factor integration, 2024–2040](geopolitical-forecast-integration-001.md) synthesizes George Friedman, GPF, and Stratfor/RANE primary materials; distinguishes personal and institutional attribution; records public/paywalled access and RSS/API findings; and supplies a multi-domain causal framework. Climate is explicitly one driver among many. Forecasts are scenario inputs, not canon facts.

- **Binding maintainer decision (2026-11-25):** realism-first retcon; no departure from authentic real-world scientific, technological, demographic, economic, institutional, military, or geopolitical plausibility through 2040-12-31. The first deliberate alternate-history divergence may begin in 2041 or later.
- **Current editorial authority:** [Realism-first continuity baseline and replacement timeline, 2024–2040](realism-first-timeline-2024-2040.md). This document defines the realism envelope, observed-versus-scenario boundary, revised 2024–2040 chronology, retcon matrix, page dependency checklist, and validation gates.
- **Source audit:** [corrected-realism-audit-001.md](corrected-realism-audit-001.md) verified 13 relevant Bronze source page hashes against the pinned archive manifest and documented source-level conflicts. It remains the evidence record for the initial audit.
- **Superseded draft:** [corrected-realism-proposal-001.md](corrected-realism-proposal-001.md) is retained for source inventory/history only. Its 2024–2034 proposed chronology and unresolved editorial questions are superseded by the 2024–2040 realism-first baseline.
- **Required retcons:** remove the pre-2041 global Flood/sea-level catastrophe and mass-death/displacement totals; global Great Famine and extraordinary mortality; Second Chinese Civil War/Three Gorges Dam trigger; multi-state White Tide civil war; Russian dissolution/nuclear seizure; Turkish Arabia occupation/Arctic–Bosporus pipeline; 2023/2026 crewed Mars landings and 2029–2033 terraforming; and unsupported 400m U.S. population / 90m displacement / wholesale housing seizure claims.
- **Dependency control:** no canon-edit phase until all pages listed in the replacement timeline's dependency checklist are reconciled, including timeline page 88, Flood 637, Great Famine 2027, Market Crash 642, Revolutions 820, White Tide 3593, AOC 3592, China 1413/1408, Russia 1683, Turkey 1423, Mars 638/1139, and all downstream linked/mentioned pages.
- **Completed dependency discovery pass 001:** [method and findings](dependency-discovery-001.md) with [243-row claim ledger](claim-ledger-001.csv). The pinned archive contained 3,579 Bronze pages; every raw Wikitext SHA-256 matched the manifest. Exact-phrase scanning found 107 unique Main-namespace pages; Silver relations yielded 148 direct wikilink edges from 73 unique source pages (145 Main, two User, one Template). The ledger records 127 grouped direct-link observations, 66 text-only mentions, 31 numeric claims, four timeline fields, three redirects, six template/infobox-use records, and six category-membership records. These row counts, graph edges and unique pages are different measures.
- **Flood claim reconciliation pass 001:** [page-level findings](flood-claim-reconciliation-001.md) and [58-page source ledger](flood-claim-reconciliation-001.csv). The Main-namespace Flood phrase-hit set contains 58 pages and 35 canonical parsed-link edges across 29 of them. The review classifies two primary chronology/source pages, 37 direct causal/structural dependencies, 11 indirect/downstream dependencies, four cultural/summary references, three incidental/poll references, and one regional-climate exception. This is a focused context-window review; semantic review beyond the exact phrase-hit set remains open.
- **Structural findings:** three redirects lead to Mars colonization, Russian dissolution (target article absent), and Great Reset. `Category:The Flood` has three memberships (one lore page, two File pages). Six source pages invoke 21 templates/modules. No explicit `{{:Page}}` transclusion of a scoped event/entity was found. Context-only exact-phrase hits: eight Talk, twelve Thread, three User, three File, and one Template page.
- **RAG limitation for this pass:** Silver page/link/year metadata was present and scanned, but the built SQLite FTS index, chunk JSONL and separately described RAG-index ZIP were absent from the supplied archive and branch tree. No RAG CLI query or build was run.
- **Current discovery disposition:** this is dependency mapping, not source adjudication or canon editing. Preserve the Great Famine 2032/2033, Flood 300m-deaths versus 300m-without-basic-needs, Mars 2023/2026 first-crew, and Russia 2138/2139 discrepancies. Page 1423 `Turkey` is an inferred review candidate, not an exact phrase hit. Next step is claim-by-claim reconciliation and a page-by-page proposal; canon edits still require separate approval.
- **Authority limit:** this is an approved editorial direction, not permission to edit accepted canon, Bronze/Silver data, manifests, or RAG implementation. No PR, merge, or branch promotion is authorized.

## Research assistant / RAG workstream

- Answer contract: `research/continuity/RESEARCH-ASSISTANT-PROTOCOL.md` — normative retrieval, evidence, citation, contradiction, and abstention rules for lore answers.
- Implementation plan: `research/rag/README.md` — staged architecture, corpus contract, retrieval design, evaluation criteria, risks, and next coding task.
- Evidence transport: `research/rag/evidence-packet.schema.json` — JSON Schema 1.0 for portable retrieved evidence packets.
- Evaluation baseline: `research/rag/evaluation-set-001.md` — maintainer-approved 20-case set. All ten registered source identities, 51 locator/content ranges, and seven title/map-boundary checks passed. Retrieval pass 001 found 19/19 expected-page sets within top five unique page candidates (27 expected page-ID instances); first-stage locator coverage was 47/55 and rose to 55/55 after full-page expansion of already retrieved pages. Manual answer-generation pass 001 now records 20/20 answer-key-compliant outputs, 20/20 cited cases, 4/4 contradiction disclosures, and 3/3 required abstentions. This is not a runtime or independent-scoring result. See `research/rag/evaluation-locator-validation-001.json`, `research/rag/retrieval-benchmark-pass-001.json`, and `research/rag/answer-generation-pass-001.md`.
- **Current status:** protocol/schema/evaluation seed, read-only archive validator, section-aware chunker, SQLite FTS5 index builder, exact-title/redirect index builder, evidence-packet search CLI, source-aware infobox claim extractor, claim schema, and conservative same-scope comparison CLI are committed. Archive SHA-256: `d1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8`. Corpus: 3,579 page metadata rows, 7,598 unique chunks, 7,598 FTS rows; 3,092 pages have text chunks. 487 captured records have no non-whitespace text, including three empty main-namespace pages. Default lexical search is main namespace only; context namespaces require explicit inclusion. Exact title/redirect lookup is opt-in via `--title` and preserves redirect provenance. Retrieval benchmark pass 001 is exploratory (source-equivalent reconstruction, not byte-identical committed scripts); manual answer-generation pass 001 is complete from retrieved page IDs plus full-page expansion, not from CLI-generated evidence packets. No end-to-end answer-generation or independent citation score is claimed.
- **Infobox claim runtime verification (2026-11-21):** committed extractor executed against the pinned archive: 507 main-namespace pages, 143 infobox invocations, 4,381 claims, all IDs unique; 4,381/4,381 records passed JSON Schema Draft 2020-12 and exact offset/provenance checks. Repeat extraction was byte-identical. Evaluator retained two unscoped repeated-parameter groups as unresolved and produced zero scoped candidate conflicts. See `research/rag/infobox-claim-validation-001.json`.

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
- `research/rag/evaluation-set-001.md` — 20-question maintainer-approved baseline answer key with page IDs, character locators, answer criteria, pitfalls, and abstention expectations; retrieval pass 001 recorded, answer-generation/citation scoring pending.
- `research/rag/evaluation-locator-validation-001.json` — independent pinned-archive check of all ten source identities, 51 cited locator/content ranges, and seven exact-title/map-boundary conditions; Q09/Q16/Q17 locator corrections recorded.
- `research/rag/retrieval-benchmark-pass-001.json` — initial approved 20-case retrieval benchmark, per-case page discovery, first-stage/full-page locator coverage, entity/redirect/abstention results, precision caveats, and execution-source limitations.
- `research/rag/answer-generation-pass-001.md` — 20 source-grounded manual answer outputs and case-by-case scoring for answer-key compliance, citation/provenance, contradiction disclosure, and abstention; explicitly not a runtime or independent-scoring evaluation.
- `research/rag/extract_infobox_claims.py` — read-only, provenance-preserving infobox parameter claim extractor.
- `research/rag/infobox-claim.schema.json` — machine-readable claim record contract.
- `research/rag/evaluate_infobox_claims.py` — comparison requiring same page subject, explicit reviewed `event_scope_id`, template family, and exact normalized parameter name; unscoped repeated parameters remain unresolved.
- `research/rag/test_infobox_claims.py` — five parser/comparison regression tests; passed in GitHub Actions on 2026-11-21 under Python 3.11.18.
- `research/rag/infobox-claim-validation-001.json` — committed extractor/evaluator execution report: 4,381 claims from the pinned ZIP, all schema/offset/provenance checks passed, repeat output byte-identical; two unscoped repeated fields remain unresolved.
- `research/rag/infobox-claims-pass-001.md` — detailed method, development-probe coverage, unresolved repeated-parameter examples, and limitations.


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

## Narrative audit — validation tranche 001

**Status:** First independent handoff validation and targeted narrative review completed; full narrative audit remains in progress.

- Snapshot: branch experiment/corrected-realism, HEAD fdec89ff1221a36fa360630b0d7607b7c7d2f95d.
- New artifacts: research/narrative-audit/MASTER-NARRATIVE-AUDIT.md, validation-tranche-001.md, POST-2041-LINK-DISCOVERY-001.md, and page-review-001.csv.
- Twenty-eight Bronze pages reviewed at varying depth (19 full, 9 partial); all 28 raw hashes matched the Bronze manifest.
- Fourteen exact-year pages were confirmed absent from claim-ledger-001.csv. Page 1998 is a separate downstream candidate; five additional recursive pages were reviewed even though they do not meet the exact-year threshold.
- Exact-year discovery: 116 non-redirect Main pages mention 2024–2040; 262 mention 2041 or later; 82 mention both. These are discovery counts, not semantic completion metrics.
- Key issues include the 2024 Mexican presidential succession, 2024 gastric-brooding frog de-extinction, Little Cold War NATO membership claim, Trump-Russia/Mueller claim, Mars settlement/terraforming chronology, Caribbean annexation dependencies, US party-system continuity, hypersonic/orbital-weapons claims, and the 2029 Russia succession sequence.
- Claude's Russia finding was narrowed: the dates may describe successive events rather than three incompatible accounts. Korean famine chronology may be anticipatory rather than strictly cause-after-effect.
- Archive SHA-256 was independently recomputed from SR-Doc-Audit.zip. Five current documents were corrected; historical session-log entries remain untouched under append-only policy.

## Next recommended work

1. **Post-2041 survival map:** classify the 262 discrete-year pages in bounded batches as independent, latent dependency, direct dependency, or unresolved. Start with Flood, Mars, Great Famine, Russia/Eurasia, and US territorial expansion clusters. Link edges are discovery evidence only.
2. **Observed-baseline sweep:** review 2022–2026 claims across pages 97, 961, 1317, 1445, 318, 1234, and 1366, then expand recursively.
3. **Russia/Eurasia regional chain:** complete pages 97, 1683, 1729, 1438, 1998, 961, and related successor-state, Turkish, Polish, and Japanese pages.
4. **US political continuity:** reconcile pages 2136, 1262, 1266, and 1796 with the party-system and election pages.
5. **Return to the Great Famine / Market Crash / Revolutions / Great Reset cluster** after the current cross-domain dependencies have been mapped.

The earlier Chinese political-history workstream remains important but is deferred behind the active narrative dependency and observed-baseline audit.

## Safety rails

- Current editorial working branch: `experiment/corrected-realism`; the base `audit/continuity-research` remains the read-only research baseline for this offshoot.
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
- Limitations: this remains lexical candidate retrieval with heuristic date extraction, not a semantic claim parser or contradiction adjudicator. The maintainer-approved 20-question benchmark has retrieval pass 001 results in `research/rag/retrieval-benchmark-pass-001.json`; generated-answer correctness, citation precision, claim support, and semantic contradiction precision remain unscored. No overall reliability percentage is claimed.
- Changed files: `research/rag/search.py`, `research/rag/test_search.py`, and this RAG documentation. No Bronze/Silver source data, canon, or binary database changed. No merge, PR, or branch promotion.


## AI session swap memory

- `.ai/swap.md` is the compact, mutable, cross-window handoff snapshot. It records active work, verified branch/HEAD, durable working decisions, blockers, and immediate next steps. It is not a source of canon, detailed findings, or chronological history.
- `research/continuity/DOCUMENTATION-GOVERNANCE.md` section 12 now defines the memory boundaries, read/update cadence, size/freshness hygiene, authority/conflict order, security rules, and handoff contract.
- `agents.md` requires new sessions to verify Git state and read the swap first, then follow the existing documentation governance and source hierarchy.
- Initial swap established on `audit/continuity-research` at 2026-11-20. It identifies source-aware infobox claim extraction and reviewed benchmark evidence as the next RAG work.
- The swap is deliberately concise and replaceable; durable decisions must be promoted to permanent docs/ADRs and completed milestones to the append-only session log.


## RAG — source-aware infobox claims and conservative comparison pass 001

- Added a derived JSONL extractor that retains page ID/title, namespace, revision, archive snapshot hash, source path/hash, exact infobox template and invocation locator, parameter name/index, raw value, value character offsets, linked wikilink targets/display text/offsets, and explicit provenance.
- Added a JSON Schema contract and a separate comparison CLI. Candidate comparisons require the same captured page subject, an explicit reviewed `event_scope_id`, template family, and exact normalized parameter name. The extractor does not infer event scope. Repeated parameters without event-scope annotation are retained as unresolved comparison groups, not classified as conflicts. Different date-bearing fields (for example, an event `date` field versus a date string inside `combatant1`) are not compared.
- Different page subjects are not compared absent an explicit entity-equivalence mapping. Different infobox invocations are not assumed to share event scope. Only manually reviewed scope annotations permit candidate comparison; no claim is adjudicated.
- Parser design uses brace-stack-aware Wikitext template scanning to handle nested templates and triple-brace parameters. A local parser-equivalent probe against the pinned archive identified 143 infobox invocations and 4,381 parameter candidates across 507 main-namespace pages. This is not a committed-CLI execution or a formal test result.
- Regression runtime verification is now complete for the five committed parser/comparison tests (GitHub Actions run 44925739208, success); the existing continuity validator, compileall step, and two pytest tests also passed. The committed extractor/evaluator CLI was subsequently run against the pinned archive; all 4,381 emitted claims passed JSON Schema and offset/provenance validation, with deterministic repeat output. See `research/rag/infobox-claim-validation-001.json`. Source-context review of the two repeated-parameter groups is now documented in `research/rag/infobox-claims-pass-001.md`: page 636's `office` values sit in separate nominee blocks, while page 1343's two `order` values cannot be assigned confidently from field order. Both remain unresolved; no event-scope annotation is justified. The 20-question evaluation set has exact page IDs and character locators, was approved by the maintainer on 2026-11-21, and has retrieval pass 001 results. Answer-generation/citation scoring remains pending.
- No Bronze/Silver source data, manifests, canon pages, or generated binary index were changed.


## RAG — benchmark source verification pass 001

- Independently re-read the ten Bronze page records used by `research/rag/evaluation-set-001.md` from the pinned archive and recomputed each source SHA-256 against the page manifest. All ten page IDs, exact titles, revision IDs, paths, and hashes matched.
- Cross-checked the critical chronology/infobox claims used by the benchmark, including the distinct Second Chinese Civil War `date` and `combatant1` fields, Third Chinese Civil War phase labels, the UFC/FRoC 2108 transition, repeated 20th-century history fields, Joseph Loveridge's Chairman-role values, and the Association's 2140 establishment date.
- Confirmed the referenced historical orthographic-projection SVG is not in the captured 900-record asset manifest; confirmed the exact-title absence cases for `UFC` and `Association of East Asia`, with the hyphenated page 1927 retained as a near-match only.
- At the time of this source-verification pass, the work was a targeted archive cross-check, not a fresh full-corpus validation, maintainer sign-off, exhaustive locator audit, committed CLI/test execution, or scored benchmark. Later milestones supersede the approval/scoring status: the maintainer approved the baseline and retrieval pass 001 is recorded in `research/rag/retrieval-benchmark-pass-001.json`. This remains an exploratory retrieval reproduction; answer-generation/citation scoring is still outstanding.


## Narrative audit — validation tranche 002

**Current status:** The first 14-page exact-year gap was a threshold subset, not the full ledger gap. The repeatable standalone-year scan now identifies **43 non-redirect Main pages** with at least one discrete 2024–2040 year that are absent from `claim-ledger-001.csv`. The complete provenance/disposition inventory is `research/narrative-audit/claim-ledger-gap-002.csv`; the independent source and baseline review is `research/narrative-audit/validation-tranche-002.md`.

- Method: raw Bronze Wikitext scan with standalone four-digit year tokens 2024–2040; decade labels such as 2030s are excluded.
- Coverage: 116 pages contain at least one such year; 73 are represented in claim-ledger-001; 43 are not. The gap contains 17 one-mention pages, 12 two-mention pages, and 14 pages with three or more mentions. The prior 14-page count is the last category, not the complete gap.
- Provenance: 43/43 gap-page raw SHA-256 values match the pinned Bronze manifest. The additional 29 pages received targeted year-context review, not full semantic review.
- Independent corrections: Claude's direct US presidential chronology contradiction is confirmed; the 2025–2026 observed baseline shows US-origin NATO stress rather than Western European withdrawals; the frog project's "put on ice" status is supported by 2025 reporting; the GAO Navy CPS citation is not HACM evidence, and the first HACM flight-test release occurred in October 2026.
- New dependencies: pages 1405/1426 (crewed Jupiter/Saturn), 1685/2127 (space elevators), 1715/3484 (Korean reunification), 1739/1431/2127/3662 (Mars settlement/mission), 3099 (ISS LEO-to-GEO transfer), 3494 (Serbia/Bosnia), and 3651 (Hong Kong independence) require explicit disposition.
- Page 1998 Central Eurasian Union was read; no direct dependency on the 2029 Russian dissolution is stated. Do not infer one from the name.
- The 2041+ page universe remains 262 discovery candidates; zero pages have been formally classified in the full page-level survival map. No regions are complete.

The tranche also records a bounded 2025–2026 observed-baseline update: NATO remains at 32 members; Iran-war disagreements, US force-posture reductions, and the Greenland dispute are real alliance stresses; the November Greenland agreement preserves Danish sovereignty while expanding US military access. The full sources, qualifications, and limitations are in validation-tranche-002.md.

No canon, Bronze/Silver source data, manifests, or RAG implementation changed. No tests, builds, RAG CLI runs, PRs, merges, or branch promotion occurred.


## Chronology proposal register 001 — conversation-origin, non-canon

- [Chronology proposal register 001](chronology-proposal-register-001.md) records 16 maintainer-supplied chronology proposals and their reported relationships to existing Bronze lore.
- **Every entry is PROPOSAL, conversation-origin, not canon, not approved.** The register preserves conflicts and competing values; it does not edit or supersede the realism-first timeline.
- Reported conflicts include page 214's six presidential succession slots, page 1106's 2045 Earth Working Group origin, page 88's Balkan Crisis/Japanese Resurgence/Meridian Base/China/Prometheus/Augment Rights entries, page 107's WWIII and armistice chronology, and page 1438's Eurasian Coalition.
- Page relationships are registered from the maintainer's 2026-11-27 instruction and reported Claude findings; the register explicitly marks them as not independently re-fetched/re-hashed in this work unit.
- Open maintainer decisions include real-person and pre-2041 named-president policy, replacement/refinement of Japanese Far East lore, Kura-Araxes/Neum mapping, Earth Working Group re-founding, armistice-stage chronology, Prometheus mechanism, and Augment Rights dates.
