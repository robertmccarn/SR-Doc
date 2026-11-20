# Dependency reconciliation — alias and redirect pass 1

Date: 2026-11-20  
Branch: `audit/continuity-research`  
Source: uploaded `SR-Doc-Audit.zip`; Bronze manifests and captured Wikitext were read-only.

## Scope

This pass follows completion of the initial cross-reference of all 900 media-manifest records. It examined the relationship between the 900 media records, all File-namespace page records, and the extracted `images` metadata from all 3,579 page records. It also independently scanned raw Wikitext for explicit `[[File:...]]` / `[[Image:...]]` links and inspected literal filename mentions for assets without exact extracted references.

## File-namespace reconciliation

- The page manifest contains **906 File-namespace pages**.
- The media manifest contains **900 records**; all 900 asset `page_id` values resolve to a File-namespace page.
- Six File-namespace pages are not represented as media-manifest assets:
  - `File:Example.jpg` (page ID 32), a non-redirect file description page; this title appears in extracted image metadata 19 times, mainly template documentation/examples.
  - `File:Communitylogo.png` (page ID 44), empty captured source.
  - `File:Wiki.png` (page ID 45), empty captured source.
  - `File:180px-Gerald Ford.jpg` (page ID 288), redirect to `File:Gerald Ford.jpg`.
  - `File:465px-William McKinley 1.png` (page ID 289), redirect to `File:William McKinley 1.png`.
  - `File:Eagle 7 Booster.png` (page ID 1153), redirect to `File:Eagle 9 Booster.png`.

The six-page difference is therefore not simply six missing binary downloads: it includes three redirects and three other File pages. The three redirect source titles should be retained as aliases when resolving historical references. Their target availability and rendering behavior have not been independently proven by this pass.

## The 141 image titles absent from the media manifest

The extracted `images` arrays contain **141 distinct image titles** that do not exactly match any of the 900 media-manifest titles.

Reference-source distribution for these 141 titles:
- 128 are referenced only from namespace 10 (Template).
- Five are referenced only from namespace 828 (Module).
- Three are referenced only from main namespace (namespace 0).
- Two are referenced from both Template and Module namespaces.
- One is referenced only from User namespace (namespace 2).
- One is referenced only from Thread namespace (namespace 1201).
- One is the File-namespace page `File:Example.jpg` itself.

This distribution shows why the 141-title difference cannot be treated as 141 missing article images. Much of it represents generic template/module dependencies, template documentation, and placeholder/example assets. The most frequently referenced title is `File:Placeholder` (63 references, primarily user pages); `File:Example.jpg` has 19 references; `File:Flag placeholder.svg` has five.

Notable template/module dependencies include `Ambox warning orange.svg`, `Imbox content.png`, `Missing map.svg`, `Lua-logo-nolabel.svg`, `Example.png`, and multiple generic election/country-infobox images. These are dependencies of the captured template/module corpus, not automatically evidence of visible use in a specific article.

## Independent raw-Wikitext check

A separate scan for explicit `[[File:...]]` and `[[Image:...]]` links found:
- 441 distinct media-manifest titles explicitly linked in raw Wikitext.
- 749 explicit-link occurrences for those titles.
- None of the 108 assets without an exact extracted `images` reference had an exact normalized explicit File/Image wikilink in the captured raw corpus.

This does not contradict the 792 exact extracted references: extracted metadata can reflect parser/template expansion and other dependencies that are not present as literal wikilinks in the individual raw source. Conversely, raw template parameters and aliases may identify dependencies without being explicit wikilinks.

## Eleven assets with literal mentions but no exact extracted reference

The 11 previously identified literal-only cases are not all equivalent:
- `File:Flag of Taiwan.png`: filename occurs in two main-namespace pages, but surrounding context points to an infobox image parameter and a blank image parameter; country-data templates use `Flag_of_Taiwan.png` conventions elsewhere. Do not assume it is the rendered flag.
- `File:Vietnam.png`: literal in `Template:Country data Vietnam` only as a flag alias in an older naming convention; the actual configured alias is `Flag_of_Vietnam.png`. Also occurs in a portal image module as part of a different filename (`Map of Vietnam.png`), which is not an exact file dependency.
- `File:Sudan.png`: occurs in Sudan and South Sudan country-data templates, but those templates specify `Flag_of_Sudan.png` and `Flag_of_South_Sudan.png`.
- `File:Chile.png`: country-data template specifies `Flag_of_Chile.png`.
- `File:Bolivia.png`: country-data template specifies `Flag_of_Bolivia.png`.
- `File:Xanthe Flag.png`: country-data template explicitly sets this as Xanthe's `flag alias`; this is the strongest actual alias/dependency lead in this group, but rendered use is still unverified.
- `File:Flag of Russia.svg`: appears in `Module:Portal/images/r` as a portal image mapping.
- `File:Flag of Venezuela.png` and `File:The Chinese Civil War.png`: appear only in Thread/comment welcome text linking to file pages.
- `File:K8ch1z55ucnz.png`: appears only in a Thread/comment welcome message; it is the one missing/failed binary asset already identified in the media audit.
- `File:Trump.jpg`: occurs in the President of the United States page inside a CSS image-crop parameter that names `Donald_Trump.jpg`; this is not an exact filename match and is not proof that `Trump.jpg` is used.

## Interpretation and limitations

1. Extracted `images` metadata is not a rendered dependency graph. Template documentation and module dependencies can be included.
2. The 141 titles without manifest counterparts are not confirmed missing files. Many are template/module dependencies; some may be intentionally external or unresolved.
3. Literal filename mentions are not necessarily dependencies. A mention may be prose, a Thread welcome link, an obsolete alias, or a substring of another filename.
4. An exact filename match in a template parameter is a stronger lead than a prose mention, but still does not prove a particular article rendered that file.
5. This pass did not execute the wiki parser, resolve all template expansions, or verify current remote file availability.
6. Bronze assets and manifests were not modified.

## Updated working model

Use three separate inventories going forward:
- **Captured media inventory:** the 900 records in the asset manifest.
- **File-page/alias inventory:** all 906 File-namespace page records, including redirects and pages without media records.
- **Page dependency inventory:** the extracted 933 distinct image titles, including 141 titles outside the captured media manifest.

The next useful pass is targeted resolution of the 141 external dependency titles and the 108 assets without exact page references, prioritizing template alias chains and main-namespace article references. Keep unresolved cases explicit rather than inferring orphan status.
