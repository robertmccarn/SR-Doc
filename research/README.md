# SR-Doc research workspace

This folder contains source-grounded audit ledgers and notes. It does not alter or replace Bronze captures, Silver transformations, or Gold proposals. The authoritative source for page review is the original Bronze Wikitext plus its manifest SHA-256.

## Current audit status — 2026-11-20

- Page corpus: 3,579 manifest records; all 3,579 raw Wikitext paths are present in the supplied ZIP archive.
- **Pages directly read and SHA-256 verified: 2,416 / 3,579 (67.50%).**
- Ledger: **2,416 read; 36 unverified_prior_claim; 1,127 not_started.**
- Main namespace: **413 / 507 read (81.46%).**
- Latest completed tranche: manifest entries **2101–2400**, all namespaces; 300/300 SHA-256 matches; 290 new unique verified reads.
- Latest detailed notes: [manifest-2101-2400.md](page-notes/manifest-2101-2400.md).
- Next tranche: manifest entries **2401–2700**, preserving original manifest order.
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
