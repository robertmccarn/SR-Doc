# Targeted unmatched image dependency review — China, Al-Hasa, and main page

Date: 2026-11-20  
Branch: `audit/continuity-research`  
Source: Bronze page manifest and raw Wikitext from `SR-Doc-Audit.zip`; read-only inspection.

## Scope

Inspected the four pages associated with the three unmatched main-page image titles identified in dependency reconciliation pass 1:
- `Al-Hasa`
- `Federal Republic of China`
- `United Federation of China`
- `Second Renaissance Wikia`

Checked each page's extracted `images` metadata against its raw Wikitext, then checked whether each title has a corresponding media-manifest record or File-namespace page.

## Findings

### 1. `File:Blank.png` — Al-Hasa

The Al-Hasa infobox contains:
```wikitext
| image_map =
| image_map_caption =
```
The extracted image metadata nevertheless lists `File:Blank.png`. The page does not explicitly assign Blank.png to the map field. The page also has an ordinary Saudi Arabia flag assignment.

**Assessment:** This is likely a placeholder/template/parser artifact associated with an empty infobox image field, not evidence that Al-Hasa has a missing map asset. There is no matching media record or File page in the supplied archive. Do not classify this as a confirmed missing map.

### 2. `File:Republic of China (orthographic projection historical).svg` — Chinese state succession

Both pages explicitly assign the same image to the `image_map` parameter:

- **Federal Republic of China** (2108–2139): caption says the map shows the location and maximum extent of the territory claimed by the Federalist government.
- **United Federation of China** (2058–2108): caption says the map shows the location and maximum extent of the territory claimed by the Republic of China.

The title is absent from the 900-record media manifest and there is no matching File-namespace page in the captured page manifest.

**Assessment:** This is a genuine intended map dependency in the source, not a template placeholder. The missing binary means the map's visual content cannot be verified from this archive. Since it is reused across successive Chinese polities and its captions describe territorial claims, it is a high-priority continuity asset. The reuse may be intentional, but it also raises a question: does one historical map accurately represent both states and both periods, or is the map intended as a common baseline? The source alone does not settle that question.

### 3. `File:Slider` — Second Renaissance Wikia main page

The main page contains:
```wikitext
<gallery type="slider">
Slider
SR_Timeline.png|link=Timeline|linktext=Chronology of Events
...
</gallery>
```
The bare `Slider` line is inside the gallery configured with `type="slider"`. It is not written as a `File:` link, and there is no matching media record or File page.

**Assessment:** Treat this as gallery syntax/configuration or a parser-specific marker, not as a missing image filename. It should be excluded from missing-media counts unless a renderer-specific investigation proves otherwise.

## Updated interpretation of the three main-namespace unmatched titles

- `Blank.png`: likely empty-field placeholder artifact; no direct image assignment in Al-Hasa source.
- `Republic of China (orthographic projection historical).svg`: explicit, reused map dependency on two consequential Chinese state pages; binary absent from this archive.
- `Slider`: gallery marker/configuration token, not a conventional file dependency.

This demonstrates why raw page-context inspection is necessary before classifying unmatched extracted image titles.

## Continuity implications for follow-up

1. Locate or reconstruct the intended China map only if another source capture or authorized external source is available; do not invent its geography from the filename.
2. Compare the map's intended territorial scope against the two article captions and the 2058/2108/2139 state chronology once the visual asset is recovered.
3. Review the China succession chain and the articles' conflicting historical-era fields in a separate chronology audit; this pass does not resolve those content issues.
4. Keep `Blank.png` and `Slider` out of confirmed missing-media findings.

## Limitations

- No wiki parser/rendering environment was run.
- No remote media source was queried.
- The map's actual visual content and historical accuracy remain unknown.
- Extracted `images` metadata may include parser/template artifacts.
- Bronze source files were not modified.
