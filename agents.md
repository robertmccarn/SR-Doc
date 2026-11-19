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


# Addendum A — Full continuity handoff and prior-session record
## Appended 2026-11-19

This addendum preserves the fuller working context available from the prior audit conversation. It is intentionally explicit about the difference between repository facts previously observed, conversational claims that still need rechecking, and planned work. It supplements rather than replaces the methodology and rules above.

## A1. Scope interpretation: do not narrow the audit

The user's requested scope was an individual review of **all 3,579 captured source-page files** and inspection of **every media asset** in the supplied archive. The repository inventory distinguishes 507 main-namespace pages from the much larger set of captured pages in other namespaces. Those numbers describe different scopes:

- **3,579** is the previously reported total count of captured page/Wikitext source files across namespaces.
- **507** is the previously reported main-namespace subset.
- The remaining pages include non-main-namespace material such as File descriptions, Templates, Talk pages, Users, Modules, Categories, and other namespaces.

Do not reinterpret the user's request as only 507 pages. Maintain a page ledger for the entire captured source-page set. Namespace and page type should inform the depth and style of review, not silently remove a page from the inventory. For example, a template may be reviewed as a template rather than summarized as narrative, but it still needs a traceable status. File-description pages are not substitutes for inspecting the corresponding binary media assets.

There are two related review tracks:
1. **Page/source track:** account for every captured Wikitext page, distinguish namespaces, and inspect original source text.
2. **Media track:** account for every manifest media record and every actual local asset, inspect the actual image/vector/animation, and reconcile records with files.

Keep the 507-page main-namespace progress metric as a useful sub-metric only. It must never be presented as the total page-audit completion metric.

## A2. Repository architecture and data flow observed during the earlier inspection

The following architecture was described in the README and corroborated by selected source/code inspection. Reopen files when implementation details become important; this is a continuity map, not a substitute for a fresh repository review.

### Bronze
Bronze is the raw/provenance-oriented capture layer. It contains the captured MediaWiki Wikitext source, page metadata, media files/assets, and manifests. The design intent is to preserve source material and identifiers so downstream processing can be traced back to the imported source.

### Silver
Silver contains deterministic transformations of the captured material, including Markdown and JSONL outputs, extracted internal links, year mentions, and a generated continuity report. It is useful for indexing, cross-reference, and navigation. It is derived data: a Silver Markdown rendering or extracted JSON record is not proof that the corresponding original Wikitext has been read.

The previously viewed Silver continuity report reported:
- 3,579 source pages.
- 11,462 extracted wiki links.
- 4,447 year mentions.
- The most frequently mentioned year was reported as 2160.

These are earlier report values, not independently revalidated totals. Re-run or inspect the current transformation output before using them as current metrics. Also distinguish the report's definition of a page/link/year from any hand-built review ledger.

### Gold
Gold is the reviewed narrative-additions/proposals area. Its purpose is to keep human-reviewed or proposed narrative additions distinct from imported source canon. Gold content must not be mistaken for source capture. Any proposal or extension must remain clearly marked and traceable to its rationale/source references.

### Site and rendered wiki
The repository also contains a `site/` area associated with MkDocs navigation/overview inputs, plus a locally rendered wiki based on captured MediaWiki parsed HTML. The rendered wiki is a convenience for browsing and presentation, not the authoritative source for source-faithful review. Reopen the original Bronze capture for claims about what a page says.

## A3. Earlier code and workflow inspection: observations to retain

The previous inspection touched the following files or areas. These are the files specifically covered in that review, not a claim that every repository file has been exhaustively audited:

- `README.md`
- `pyproject.toml`
- `.gitignore`
- `.gitattributes`
- `.github/workflows/continuity.yml`
- `sr_doc/archive.py`
- `sr_doc/transform.py`
- `sr_doc/validate.py`
- `sr_doc/wiki.py`
- `tests/test_transform.py`
- `gold/README.md`
- `gold/examples/proposal.md`
- `silver/continuity-report.md`
- manifests in `bronze/manifests/`

The following are concise records of the code-level findings from that pass. Re-open and verify before proposing code changes or describing current behavior as definitive.

