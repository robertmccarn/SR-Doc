# SR-Doc

An API-first, provenance-preserving mirror and narrative-continuity workspace for the Second Renaissance Wikia.

## Quick start

```powershell
python -m sr_doc.archive plan
python -m sr_doc.archive sync --media-budget-mib 320
python -m sr_doc.transform build
python -m sr_doc.validate
```

`sync` is resumable. It saves immutable source captures under `bronze/`; the transform command generates reviewable Silver artifacts and continuity data.

## Rendered wiki mirror

The narrative artifacts are not the reader-facing wiki. Capture Fandom's template-expanded article HTML and build the actual local wiki mirror with:

```powershell
python -m sr_doc.wiki render
python -m sr_doc.wiki build
python -m http.server 8080 --directory build/wiki
```

Open `http://localhost:8080`. The rendered capture is resumable and keeps source revision provenance for every page.

## Layout

- `bronze/` — raw API responses, exact current wikitext, asset metadata, downloaded originals, and run manifests.
- `silver/` — deterministic Markdown and JSONL derived only from Bronze.
- `gold/` — reviewed narrative additions and proposal records. Nothing here mutates imported source canon.
- `site/` — generated local navigation and overview inputs for MkDocs.

The source wiki is checked through its public MediaWiki API. This repository retains source URLs, revision IDs, and attribution metadata; review the upstream license before redistributing a mirror.
