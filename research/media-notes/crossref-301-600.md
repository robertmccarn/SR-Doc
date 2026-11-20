# Cross-corpus media reconciliation — manifest entries 301–600

## Scope and method

Compared media-manifest records 301–600 against the complete 3,579-record page manifest and all captured Bronze Wikitext sources. Used the extracted `images` metadata for exact page-to-file references, then searched raw Wikitext for exact filenames and space/underscore variants when no exact extracted reference existed. This repeats the same method as entries 1–300.

Three statuses are kept separate:
1. **Exact extracted reference** — the page manifest's `images` array contains the exact `File:` title.
2. **Literal/template mention only** — no exact extracted reference, but the filename occurs in raw Wikitext (possibly module/template data).
3. **No discovered reference** — neither exact extracted reference nor literal filename occurrence was found.

The `images` array is an extracted index, not a fully rendered dependency graph. It may include template documentation or transcluded dependencies and does not prove what a reader sees after rendering. Raw filename mentions may be aliases, data values, stale references, or examples.

## Results

- Media records examined: 300.
- Exact extracted page-image references: **284/300 (94.7%)**.
- Assets absent from extracted `images` metadata: 16.
- Of those 16, **one** has a raw/template filename mention; **15** have no exact or space/underscore-normalized filename mention found in the captured Wikitext corpus.
- The 284 exact matches account for 525 asset-to-page references.
- Reference multiplicity: 145 assets referenced by one page; 93 by two; 23 by three; 14 by four; two by five; one by six; three by seven; one by eight; one by ten; and one by fourteen pages.

## Assets without exact extracted references

| Manifest index | Asset | Classification | Raw-source mention |
|---:|---|---|---|
| 301 | `File:Hillary Clinton.png` | No discovered reference | None |
| 307 | `File:Cory Booker.jpg` | No discovered reference | None |
| 351 | `File:Flag of the Worker-Peasant Red Guards.png` | No discovered reference | None |
| 352 | `File:Emblem of the Korean People's Army.png` | No discovered reference | None |
| 353 | `File:Korean War.png` | No discovered reference | None |
| 359 | `File:Flag of Russia.svg` | Literal/template mention only | `Module:Portal/images/r` |
| 361 | `File:Flag of the Soviet Union (1923-1955).svg` | No discovered reference | None |
| 371 | `File:Flag of the Northwest Territories.png` | No discovered reference | None |
| 517 | `File:Hong Kong (22nd Century).png` | No discovered reference | None |
| 529 | `File:Community-header-background` | No discovered reference | None |
| 537 | `File:Flag of Arabia.png` | No discovered reference | None |
| 538 | `File:Assyrian Flag.png` | No discovered reference | None |
| 539 | `File:Flag of Iraqi Provisional State.png` | No discovered reference | None |
| 549 | `File:Kirsten Gillibrand, official portrait.jpg` | No discovered reference | None |
| 550 | `File:John Hickenlooper.jpg` | No discovered reference | None |
| 552 | `File:Tulsi Gabbard, official portrait.jpg` | No discovered reference | None |

The sole raw mention, Russia's flag in `Module:Portal/images/r`, is a portal image mapping and does not establish a page's rendered use. The other 15 are candidates for unused historical uploads, indirect dependencies, or parser/index omissions—not confirmed orphans.

## High-reference assets and useful leads

- `File:Cold War Logo.png` (index 530) is referenced by 14 pages, including the wiki portal, Third Mexican-American War, United States of America, Second Vietnam War, and Mexico.
- `File:Under contruction icon-red.png` (index 547) appears in ten page records, including political-party and WIP-related sources.
- `File:Flag of the United Kingdom.png` (index 579) appears in eight records, including several infobox templates and documentation. This likely reflects shared template-level dependencies; do not count all eight as independent article uses.
- Romania and Czech Republic flag assets (indices 381 and 383) each appear in seven records, including Intermarium and infobox template/documentation pages.
- `File:East Asia Flag.png` (index 396) appears in seven geopolitical/national pages, including Federal Republic of China, United Federation of China, Japan, and Korea.
- The placeholder portraits for Zaya Blank, Dom Terragno Blank, and Maya Garcia Blank are each referenced by four records spanning leadership and election pages.

## Interpretation and limitations

This batch's exact-reference rate is higher than the first batch (94.7% vs 89.3%), but this should not be interpreted as better asset quality. Manifest ordering is historical and the batches have different asset types. Several high-frequency references are shared template or documentation dependencies. A proper rendered dependency graph requires template expansion, module evaluation, alias resolution, and page-level validation.

No media files, Bronze Wikitext, or manifest values were modified. The cross-reference results are descriptive and do not validate the historical accuracy or canonical status of the images.

## Cumulative progress

For manifest entries 1–600:
- Exact extracted references: **552/600**.
- Raw/template mentions without exact extracted reference: **7**.
- No discovered reference: **41**.
- Exact-reference asset-to-page edges: **1,401** (876 in tranche 1; 525 in tranche 2).

Across the full corpus, the earlier first-pass title comparison identified 792 of 900 assets with an exact extracted reference and 108 without; it also found 141 extracted image titles without exact manifest counterparts. Those full-corpus counts are not yet reconciled for aliases, normalized names, and template expansion.

## Next tranche

Continue with manifest entries 601–900 using the same three-way classification, then perform alias/redirect/template reconciliation before calling any asset orphaned or missing.