### `sr_doc/archive.py`
The earlier review found that the archive/capture implementation obtains current MediaWiki page revisions and page metadata and handles media asset capture. The reviewed behavior included retries, pagination, a download budget, and checksum verification. It did **not** appear to preserve the complete historical revision history of each page; the capture appeared centered on current revisions. This distinction matters: the archive is a provenance-preserving snapshot, but it should not be described as a full MediaWiki revision-history archive unless a fresh review finds additional history capture.

### `sr_doc/transform.py`
The earlier review found deterministic transformation behavior for headings, wiki links, year mentions, warnings, and Wikitext-to-Markdown conversion. It should not be characterized as a full semantic knowledge graph, comprehensive entity resolver, or robust chronology parser. Extracted links and year mentions are useful leads, but require human/source review for meaning, context, and temporal interpretation.

### `sr_doc/validate.py`
The earlier review found validation around Gold front matter, unique IDs/statuses, accepted extension rationale or source page IDs, and page references. It did not appear to perform deep semantic contradiction detection across the narrative corpus. Passing validation therefore does not establish that the fictional chronology is internally consistent.

### `sr_doc/wiki.py`
The earlier review found logic for capturing rendered HTML and building a static HTML wiki. One potential staleness concern was that existing rendered captures could be skipped without checking whether the upstream page revision had changed. HTML link and media rewriting appeared relatively basic. Recheck current behavior and tests before filing an issue; retain this as a code-review lead, not a confirmed current defect.

### Tests and CI
The earlier pass only specifically noted two tests in the inspected test file: slug generation and the root wiki shell. This does not prove that the entire repository has only two tests; it means the test coverage observed during that review was very narrow. The CI workflow inspected was `.github/workflows/continuity.yml`. Re-inventory all tests and workflow behavior before making broader coverage claims.

### Git LFS
The repository's `.gitattributes` was observed to apply Git LFS to `bronze/assets/**`. GitHub file APIs or source views may therefore return LFS pointer text rather than the actual image bytes. Do not treat a pointer as a downloaded or inspected asset. For a visual review, obtain the actual LFS object or inspect the corresponding asset from the user-provided archive, then confirm that it is the same object/path represented by the manifest.

## A4. Archive inventory and reconciliation details

The prior archive inventory reported an archive named `SR-Doc-Audit.zip`, approximately 247.01 MiB compressed and 270.33 MiB uncompressed. The reported ZIP inventory contained 8,076 files, including:

| Item | Earlier reported count | Notes |
|---|---:|---|
| `.wikitext` files | 3,579 | Captured page-source files; audit all namespaces |
| `.md` files | 3,583 | Derived Markdown count; do not equate 1:1 with source-page review |
| PNG | 682 | Actual media file inventory; verify locally |
| JPG | 160 | Actual media file inventory; verify locally |
| JPEG | 13 | Actual media file inventory; verify locally |
| SVG | 34 | Render before detailed visual inspection |
| GIF | 6 | Inspect relevant animation frames |
| WebP | 1 | Decode and visually inspect |
| **Media by listed extensions** | **896** | Sum of the six extension rows above; reconcile |
| **Media manifest records** | **900** | Earlier manifest inventory; reconcile against assets |

A previous local inventory reported 899 asset files, while the extension inventory above sums to 896 and the manifest contained 900 records. These are three distinct earlier counts. Do not pick one and discard the others. Reconcile:
- manifest record count;
- unique referenced asset paths;
- files physically present in the archive;
- files physically present in the repository checkout;
- files that decode/render;
- files that are duplicates or aliases;
- files represented only by LFS pointers;
- manifest records with no file;
- files with no manifest record.

The earlier namespace count was reported as follows. These values are provisional until recalculated directly from the current manifest:

| Namespace/page category | Earlier reported count |
|---|---:|
| Main namespace | 507 |
| File-description pages | 906 |
| Templates | 744 |
| Talk pages | 625 |
| User pages | 104 |
| Modules | 102 |
| Other namespaces | Remainder; not recorded reliably |

The six named namespace counts total 2,988; the residual against 3,579 is 591. Do not infer the names or composition of that residual from this arithmetic. Recalculate namespace counts from the manifest and preserve the raw namespace identifier/name.

