# SR-Doc research workspace

**Last reconciled:** 2026-11-20  
**Working branch:** `audit/continuity-research`

This directory contains source-grounded audit ledgers, tranche evidence, dependency analysis, and continuity investigations. It does not alter or replace Bronze captures, Silver transformations, or Gold proposals. Bronze source files and manifests remain immutable.

## Start here

1. **[Master research register](continuity/MASTER-RESEARCH-REGISTER.md)** — canonical status, evidence hierarchy, reconciled counts, findings, full note inventory, and next work.
2. **[Agent operating guide](../agents.md)** — concise instructions for future sessions.
3. **[Session log](session-log.md)** — append-only chronology. Earlier entries are historical and may contain checkpoint counts superseded by later work.
4. Detailed evidence is retained in the tranche and thematic notes listed below.

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
- `continuity/MASTER-RESEARCH-REGISTER.md` — canonical synthesis and complete note inventory.
- `continuity/agents-md-history-2026-11-20.md` — verbatim preservation of the former long `agents.md`; archival only, not current guidance.

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
