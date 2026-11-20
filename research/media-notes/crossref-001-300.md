# Cross-corpus media reconciliation — tranche 1 (media manifest 1–300)

## Scope and method

Compared media manifest records 1–300 against the complete 3,579-record page manifest and its extracted `images` references. Then searched the raw Bronze Wikitext corpus for filename literals (both spaces and underscore forms) for every asset not found in the extracted image-reference index. This distinguishes (1) exact extracted page references, (2) literal filename mentions in source/template parameters, and (3) no discovered reference. A filename mention in a template is not proof that a rendered page uses the asset; template expansion is a separate step.

## Results

- Media records examined: 300.
- Exact media-title matches in page `images` metadata: 268/300 (89.3%).
- Assets absent from extracted `images` metadata: 32.
- Of those 32, six have literal filename mentions somewhere in raw Wikitext (including country-data templates or module data); 26 have no exact or underscore-normalized filename mention found in the corpus.
- The 268 exact matches resolve to 90 assets referenced by one page, 39 by two, 25 by three, 73 by four, 17 by five, four by six, nine by seven, one by eight, two by nine, two by ten, one by 15, one by 17, one by 18, one by 20, one by 24, and one by 29 pages. (Counts are asset-to-page reference multiplicities.)
- The global page-manifest index contains 933 distinct image-title references. A first-pass exact-title comparison across the entire corpus finds 792 manifest assets with at least one extracted reference, leaving 108 manifest assets without an exact extracted reference and 141 extracted image titles with no exact-title counterpart in the asset manifest. These are corpus-wide leads; do not label them missing or orphaned until title normalization, aliases, redirects, template data, and failed downloads are reconciled.

## Notable unreferenced/alias cases

- `File:Flag of Taiwan.png` is not the file used in the two relevant raw page sources: those sources name `New_Flag_of_Taiwan.png`. Treat as a distinct, currently unreferenced older asset unless another alias relation is established.
- `File:Vietnam.png` is not the flag named in the Second Vietnam War source, which uses `Flag_of_Vietnam.png`; the filename also appears in portal-module data and the country-data template. Those mentions do not establish use of this specific file.
- `File:Sudan.png`, `File:Chile.png`, and `File:Bolivia.png` appear not as direct page image references but as simplified names whose country-data templates point to underscored flag filenames (`Flag_of_Sudan.png`, `Flag_of_Chile.png`, `Flag_of_Bolivia.png`). Do not assume the simplified files are the rendered flags.
- `File:Xanthe Flag.png` appears as the `flag alias` value in Template:Country data Xanthe. The extracted image-reference index does not expand this template, so template-mediated use needs a renderer/expansion check.
- Other no-reference assets include site/UI resources (wordmark, favicon, location/world graphic), a WWIII map, portraits, political flags, and vehicle imagery. These may be historical uploads, unused assets, or references omitted by the parser; they are not automatically errors.

## Interpretation and limitations

The page manifest's `images` field is an extracted index, not a rendered dependency graph. It does not expand template aliases or prove whether a file is visible in the final page. Conversely, literal filename occurrence can be a template parameter, documentation example, or stale reference. The 26 records with no extracted or literal filename match are candidates for unused/orphaned assets, not confirmed orphans. A complete determination requires template expansion and title/alias normalization, followed by page-level review for consequential assets.

## Next tranche

Continue the same procedure for media manifest entries 301–600. Preserve three separate states: exact extracted reference, raw/template filename mention only, and no discovered reference. Do not change Bronze assets or manifest values.