The media manifest was earlier reported to contain:
- 728 records with status `existing_verified`;
- 171 records with status `downloaded_checksum_mismatch`;
- 1 record with status `failed`.

Those values sum to 900 but remain earlier reported manifest counts, not a fresh audit. A later conversational media-review summary reportedly used different per-batch counts. Treat the manifest as the source for status reconciliation and actual file bytes as the source for visual inspection.

## A5. Prior page-by-page tranche claims: exact conversational record and reliability warning

Earlier assistant responses presented four consecutive tranche reports. The claims below are preserved so future sessions can reconcile them against an actual manifest and source files. **None of these tranche claims is independently verified by this handoff.** Do not import their purported contents as facts, do not mark the files read solely because they appeared in these reports, and do not claim these ranges are complete until each exact source file has been reopened.

| Prior report label | Claimed page range | Reported alphabetical boundary | Claimed cumulative progress |
|---|---:|---|---:|
| Tranche 1 | 61–90 | “British Cameroons” through “Council of the European Union” | 90 / 507 |
| Tranche 2 | 91–120 | “Country Code Top-Level Domain” through “Energy” | 120 / 507 |
| Tranche 3 | 121–150 | “Energy Industry” through “Flag of Europe” | 150 / 507 |
| Tranche 4 | 151–180 | “Flags of the United States” through “Hillary Clinton” | 180 / 507 |

Important reconciliation issues:
- The first listed report starts at page 61 even though its claimed cumulative count was 90/507. The conversational record available here does not establish what happened to pages 1–60. Do not assume they were reviewed.
- Later reports continued the 91–120, 121–150, and 151–180 numbering, but the numbering itself is not an auditable source record.
- The next intended alphabetical range was described as beginning with “Hivvir”. That is only a search hint. Verify actual manifest ordering and titles before using it as the next page.
- The four reports were described as if 30 pages had been handled in each tranche, but the available continuity record cannot establish that the exact Bronze Wikitext files were individually read. They may have been summarized from prior notes, title lists, or assumed alphabetical order.
- A previous response also described 3,579 pages as if they were all narrative articles and referred to “1,000+ Markdown article files.” That framing was misleading. The source corpus has multiple namespaces, and the 3,583 Markdown files are derived outputs, not proof of 3,583 narrative articles.

The correct recovery process is to generate a canonical page list from the current page manifest, map each row to the actual Bronze file, and set each status according to direct inspection. If a page from one of the reported ranges is genuinely opened and read during recovery, mark it verified then; do not mark an entire range complete by association.

## A6. Prior media-review claims: exact caution

A prior assistant response claimed that 434 of 900 media assets had been visually inspected. Another description implied that media work had been split into two batches of 300 and a final batch of 134. These claims are not independently supported by the available continuity evidence and should be classified as `unverified_prior_claim`.

Do not:
- report 434/900 as verified progress;
- assume the claimed 300 + 300 + 134 batches map to unique manifest records;
- equate a media description page, thumbnail, contact sheet, filename, checksum, or LFS pointer with a visual inspection;
- infer that all 900 manifest records correspond to 900 distinct local files.

Rebuild the media ledger using manifest IDs and exact local paths. Give each manifest record a distinct audit status, and separately track whether the underlying physical file exists, decodes, renders, and has been visually examined. For an asset referenced by multiple pages, preserve all relevant source-page relationships without double-counting the physical file as multiple unique assets.

## A7. Other prior continuity leads and thematic map

The earlier conversation identified the following broad thematic clusters as promising cross-source research paths. These are not verified canon statements and should remain research navigation hints until source-grounded:

- Climate catastrophe, the Flood, famine, the Refreeze, and ecological restoration.
- American political realignment, the White Tide, successor states, and the United States' development into a planetary power.
- World War III, Japan and Turkey, orbital command infrastructure, and postwar security architecture.
- Mexican-American conflicts, Aztlan, and the Third Mexican-American War.
- Mars colonization, MarsCorp, the First Martian Revolution, the Interplanetary Trade Commission, and colonial statehood.
- Human augmentation, genetic engineering, AI/Android sentience, and changing legal definitions of personhood.
- Alien civilizations and First Contact, including Argommi, K'lerin, Hiilo, Hivvir, Ckuteko, and other species named in the source corpus.
- Associated states, protectorates, planetary governments, and the post-2139 international order.
- Dyson swarms, gravitonics, interstellar travel, and megastructure engineering.

