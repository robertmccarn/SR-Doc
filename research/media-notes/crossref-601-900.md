# Cross-corpus media reconciliation — manifest entries 601–900

## Scope and method

Compared media-manifest entries 601–900 against the extracted `images` metadata for all 3,579 captured Wikitext records. For assets absent from that metadata, searched all raw Wikitext for the filename and space/underscore variants.

Three classifications are kept separate:
1. **Exact extracted reference** — exact `File:` title appears in a page record's `images` array.
2. **Literal/template/thread mention only** — no exact extracted reference, but filename text occurs in raw Wikitext.
3. **No discovered reference** — neither an exact extracted reference nor a literal filename mention was found.

The `images` array is an extracted index, not a rendered dependency graph. Template/module aliases and parser omissions may affect results. A literal mention may be a talk/thread comment, example, stale text, or data mapping and is not proof of visible use.

## Results

- Media records examined: **300**.
- Exact extracted page-image references: **240/300 (80.0%)**.
- Assets absent from extracted `images` metadata: 60.
- Of those 60, **four** have a raw filename mention; **56** have no discovered literal filename mention.
- The 240 exact matches account for **295 asset-to-page references**.
- Reference multiplicity: 205 assets referenced by one page; 22 by two; nine by three; three by four; and one by seven.

## Assets without exact extracted references

### Literal/thread mentions only (4)

| Manifest index | Asset | Raw source mention | Interpretation |
|---:|---|---|---|
| 765 | `File:Flag of Venezuela.png` | `Thread:ItVaries/@comment-32769624-20190304143214` (page 3132) | Thread/comment mention only |
| 767 | `File:The Chinese Civil War.png` | `Thread:B-Tank/@comment-32769624-20190411044617` (page 3184) | Thread/comment mention only |
| 815 | `File:K8ch1z55ucnz.png` | `Thread:MUHAM3441M/@comment-32769624-20201116131412` (page 3527) | Thread/comment mention only; the archive has no physical binary for this failed manifest record |
| 823 | `File:Trump.jpg` | `President of the United States` (page 214) | Literal filename mention in page source; not present in extracted image metadata |

### No discovered extracted or literal reference (56)

| Index | Asset |
|---:|---|
| 630 | `File:North american hyperloop networks by ynot1989-dc75bjb.png` |
| 632 | `File:Azawad Flag.png` |
| 634 | `File:Flag of Biafra.png` |
| 635 | `File:Flag of Arewa Republic.png` |
| 643 | `File:Brazos Flag 1.svg` |
| 655 | `File:RandPaulAgedByPhojoedotcom.jpg` |
| 658 | `File:Sherrod Brown.jpg` |
| 690 | `File:ElectoralCollege2020.svg` |
| 696 | `File:ElizabethWarren.jpeg` |
| 730 | `File:Coat of Arms of the Second Mexican Empire.svg` |
| 764 | `File:20190220 224234.jpg` |
| 766 | `File:Joe P Kennedy III.jpg` |
| 812 | `File:American flag with 5 stars..png` |
| 813 | `File:Screen Shot 2020-10-26 at 3.04.09 PM.png` |
| 816 | `File:K8ch1z55ucnz (1).png` |
| 817 | `File:220px-Joe Biden official portrait 2013 cropped.jpg` |
| 818 | `File:V5xoftjt8i901.png` |
| 819 | `File:Alexandria Ocasio-Cortez.png` |
| 821 | `File:Download.jpg` |
| 822 | `File:3500.jpg` |
| 824 | `File:KamalaHarrisPoint.jpg` |
| 825 | `File:2024electoralmap.png` |
| 827 | `File:Kamala Harris Vice President.jpg` |
| 830 | `File:40B28EA5-B8C7-4D21-BA45-2DB4A95CE904.jpeg` |
| 835 | `File:Site-logo.png` |
| 836 | `File:Site-favicon.ico` |
| 850 | `File:US Flag 5 Stars.png` |
| 852 | `File:Hong Kong flag.png` |
| 870 | `File:Yooper Flag.gif` |
| 871 | `File:American Hispanic Flag.jpeg` |
| 872 | `File:Autism Pride Flag.png` |
| 873 | `File:Autism Speaks.png` |
| 874 | `File:Native American Flag.gif` |
| 875 | `File:New Africa Flag 2.png` |
| 876 | `File:American Muslim Flag.png` |
| 877 | `File:New England Flag.png` |
| 878 | `File:Lakota.png` |
| 879 | `File:Cascadia Flag.png` |
| 880 | `File:Islam flag.png` |
| 881 | `File:Iroquois Flag.png` |
| 882 | `File:Rainbow Progress.webp` |
| 883 | `File:Canadian Muslim Rainbow Pride Flag.jpeg` |
| 884 | `File:IMG 2233.png` |
| 885 | `File:Blackfoot flag.jpeg` |
| 886 | `File:Palestine flag.png` |
| 887 | `File:California Seperatist Flag.jpeg` |
| 888 | `File:IMG 2240.jpeg` |
| 889 | `File:Free Texas Militia.jpeg` |
| 890 | `File:Socialist Red Star.png` |
| 891 | `File:Free Vermont.png` |
| 892 | `File:IMG 2244.png` |
| 893 | `File:Nikki Haley Official portrait.jpg` |
| 897 | `File:2026 Senate Election Map.jpg` |
| 898 | `File:2026 Senate.jpg` |
| 899 | `File:2025 senate.jpg` |
| 900 | `File:2026 (pre-flood) GOP extent of support.jpg` |

This list includes likely site chrome (logo/favicon), election and portrait images, flags, and screenshots. The lack of a captured reference does not establish that any is an orphan; the reference may be indirect, historic, or outside the extracted dependency fields.

## Useful reference patterns

- `File:Flag of Croatia.png` (index 627) has seven references, spanning country/geopolitical infobox templates and documentation, Intermarium, Allies of World War III, and Population growth. Template/documentation hits should not be mistaken for seven independent article uses.
- `File:Alexandria Ocasio-Cortez Official Portrait.jpg` (index 826) appears in President of the United States, United States presidential election, 2032, and Alexandria Ocasio-Cortez.
- `File:Hong Kong China Flag.png` (index 853) appears in Third Chinese Civil War, Second Chinese Civil War, Hong Kong, and a user page.
- `File:Christian Separatist Flag.png` (index 631), `File:Confederate-rebel-flag.png` (index 837), `File:SCA Flag (2030-2031).png` (index 857), and `File:Northwest Territorial Imperative flag.png` (index 858) are each shared by several political/ideological pages. This is a lead for cross-page visual consistency review, not evidence of an error.

## Cumulative progress

Across all 900 media-manifest records:
- Exact extracted references: **792/900**.
- Raw/template/thread mentions without exact extracted reference: **11**.
- No discovered reference: **97**.
- Exact-reference asset-to-page edges: **1,696** (876 + 525 + 295).

The 792/900 exact references reconcile exactly with the earlier first-pass corpus-wide title comparison. The remaining 108 split into 11 raw mentions and 97 with no discovered literal mention. This classification is still not a rendered-use/orphan determination.

## Next phase

The initial asset-to-page pass now covers all 900 media records. Next: reconcile redirects and filename aliases, expand template/module dependencies where feasible, compare file-description pages and article context, and inspect high-impact/no-reference assets. Then synthesize confirmed discrepancies separately from unresolved leads. Preserve Bronze captures and do not merge or open a PR without approval.
