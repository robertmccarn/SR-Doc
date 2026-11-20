# SR-Doc research workspace

This folder contains source-grounded audit ledgers and notes. It does not alter or replace Bronze captures, Silver transformations, or Gold proposals. The authoritative source for page review is the original Bronze Wikitext plus its manifest SHA-256.

## Current audit status — 2026-11-20

- Page corpus: 3,579 manifest records; all 3,579 raw Wikitext paths are present in the supplied ZIP archive.
- **Pages directly read and SHA-256 verified: 3,579 / 3,579 (100.00%).**
- Ledger: **3,579 read; 0 unverified_prior_claim; 0 not_started.**
- Main namespace: **507 / 507 read (100.00%).**
- Latest completed tranche: manifest entries **3301–3579**, all namespaces; 279/279 SHA-256 matches; 270 new unique verified reads.
- Latest detailed notes: [manifest-3301-3579.md](page-notes/manifest-3301-3579.md).
- All 3,579 page records are now complete. Next phase: media manifest reconciliation and binary asset inspection.
- Media manifest: 900 records. The ZIP contains 899 physical files under `bronze/assets`; exact manifest-to-physical-filename reconciliation remains incomplete.
- Binary media visual inspection: **0 / 900**. File-description Wikitext review and checksum verification are not visual inspection.

## Corpus namespace counts

| Namespace | Records |
|---|---:|
| Main | 507 |
| Talk | 625 |
| User | 104 |
| File | 906 |
| MediaWiki | 3 |
| Template | 744 |
| Template talk | 1 |
| Category | 32 |
| Blog | 1 |
| Module | 102 |
| Message Wall | 121 |
| Thread | 426 |
| Board | 5 |
| Board Thread | 2 |
| **Total** | **3,579** |

The main-namespace alphabetical review is a useful sub-scope, not a substitute for the all-namespace manifest audit.

## Files

- `page-ledger.csv` — one row per captured Wikitext page; source identifiers, SHA-256, review status, basis, and notes path.
- `media-ledger.csv` — one row per media manifest record; source URL, SHA-1, size, manifest status, and visual-inspection status.
- `session-log.md` — append-only record of work actually completed.
- `page-notes/main-181-210.md` and `page-notes/main-211-240.md` — main-namespace focused reviews.
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

## Status definitions

- `read` — exact Bronze Wikitext file was opened/read and its SHA-256 matched the manifest.
- `unverified_prior_claim` — appeared inside an earlier conversational completion claim but has not yet been reopened and verified.
- `not_started` — no direct source review is recorded.
- `unavailable_missing_source_asset` — manifest asset record is failed and has no visual asset available to inspect.

A redirect is a reviewed source page. Its target is recorded separately; a target only counts as read if its own source file is independently opened. Empty Wikitext files are also valid reviewed source records, with their empty state recorded.

## Workflow rules

1. Preserve exact manifest order and review exactly 300 page records per tranche.
2. Open the original Bronze Wikitext source, not a transformed or summarized substitute.
3. Recompute SHA-256 and compare it with the manifest for every source file.
4. Record namespace distribution, empty pages, redirects, and meaningful content by source type.
5. Treat Talk and Thread records as editorial context, not automatically as canon.
6. Preserve contradictory dates, spellings, figures, and claims; do not silently correct source content.
7. Keep page-description review, checksum verification, and binary visual inspection as separate statuses.
8. Update the ledger, tranche notes, session log, this README, and `agents.md` after each completed tranche.


## Binary media audit

The 900-record asset manifest is being audited separately from page Wikitext. Each batch maps records to physical archive paths, recomputes SHA-1 and byte size, and receives contact-sheet visual triage. Visual review does not establish source authenticity or semantic correctness.

- Tranche 1 (manifest 1–300): 300/300 physically mapped and visually reviewed; 243 exact SHA-1/size matches, 57 mismatches, zero missing files and zero decode/parse failures.
- Detailed notes: `media-notes/manifest-001-300.md`.
- Media visual review progress: 300/900 (33.33%). Physical assets mapped: 300/899. The failed manifest record for page ID 3525 is still unresolved.
- Next: manifest entries 301–600, then 601–900. Preserve Bronze files and manifest values; investigate mismatches rather than silently replacing sources.


### Tranche 2 — media manifest 301–600
- 300/300 physical files mapped and visually reviewed; 288 exact SHA-1/size matches, 12 discrepancies, zero missing files and zero decode/parse failures.
- Detailed notes and mismatch register: `media-notes/manifest-301-600.md`.
- Cumulative visual review: 600/900 (66.67%); 600/899 physical assets mapped; 531 exact matches and 69 discrepancies. The failed asset at page ID 3525 remains unresolved.
- Next: manifest entries 601–900.