The previous notes also listed page-level leads in Section 10 above. In particular, revisit the Argentina, Argommi, Armor, AIOS/Android, Associated state/Association of East-Asia, Atlantis, Aztlan War, Battle of Brazil, Battle of Washington, Bradbury, British Republic/Canada, Chronoscope, Chemical Element, Crisis of 2130/Eighth Party System, Earth/Demographics, Edwin Jaso, Guardiola Foundation/Incident, Gravitonics, Germany, and European Association pages. The earlier notes mentioned possible date, casualty, population-scope, legal, sovereignty, and technology discrepancies, but none should be promoted to an issue until the source wording and exact passages are captured.

## A8. User instructions and interaction requirements carried forward

The following requirements were explicitly stated during the audit conversation and should guide future sessions:

- The user asked for the full source corpus to be individually read, not merely summarized from page lists or metadata.
- The user asked for every media asset to be inspected.
- The user asked whether batches of up to 300 pages were possible. Larger batches may be used for indexing or processing, but must not be represented as individually read unless they were.
- The user explicitly requested that each tranche begin with an overall progress report. Include total-scope progress and, separately, main-namespace progress and media progress.
- The user later said “pause” and requested a new branch plus a persistent `agents.md` handoff. That pause was a direction not to continue source-reading at that moment.
- The user requested this document be ongoing and potentially massive, so append substantive durable context rather than replacing earlier notes.
- Keep source claims, cross-source observations, interpretations, and external research distinct.
- Prefer traceable, auditable completeness over a fast but unreliable completion claim.
- Report actual branch, commit, and changed paths after GitHub writes. Do not alter `main`, merge, or open a PR unless explicitly requested.

## A9. Git handoff facts and commits

The following branch/commit information was returned by the GitHub operations in the handoff session:

- Repository: `robertmccarn/SR-Doc`.
- Branch created: `audit/continuity-research`.
- Branch base at creation: `main`, whose then-reported head was `f187e4034211feb3a9e43534654b1486cec66bc1`.
- Initial `agents.md` creation commit: `b095c7fcd2ba4c03c04de61a1f82ea168d8863b0`.
- Initial `agents.md` blob SHA after creation: `07adaba1cc3b3220e3108f179793c1c151f6afc6`.
- The original handoff document was fetched back from `audit/continuity-research` to verify its contents.
- `main` was not changed, no PR was opened, and no merge was performed.

This addendum is being appended to the existing branch file. The new commit/blob identifiers should be recorded in the response and in the session log after the update is verified.

## A10. Recovery checklist before resuming source review

Before presenting another content tranche, do the following in order:

1. Fetch the current branch version of this file and confirm the working branch.
2. Inspect the supplied ZIP or current repository manifests directly; do not rely only on the counts above.
3. Build a canonical row for every one of the 3,579 captured Wikitext pages, retaining page ID, namespace ID/name, title, exact path, and manifest provenance.
4. Build a separate canonical list for the 900 reported media records, retaining manifest identity, file path, source title, checksum/status, and all discoverable page references.
5. Reconcile source-page and media manifest counts with actual files on disk and with any Git LFS pointers.
6. Create the full-corpus ledgers before deciding what has already been reviewed.
7. Import prior conversational ranges only as candidate leads. Mark them unverified until exact source files are opened and read.
8. Resume from the first unverified row in a declared ordering, and state that ordering (e.g., manifest order, page ID order, or title order) in the progress report.
9. Keep review status and analytical depth separate. “Catalogued,” “opened,” “read,” and “deeply analyzed” are not interchangeable.
10. Append each completed tranche's exact inventory, findings, questions, and verified counts to research artifacts and this file's session log.

## A11. Append-only session log — addendum

### 2026-11-19 — Full continuity addendum requested

- User requested an addendum to the existing root `agents.md` containing the full, unabridged continuity notes for future assistant sessions.
- Existing file was fetched from `audit/continuity-research` before editing; its original contents are to be preserved and this addendum appended.
- Addendum records the full requested audit scope, repository architecture, selected code-review observations, archive-count discrepancies, previous page/media tranche claims and their unverified status, thematic navigation leads, explicit user instructions, and Git handoff facts.


