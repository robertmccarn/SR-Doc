# SR-Doc research — master register and audit status

**Last reconciled:** 2026-11-20  
**Working branch:** `audit/continuity-research`  
**Purpose:** Canonical navigation, status, definitions, findings, and handoff for the research notes. This register supersedes stale progress summaries in older append-only notes, but does not replace their detailed evidence.

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
