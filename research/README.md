# SR-Doc research workspace

This folder contains audit ledgers and source-grounded notes. It does not change or replace Bronze captures, Silver transformations, or Gold proposals.

## Current baseline (2026-11-19)

- The supplied archive's pages manifest contains 3,579 page records. All 3,579 raw Wikitext paths were present in the ZIP.
- Namespace counts: Main 507; Talk 625; User 104; File 906; MediaWiki 3; Template 744; Template talk 1; Category 32; Blog 1; Module 102; Message Wall 121; Thread 426; Board 5; Board Thread 2.
- The main-namespace review order is case-insensitive alphabetical title order. This is a sub-scope within the all-namespace audit, not a replacement for it.
- Main-namespace positions 181–210 (Hivvir through Joaquín Andrade) have now been directly read. The target Vactrain (ID 2693) was also opened because Hyperloop redirects to it.
- The earlier claim of 180/507 main-namespace pages reviewed remains unverified. It is not counted as verified progress.
- The page ledger currently has 1,248 / 3,579 unique pages marked read (34.87%), 117 rows flagged as unverified prior claims, and 2,214 not started. Main namespace progress is 203 / 507 (40.04%). Main namespace progress is 102 / 507 (20.12%). The latest completed batches directly reviewed manifest entries 1–300, 301–600, 601–900, and 901–1200 across all namespaces.
- The asset manifest has 900 records: 728 existing_verified, 171 downloaded_checksum_mismatch, and one failed record. The ZIP contains 899 physical files under bronze/assets (682 PNG, 160 JPG, 13 JPEG, 34 SVG, 6 GIF, 2 ICO, 1 WebP, and 1 file without an extension). One failed manifest record is consistent with the 899 non-failed records, but exact manifest-to-filename mapping still needs to be built.
- No asset has been marked visually inspected in the reconstructed ledger. Checksum status and visual inspection are separate. Current visual-inspection progress: 0 / 900.

## Files

- page-ledger.csv — one row per captured Wikitext page; raw manifest identifiers and review status.
- media-ledger.csv — one row per media manifest record; source URL, SHA-1, size, manifest status, and visual-inspection status.
- page-notes/main-181-210.md — source-grounded main-namespace tranche notes.
- page-notes/main-211-240.md — source-grounded main-namespace tranche notes.
- page-notes/manifest-001-300.md — all-namespace manifest tranche notes and cross-source leads.
- page-notes/manifest-301-600.md — all-namespace manifest tranche notes and cross-source leads.
- page-notes/manifest-601-900.md — all-namespace manifest tranche notes and cross-source leads.
- page-notes/manifest-901-1200.md — all-namespace manifest tranche notes and cross-source leads.
- session-log.md — append-only record of work actually completed.

## Status definitions

- read — exact Bronze Wikitext file was opened and read.
- unverified_prior_claim — appeared inside a prior conversational completion claim but has not been reopened and verified.
- not_started — no direct review recorded.
- unavailable_missing_source_asset — manifest record is failed and has no visual asset to inspect at this time.

A page redirect is still a reviewed source page. Its target is recorded separately; a target only counts as read if its own source file was opened.