# Addendum B — First verified source tranche
## Appended 2026-11-19

This section supersedes any interpretation of Section 4 as describing current progress. It does not retroactively validate the prior 180-page claim.

### B1. Inventory rebuilt from the supplied archive

The supplied ZIP was read directly. The page manifest contains 3,579 records, and all 3,579 manifest raw_path files were found in the ZIP. The recalculated namespace counts are:

| Namespace | Count |
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

The all-namespace scope remains the user's requested scope. Main-namespace alphabetical order is being tracked as a sub-sequence; it must not be mistaken for the whole corpus.

The archive contains 8,076 files, including 3,579 Wikitext files and 3,583 Markdown files. The media manifest has 900 records: 728 `existing_verified`, 171 `downloaded_checksum_mismatch`, and one `failed` record (HTTP 404). The ZIP contains 899 physical files under `bronze/assets`: 682 PNG, 160 JPG, 13 JPEG, 34 SVG, 6 GIF, 2 ICO, 1 WebP, and 1 file without an extension. The 899 physical files equal the 899 non-failed manifest rows by count; exact path-to-record mapping still needs verification. No assets have yet been marked visually inspected in the reconstructed media ledger.

### B2. Page-ledger status after tranche 5

Created:
- `research/README.md`
- `research/page-ledger.csv` — one row for each of the 3,579 captured pages
- `research/media-ledger.csv` — one row for each of the 900 media manifest records
- `research/page-notes/main-181-210.md`
- `research/session-log.md`

Ledger status:
- 31 pages directly read: positions 181–210 (30 pages) plus Vactrain (page ID 2693), opened as the target of Hyperloop.
- 180 main-namespace entries flagged `unverified_prior_claim`; not counted as read.
- 3,368 remaining records are `not_started`.
- Verified total: 31 / 3,579 captured source pages (0.87%).
- Verified main-namespace source reads: 31 / 507 (this includes the out-of-order contextual Vactrain read); the contiguous requested tranche was positions 181–210.
- Media visually inspected: 0 / 900 manifest records.

### B3. Tranche 5 details

- Ordering: main-namespace titles sorted case-insensitively.
- Exact range: positions 181–210, Hivvir through Joaquín Andrade.
- All 30 original Bronze Wikitext files in this range were opened and read.
- Vactrain (ID 2693) was additionally opened as the redirect target for Hyperloop (ID 3695).
- Redirects reviewed in-range: Honda Hippies (movement) → Honda Hippies (target absent from archive manifest); HTML attribute, Human Development Index, ISO 4217, and IUCN Red List → Wikipedia interwiki targets; Hyperloop → Vactrain; Hypersonic weapon → Hypersonic Weapons; Indian War of 2126 → India Crisis.
- No media were visually inspected.

### B4. Main source leads recorded

The detailed notes are in `research/page-notes/main-181-210.md`. Highest-priority leads include:
1. Hypersonic Weapons says the Mexican Vacuum Command emerged in 2113, then says Mexico deployed its own OKW platforms “by 2028.” Keep the exact 2028 date; do not silently amend it.
2. India Crisis infobox dates the conflict 2119–2126, while the cyberattack, cabinet deaths, provisional government, elections, and referendum are dated in the body to 2118.
3. Hong Kong's infobox lists USD, while prose refers to the Hong Kong dollar.
4. Intermarium's infobox says “The Americas” as its continent, while the prose and member list describe Eastern Europe.
5. Human says 27 recognized subclades but the displayed table lists ten.
6. The ITC and Horace Fadel articles have election-year wording that should be cross-checked against the 2080 election and presidential chronology pages.
7. Hong Kong's Association of East Asia accession is dated 2140; Japan's dissolution/succession is dated 2141.
8. Hivvir and Hyperion both touch first-contact material, but do not assume the K'lerin contact and Ivrilu contact are the same event.

### B5. Next ordered main-namespace tranche

