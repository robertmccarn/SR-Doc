# SR-Doc Research Continuity Notes

> Persistent handoff for future research sessions and future AI agents working on this repository.
> This document is an evolving research log, not an authoritative statement of fictional canon.
> Last updated: 2026-11-19.

## 1. Mission

Conduct a comprehensive, source-grounded audit of the SR-Doc repository: individually read the captured source pages, inspect the actual media assets, understand the setting's history and geopolitics, and build a traceable continuity record.

The user explicitly asked for individual reading of all 3,579 captured source pages and inspection of every media asset. The user later requested larger batches (up to 300 pages) and asked that every tranche begin with an overall progress report.

Do not substitute a superficial overview, manifest scan, generated Markdown, or previous AI summary for reading the original source. The goal is to understand the entire setting and preserve provenance.

## 2. Critical operating rules

1. **Read source files directly.** Prefer the original Bronze Wikitext pages in `bronze/pages/`. Open the exact file before making page-specific claims. Silver Markdown/JSONL is useful for navigation and cross-reference, but is derived material.
2. **Do not invent completion.** A page is not "read" because it appeared in a manifest, filename list, contact sheet, earlier summary, or search result. Track separate statuses: `catalogued`, `opened`, `read`, `partially_read`, `not_started`, `unavailable`.
3. **Do not silently repair canon.** Preserve source wording, dates, names, claims, and contradictions. Do not reconcile conflicting statements unless the source itself does so. Record conflicts with exact page IDs and quotations or line/section locations.
4. **Separate evidence from interpretation.** Label findings as:
   - **Source fact:** explicitly stated in a source page.
   - **Cross-source observation:** supported by multiple named source pages.
   - **Inference:** a reasoned interpretation, not explicit canon.
   - **External fact:** real-world knowledge or web research, kept separate from in-universe claims.
5. **Redirects and short pages count.** Record them as such; follow redirects to their target for context, but do not count the target as a second read unless its own file is opened.
6. **Namespace discipline.** The 3,579 captured pages are not 3,579 narrative articles. Keep main-namespace pages distinct from templates, file descriptions, talk pages, users, modules, categories, and other namespaces.
7. **Media inspection means viewing the actual asset.** A filename, description page, manifest status, thumbnail list, or checksum is not a visual inspection. Record file name, format, dimensions, actual visual content, legibility, and any apparent mismatch with its description. For SVG, render it before visual inspection. For GIF, inspect animation frames, not just the first frame, when animation matters.
8. **Never claim all media are reviewed until all actual files are accounted for.** The manifest and local file counts differ; reconcile missing, duplicate, and failed assets explicitly.
9. **Keep progress reports honest and reproducible.** Each tranche report should state the exact page IDs/titles or asset filenames, actual statuses, counts completed in that tranche, cumulative counts, and what remains. Do not infer counts from conversational batch labels.
10. **Do not let earlier AI notes become canon.** Prior assistant tranche summaries may contain inaccurate or fabricated details. Treat them as leads only; reopen source pages before reusing any claim.

## 3. Repository and archive inventory

Repository: https://github.com/robertmccarn/SR-Doc

At the time this note was written:
- Default branch: `main`.
- Research branch: `audit/continuity-research` (created for this work; do not merge without user approval).
- User supplied `SR-Doc-Audit.zip` in the conversation. The archive was approximately 247.01 MiB compressed and 270.33 MiB uncompressed.
- The ZIP inventory contained 8,076 files:
  - 3,579 `.wikitext` files.
  - 3,583 `.md` files.
  - 682 PNG, 160 JPG, 13 JPEG, 34 SVG, 6 GIF, and 1 WebP files (896 raster/vector files by these extensions; confirm exact local media count against manifest).
  - Other source/code/manifest files.
- The repository's prior manifest inventory reported 3,579 captured pages and 900 media records.
- Earlier namespace count reported from the archive: 507 main-namespace pages, 906 file-description pages, 744 templates, 625 talk pages, 104 user pages, 102 modules, with remaining pages in other namespaces. Re-derive these counts from the actual manifest before treating them as definitive.
- Earlier local asset inventory reported 899 files against 900 manifest records. Reconcile actual archive contents and manifest; do not assume the earlier count is final.
- Asset manifest status reported earlier: 728 `existing_verified`, 171 `downloaded_checksum_mismatch`, 1 `failed`. A later visual-review report claimed different per-batch status counts; recompute from the manifest rather than carry forward conflicting conversational figures.