## Media audit — complete

All 900 media-manifest records have been reconciled against archive paths. There are 899 physical assets; entry 815 (page ID 3525, `File:K8ch1z55ucnz.png`) is the one failed/missing asset. All 899 available files were decoded/parsed and visually reviewed at contact-sheet thumbnail scale: 728 exact SHA-1/size matches, 171 mismatches, zero decode failures. The missing asset is not visually reviewable. See `research/media-ledger.csv` and the three tranche notes in `research/media-notes/`. This does not verify visual authenticity or semantic/canonical correctness. Next phase is cross-referencing media against Wikitext and synthesizing continuity findings.


## Cross-corpus reconciliation — underway

Initial asset-to-page reconciliation for media manifest entries 1–300 is documented in `research/media-notes/crossref-001-300.md`. Exact extracted page-image references are distinct from raw filename mentions and template aliases. Initial tranche: 268/300 exact extracted references; 32 without, of which six have raw/template filename mentions and 26 have no discovered literal mention. A corpus-wide first-pass title comparison found 792 exact asset matches, 108 assets without extracted references, and 141 extracted image titles without exact manifest counterparts. These are leads, not confirmed orphans/missing files. See the note for limitations and next steps.


### Cross-corpus reconciliation — tranche 301–600

- Manifest entries 301–600: 284/300 exact extracted page-image references; 16 absent from extracted metadata, of which one has a raw/template mention and 15 have no discovered literal filename mention.
- The 284 exact matches account for 525 asset-to-page references. Combined with tranche 1, entries 1–600 have 552 exact matches, seven raw/template-only mentions, and 41 with no discovered reference.
- Detailed note: `media-notes/crossref-301-600.md`. A raw/template mention is not proof of rendered use; absence from the extracted index is not proof of an orphan.
- Next: manifest entries 601–900.


### Cross-corpus reconciliation — tranche 601–900

- Manifest entries 601–900: 240/300 exact extracted page-image references; 60 absent from extracted metadata, of which four have raw filename mentions and 56 have no discovered literal mention.
- The 240 exact matches account for 295 asset-to-page references. Across all 900 records: 792 exact references, 11 raw/template/thread-only mentions, 97 with no discovered reference, and 1,696 exact-reference edges.
- Detailed note: `media-notes/crossref-601-900.md`. Raw mentions and absent references are not proof of rendered use or orphan status.
- Initial media-to-page reference pass is complete. Next: aliases, redirects, template/module expansion, and context validation.


## Dependency reconciliation — pass 1

- Reconciled all 906 File-namespace page records against the 900 media-manifest records. All 900 asset page IDs resolve to File pages; six File pages are outside the media manifest, including three redirects (Gerald Ford, William McKinley, Eagle 7 Booster) and three other pages.
- Identified 141 distinct extracted image titles without exact media-manifest counterparts. 128 are referenced only from Template namespace, five only from Module, three only from main namespace, two from both Template and Module, and the remaining three are User, Thread, and File namespace cases. These are mostly generic template/module dependencies, not 141 confirmed missing article images.
- Independent raw scan found 441 manifest titles in explicit `[[File:...]]`/`[[Image:...]]` links (749 occurrences). None of the 108 assets without exact extracted references had an exact normalized explicit File/Image wikilink in the captured raw corpus.
- Re-examined the 11 literal-only cases; most are obsolete flag aliases, prose/Thread links, or near-name matches. `Xanthe Flag.png` is a direct country-data flag-alias lead; rendered use remains unverified.
- Detailed method, all six extra File pages, namespace distribution, literal-only contexts, and limitations: `media-notes/dependency-reconciliation-pass-001.md`.
- Next: resolve template alias chains and prioritize article-level dependencies; do not classify no-reference assets as orphans without further evidence.


### Targeted unmatched dependency review — China, Al-Hasa, main page

- Inspected Al-Hasa, Federal Republic of China, United Federation of China, and Second Renaissance Wikia raw Wikitext.
- `Blank.png` is listed in Al-Hasa extracted image metadata, but the article's `image_map` field is empty; likely placeholder/parser artifact, not a demonstrated map dependency.
- `Republic of China (orthographic projection historical).svg` is explicitly assigned as `image_map` on both Chinese state pages. It is a genuine intended dependency, but its binary and File page are absent from the supplied archive. Its visual content and territorial accuracy remain unverified.
- `Slider` is a bare token within `<gallery type="slider">`, not a normal File link; do not count it as a missing image without renderer evidence.
- Detailed source excerpts, assessments, and limitations: `media-notes/targeted-unmatched-dependencies-001.md`.