The next 30 main-namespace entries are positions 211–240:
Joseph Loveridge; Jupiter; K'lerin; Kahi'Umknovola; Khuzestan War; Korea; Korean reunification; Korean War (2017–2019); Korean War (2017–2021); Korean War (2018–2021); Lakota Republic; Late 2010s Recession; Latin American Union; Latvia; Latvian lats; Le'ma; League of Nations; Least Concern; Legislature of the European Union; Liberaccion Party (United States); Liberacion Party (United States); Liberal Party (United States); Lieutenant Governor of Maryland; Lionel Halvidar; Lise Duchesne; List of countries by population; List of countries by population, 2160; List of heads of state of Cameroon; List of heads of state of Mexico; List of Minyan Fauna.

Continue to keep the unverified earlier pages and all non-main-namespace pages in the ledger. The next ordered tranche must not cause the remaining all-namespace work to be forgotten.


# Addendum C — Main-namespace tranche 6
## Appended 2026-11-19

### C1. Verified work
- Reopened the supplied `SR-Doc-Audit.zip` and re-derived main-namespace alphabetical positions 211–240 from the page manifest.
- Directly opened and read all 30 original Bronze Wikitext files in that range, Joseph Loveridge through List of Minyan Fauna.
- Also opened Population growth (page ID 2446) and Minya (page ID 2626) as contextual redirect targets.
- No media were visually inspected.
- Detailed notes: `research/page-notes/main-211-240.md`.

### C2. Updated verified progress
- 63 / 3,579 captured pages directly read (1.76%): 31 prior unique reads + 30 tranche pages + 2 new contextual targets + Vactrain was already included in the prior 31. The ledger records 64 unique read pages in total.
- 180 earlier main-namespace entries remain `unverified_prior_claim`; do not count them.
- 3,335 page records remain `not_started`.
- Media visual inspection remains 0 / 900.
- The page ledger is authoritative for per-record status: 63 `read`, 180 `unverified_prior_claim`, and 3,336 `not_started`.

### C3. Important continuity leads
- Korea chronology spans several distinct-looking conflicts: a 1950–1953 war, redirect titles from 2017–2021, and a reunification crisis beginning in 2026 and culminating in 2031.
- Kahi'Umknovola's First Contact passage names IV-403 Endurance, then refers to Discovery's captain.
- Jupiter's stated moon populations (300m combined), total population (340m), and 76% moon-resident share do not reconcile.
- Lionel Halvidar's article dates Camp Navajo's triggering attack to 2 February 2133 but describes 15 April mobilization before giving that date later in the narrative.
- Liberal Party founding date differs between infobox (2052) and prose (2029).
- See the tranche note for detailed source wording and all additional issues.
 
### C4. Next main-namespace tranche
Positions 241–270: List of presidents of Brazil; List of recessions in the United States; List of Sophonts; List of states and territories of the United States; List of Third Mexican War weapons; List of World War III weapons; Lithuania; Little Cold War; Little Wall Street Affair; Liza Maheswaran; London; Lost Decade (China); Lower house; Luis Zepeda; Luna; Maastricht Treaty; Main Page; Maisie Luong; Malcolm Moreau; Mall; Market Crash of 2027; Mars; Mars Corporation; Martin O'Malley; Martin O'Malley (The Second Renaissance); Maya Garcia; Mediterranean Union; Member state of the European Union; Mercury; Mex-American Cold War.


# Addendum D — All-namespace manifest tranche 1–300
## Appended 2026-11-19

### D1. Verified work
- The next batch size is 300 captured source pages, in original manifest order, across all namespaces. Do not return to 30-page main-namespace-only tranches unless the user changes the instruction.
- Directly opened/read manifest entries 1–300 from their original Bronze Wikitext paths.
- Namespace composition: Template 163; File description 75; Main 17; User 16; Category 13; Board 5; MediaWiki 3; Message Wall 3; Thread 3; Template talk 1; Blog 1.
- Two records were already directly reviewed (Lionel Halvidar, page 212; Interplanetary Trade Commission, page 216). This tranche therefore adds 298 unique page reads.
- Detailed notes: `research/page-notes/manifest-001-300.md`.