## 4. Current progress: deliberately conservative accounting

Previous assistant messages claimed:
- 180 of 507 main-namespace pages reviewed.
- 434 of 900 media assets visually inspected.

**These figures are not independently verified and must not be treated as reliable completion counts.** Earlier responses sometimes described entries as "read" without demonstrating that the exact original Wikitext had been opened and examined. Some tranche inventories also appear to have been generated from an assumed alphabetical sequence. Re-establish the ledger from source files and mark previous claims as `unverified_prior_claim` until confirmed.

The last user-visible tranche was titled "Flags of the United States through Hillary Clinton" and claimed cumulative progress of 180/507. The next intended alphabetical tranche was to begin with "Hivvir". This is a navigation hint only, not proof that the preceding 180 files were read or that Hivvir is the next manifest entry. Verify the actual manifest ordering first.

The media review previously claimed two batches of 300 and one final batch of 134, but the reported counts conflict with the 900-record manifest. Do not assume media review is complete. Rebuild the visual-inspection ledger from filenames and actual assets.

## 5. Required working artifacts to maintain

As work proceeds, create and update structured records in this branch. Suggested paths:

- `research/README.md` — research index and methodology.
- `research/page-ledger.csv` — one row per source page: page ID, namespace, title, path, status, read date, reviewer/session, word count, notes path.
- `research/media-ledger.csv` — one row per manifest media record: source title, local path, format, dimensions, bytes, decode/render status, visually inspected status, checksum status, notes.
- `research/page-notes/` — detailed notes keyed by page ID, e.g. `1420-Argentina.md`.
- `research/continuity-issues.md` — contradictions and unresolved questions, each linked to exact source pages and passages.
- `research/entities.md` — people, organizations, states, places, species, technologies, and aliases, with source references.
- `research/chronology.md` — event chronology with exact source citations and conflicting dates preserved.
- `research/session-log.md` — append-only session log with work actually completed.
- `research/decisions.md` — user decisions, scope, and methodological choices.

Do not create empty artifacts merely for appearance. Establish a file when there is enough grounded material to populate it. CSVs should be machine-readable and stable; avoid changing column meanings after creation.

## 6. Per-page review template

For each source page, record:

- Page ID and exact title.
- Namespace and source path.
- Page type: narrative, biography, country/state, institution, battle/conflict, technology, species/ecology, reference, redirect, placeholder, discussion, template, etc.
- Read status and approximate source length.
- Concise but substantive source-faithful summary.
- Explicit dates, people, organizations, locations, technologies, and numeric claims.
- Internal links to other pages.
- Empty sections, WIP/TBA markers, contradictory infobox/body claims, and apparent typos (do not silently correct).
- Cross-source leads to verify.
- Exact source evidence: headings and/or short quoted passages sufficient to locate the claim.

Long articles require deeper notes than redirects. Do not compress long histories into generic one-paragraph summaries.

## 7. Per-media review template

For each actual asset, record:

- Manifest title and local filename/path.
- Format, dimensions, file size, and animation frame count if applicable.
- Successful decode/render status.
- What is visibly depicted; distinguish clear observation from uncertain identification.
- Any text, labels, legend, dates, borders, political boundaries, or symbols that are legible.
- Whether the asset appears consistent with its MediaWiki description and related source articles.
- Checksum result separately from visual integrity.
- Missing, duplicate, malformed, or suspicious assets.

Contact sheets are useful for triage, but zoom into individual images when text, maps, symbols, or fine details matter. A contact sheet alone is not sufficient for detailed inspection.

## 8. Tranche reporting format

At the beginning of every tranche, give a compact progress block:

- Current tranche number and exact scope.
- Pages/assets actually read or visually inspected in this tranche.
- Cumulative verified total / total.
- Percent complete.
- Counts by status (read, partial, not started, unavailable).
- Any changes to previous counts and why.

Then provide:
1. Exact inventory of entries handled.
2. Source-grounded findings, grouped by theme.
3. New continuity issues, with source IDs.
4. Cross-article connections clearly labeled as observations or inferences.
5. Next exact manifest entries.

If a tranche contains 300 files, do not imply all 300 received equal analytical depth. Use batching for ingestion and inventory, but individually track actual review. The user has asked for large batches (up to 300) but accuracy is more important than making a batch look complete.

## 9. Early thematic map (leads, not settled conclusions)

Prior conversation identified recurring storylines worth testing against source files:

- Climate catastrophe, the Flood, famine, the Refreeze, and ecological restoration.
- American political realignment, White Tide, successor states, and the evolution of the U.S. into a planetary power.
- World War III, Japan/Turkey, orbital command infrastructure, and postwar security architecture.
- Mexican-American conflicts, Aztlan, and the transition to the Third Mexican-American War.
- Mars colonization, MarsCorp, the First Martian Revolution, the Interplanetary Trade Commission, and colonial statehood.
- Human augmentation, genetic engineering, AI/Android sentience, and changing legal definitions of personhood.
- Alien civilizations and First Contact, including Argommi, K'lerin, Hiilo, Hivvir, Ckuteko, and other species.
- Associated states, protectorates, planetary governments, and the post-2139 international order.
- Dyson swarms, gravitonics, interstellar travel, and megastructure engineering.

These are navigation aids. Confirm every specific claim against source files.

## 10. Known potential continuity leads from previous discussion (all require re-verification)

The following were flagged in earlier conversation summaries. Reopen the named source files and verify before treating any as genuine issue:

- Argentina: annexation date and missing Mexican-American War sections.
- Argommi: First Contact chronology, Great Flood death tolls, and post-contact political settlement.
- Armor: model chronology, power sources, and military capabilities.
- AIOS / Android: imprinted-AI ban, 35th Amendment, sentience, and cache-purging regulations.
- Associated state / Association of East-Asia: sovereignty, founding dates, leadership succession.
- Atlantis: Nemo Station Incident, terraforming, and biological containment.
- Aztlan War: incomplete narrative and relationship to the Third Mexican-American War.
- Battle of Brazil: missing operational sections.
- Battle of Washington: dates, force sizes, and orbital reinforcements.
- Bradbury: conflicting founding and Meridian food-delivery dates.
- British Republic / Canada: 2073 Union Act and subsequent territorial status.
- Chronoscope: 2112 warrant requirement and later law-enforcement use.
- Chemical Element: discovered versus named element counts and fictional element claims.
- Crisis of 2130 / Eighth Party System: Personal Liability Corporation economy and collapse.
- Earth / Demographics: Earth population versus Earthsphere population scope.
- Edwin Jaso: presidency start date and age at death.
- Guardiola Foundation / Incident: founding dates and casualty totals.
- Gravitonics: physical limits and chronology.
- Germany and successor states: dissolution chronology.
- European Association: 2139 founding and later territorial expansion.

## 11. Git and collaboration rules

- Continue work on `audit/continuity-research`.
- Do not push research notes to `main`.
- Commit incremental, coherent updates with descriptive messages.
- Keep this `agents.md` file appendable and update its "Current progress" section whenever a tranche is completed.
- Never overwrite source captures. Research notes must remain separate from Bronze/Silver/Gold source data.
- Do not merge the branch or open a PR unless the user asks.
- After each push, report the branch, commit SHA, and changed paths.

## 12. Immediate next actions

1. Re-read the manifests from the uploaded archive or repository and generate a canonical ordered list of the 507 main-namespace source pages.
2. Reconcile that list with the previous conversational tranche claims. Mark prior entries `unverified_prior_claim` until each exact source file is reopened.
3. Create the page and media ledgers.
4. Resume at the first unverified main-namespace page in canonical order; do not assume the next page is Hivvir without checking.
5. Inspect actual media files systematically and reconcile all 900 manifest records against local assets.
6. Update this document and the ledgers after every tranche.

---

## Append-only session log

### 2026-11-19 — Initial handoff creation

- User supplied `SR-Doc-Audit.zip`; archive inventory observed at approximately 247.01 MiB compressed / 270.33 MiB uncompressed.
- Repository `robertmccarn/SR-Doc` inspected. Default branch is `main`; main head at handoff time: `f187e4034211feb3a9e43534654b1486cec66bc1`.
- Created research branch `audit/continuity-research` from `main`.
- Prior conversation reported 180/507 pages and 434/900 media assets, but these are explicitly unverified claims and must be reconciled.
- User asked to pause reading and create a persistent handoff document for future agents.