### D2. Corrected progress baseline
- The page ledger immediately before this tranche contained 63 unique `read` records, 180 `unverified_prior_claim` records, and 3,336 `not_started` records. An arithmetic sentence in Addendum C saying 64 unique reads was incorrect; use the ledger as the source of truth.
- After marking manifest entries 1–300 as read, the ledger contains 361 `read`, 176 `unverified_prior_claim`, and 3042 `not_started` records (3579 total).
- Media visual inspection remains 0 / 900. File-description pages do not count as viewing media.

### D3. Continuity leads
- India Crisis: timeline 2119–26 vs 22nd Century politics list 2126.
- Third Mexican War: infobox 2 February 2133 vs timeline/22nd Century invasion phase in 2134.
- Progress Party: infobox 17 October 2023 vs prose 2060; merger successor UPP in 2155.
- WWIII end date has multiple source-stated conventions (ceasefire, surrender, treaty).
- Dylan J. Price birth date: 13 April 1985 in infobox vs 9 November 1985 in prose.
- Earth Commonwealth establishment: prose 2136 vs infobox 4 July 2137.

### D4. Next ordered batch
Manifest entries 301–600. Continue from the next 300 rows in the page ledger/manifest, not the main-namespace alphabetical list. Read every source directly and retain the all-namespace scope.


# Addendum E — All-namespace manifest tranche 301–600
## Appended 2026-11-19

### E1. Verified work
- Directly opened/read manifest entries 301–600 from their original Bronze Wikitext paths.
- Independently recomputed SHA-256 for all 300 UTF-8 source texts; all matched the manifest raw_sha256 values.
- Namespace composition: File descriptions 143; Templates 125; Modules 23; Main 4; User 3; Message Wall 1; Thread 1.
- Two prior unverified claims (Conservative Party (United States), page 310; Evalyn Jacobi, page 317) were reopened and verified. No page in this tranche had already been credited as read. This tranche adds 300 unique verified reads.
- Detailed notes: `research/page-notes/manifest-301-600.md`.

### E2. Verified progress
- Page ledger after this tranche: 661 read, 174 unverified_prior_claim, 2744 not_started (3579 total). This is 661 / 3,579 (18.47%) directly read.
- Main namespace: 82 / 507 directly read (16.17%).
- Media visual inspection remains 0 / 900. Reading File-namespace descriptions does not count as viewing the underlying media.

### E3. Continuity and structural leads
- Mars is called the second planetary commonwealth in its article, but the commonwealth list orders Earth, Luna, Mars (third).
- Mars article says ITC was absorbed into the federal government in early 2133; ITC article page 216 gives dissolution 1 June 2134.
- Earth page 272 says 145 states, while the commonwealth table lists 146.
- Mars population 3,003,102,000 vs 3bn rounded; water coverage half vs 53%; executive constitutional officers described as independently elected and appointed/confirmed.
- Mars admission date 4 July 2137 vs integration/statehood events in 2136; its page also describes 50 territories receiving statehood by 2134 and 500 states in 2160.
- Commonwealth infobox template documentation and implementation disagree on StateAnthem/PlanetaryAnthem and Lieutenant Governor parameter names. European Association flag template alt text names South Australia.
- See tranche note for details and exact source references.

### E4. Next batch
Manifest entries 601–900. Continue all-namespace manifest order in 300-page batches.


# Addendum F — All-namespace manifest tranche 601–900
## Appended 2026-11-19

### F1. Verified work and progress
- Directly opened/read all 300 original Bronze Wikitext sources in manifest order 601–900, across all namespaces.
- Recomputed SHA-256 for all 300 decoded texts: 300 matched manifest hashes; zero mismatches.
- Before the tranche, the 300 rows were 294 `not_started` and six `unverified_prior_claim`; none were already credited as read. All 300 are now direct reads.
- Namespace composition: Template 161; Module 54; File description 36; Main 20; Talk 15; User 2; Message Wall 6; Thread 6.
- Detailed source notes: `research/page-notes/manifest-601-900.md`.

### F2. Verified page progress
- 961 / 3,579 pages read (26.85%); 168 unverified_prior_claim; 2,450 not_started.
- Main namespace: 102 / 507 read (20.12%).
- Media visual inspection: 0 / 900. The 36 File-description pages in this tranche do not count as viewing the corresponding assets.
- Seven File-description Wikitext files are empty; all six Message Wall Wikitext files are empty.

### F3. Main source leads
- 2132 presidential election (ID 636): displayed candidate percentages total 94.3%; candidate slot 3 is absent although the prose says six major candidates; Halvidar's listed share is 37.5%.
- The Flood (ID 637): chronology gives 2026 South Greenland event, 2039 Antarctic loss, and 2041 peak in an internally awkward sequence.
- Market Crash of 2027 (ID 642): article says crash began 24 October 2027, but timeline narrates the market break on 4 January 2027.
- Mars Corporation (ID 638): first planetfall 26 April 2023; previously read Mars article ID 318 gives a crewed mission in 2026.
- Federal Republic of China (ID 649): 2108–2139 infobox but Foundation section is TBA and historic Republic of China infobox material remains.
- Guardiola Foundation (ID 823): anomalous “In early 2022, a war with a show...” origin sentence.
- Oscar Lachman (ID 896): birth 21 October 2021 and death 18 April 2136; infobox says age 115.
- Carla Anderson (ID 902) and First Nations War (ID 911): shared 2064–2067 war narrative and 2073 Union Act annexation.
- See tranche notes for full source summaries, vote arithmetic, conflict details, namespace inventory, and editorial talk-page leads.

### F4. Next batch
Continue with manifest entries 901–1200, in original manifest order, all namespaces.


# Addendum G — All-namespace manifest tranche 901–1200
## Appended 2026-11-19

### G1. Verified work
- Directly opened/read all 300 original Bronze Wikitext files at manifest entries 901–1200, all namespaces.
- Recomputed SHA-256 for all 300 decoded source texts: 300/300 matched the manifest; zero mismatches.
- Prior ledger status in the batch: 13 read, 51 unverified_prior_claim, 236 not_started. After this review, all 300 are read; this adds 287 unique verified reads.
- Namespace composition: Main 114; Talk 74; File 46; Template 30; Module 21; Category 3; User 1; Message Wall 4; Thread 5; Board Thread 2.
- Detailed notes: `research/page-notes/manifest-901-1200.md`.

### G2. Progress
- 1,248 / 3,579 read (34.87%); 117 unverified_prior_claim; 2,214 not_started.
- Main namespace: 203 / 507 read (40.04%).
- Media visual inspection remains 0 / 900. This tranche's 46 File descriptions are not visual inspections.
- 82 redirects were reviewed (80 Main, one Template, one File); 17 source pages are empty (13 File descriptions, four Message Walls).

### G3. Continuity leads
- Intermarium's infobox geography says Americas while its prose describes Eastern Europe; the Allies of WWIII page lists it in a 2051–55 alliance although Intermarium's formal founding date is 2102.
- Poland federation start date 2076 vs 2077.
- Aztlan secession timeline/count wording; 2136 election infobox field says Vice President.
- Liberal Party founding 2029 in prose vs 7 December 2052 in infobox.
- Fifth Great Awakening's time span differs within the article.
- Mars colonization anchors 2023 and 2026 conflict across Mars Corporation, Space Age, Mars, and colonization pages.
- Venus commonwealth date 2137 precedes stated human-rated habitability 2140.
- Olympus-class relativistic gun speed and firing/recovery figures conflict internally.
- Further detail and article summaries are in the tranche note.

### G4. Next batch
Continue with manifest entries 1201–1500 in original manifest order, all namespaces.


# Addendum H — Manifest tranche 1201–1500

Updated 2026-11-19. All 300 Bronze Wikitext files at manifest entries 1201–1500 were opened and read in original manifest order, across all namespaces. SHA-256 matched the manifest for all 300 files. This adds 290 unique verified reads (10 were already read; 25 unverified prior claims and 265 not-started records were newly verified). The ledger now records all 300 rows as `read`; detailed notes are in `research/page-notes/manifest-1201-1500.md`.

Cumulative page-ledger status after this tranche: 1538 read; 92 unverified prior claims; 1949 not started, out of 3,579. Main namespace: 269/507 read. Manifest entries 1501–1800 are next. Media visual inspection remains 0/900; no binary asset was viewed in this tranche. Continue to keep all work on `audit/continuity-research`, preserve source contradictions, and do not merge or open a PR without user approval.
