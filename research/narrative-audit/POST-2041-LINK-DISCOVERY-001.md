# Post-2041 link discovery 001

**Status:** Discovery inventory only; semantic classification pending  
**Repository:** robertmccarn/SR-Doc  
**Branch:** experiment/corrected-realism  
**Snapshot:** fdec89ff1221a36fa360630b0d7607b7c7d2f95d  
**Date:** 2026-11-25

## Method

The Bronze manifest contains 507 Main-namespace pages, including 150 redirects and 357 non-redirect pages. A whole-year, word-boundary scan of raw Wikitext identified 262 non-redirect Main pages with at least one discrete year from 2041 onward.

The same scan identified 116 non-redirect pages with at least one discrete year from 2024 through 2040 (117 if redirects are included). Eighty-two pages mention both periods, 34 mention only 2024–2040, and 180 mention only 2041 onward. Sixty-one mention neither period.

This scan excludes decade labels such as 2050s from the discrete-year count. Silver pages.jsonl may normalize decade labels to their leading year, so its years_mentioned-derived count is not directly interchangeable with this raw-text scan.

## Explicit link counts from the 262 future-dated pages

The following counts are distinct future-dated source pages that contain an explicit wiki-link to the named target page. They are useful discovery signals, not semantic or causal classifications.

| Target page | Future-dated pages linking to it |
|---|---:|
| Mars | 27 |
| The Flood | 20 |
| The Refreeze | 10 |
| Terran diaspora | 8 |
| Great Reset | 8 |
| White Tide | 8 |
| Earth Working Group | 7 |
| Revolutions of 2027 | 7 |
| Mars Corporation | 6 |
| Turkey | 5 |
| Great Famine | 4 |
| Second Chinese Civil War | 4 |
| British Republic | 3 |
| Russia | 2 |
| Caribbean annexation | 1 |
| Treaty of Odessa | 1 |

Counts overlap: a page may link to several targets. They do not establish that a link is causal, direct, or even narratively important. Cultural summaries, lists, and incidental references must be separated from true dependencies during semantic review.

## Initial dependency clusters

### Flood and climate-displacement cluster

The existing Flood reconciliation identified 37 direct dependents among 58 phrase-hit pages. The link graph additionally identifies future-dated pages that link to The Flood, The Refreeze, Earth Working Group, and related climate/political outcomes. High-priority examples already identified in source review include:
- Page 1366, Caribbean annexation, which explicitly ties 2035 annexation and displacement to Flood-era premises.
- Pages 272, 2356, and 1936, which repeat the US territorial/statehood expansion chronology.
- Pages 1106, 1637, and 1913, which the existing Flood reconciliation identified as downstream or direct dependencies.

The counterfactual question is not merely whether a page mentions the Flood. It is whether the post-2041 event still occurs if the Flood is removed, and what independent mechanism would be required to preserve it.

### Mars and space-infrastructure cluster

Mars has the largest explicit link count. The pre-2041 Mars premise is already prohibited by the realism-first timeline, including early crewed landing, mass settlement, permanent colony, and terraforming. Candidate dependents include:
- Page 1739, Terran diaspora.
- Page 1431, Arya Kanzaki and the Titan expedition.
- Page 318, Mars and terraforming.
- Page 1479, Orbital Command Stations.
- Pages 1234 and 1702, hypersonic/space weapons where related space infrastructure may be relevant.
- Later Mars, lunar, and orbital institutions not yet semantically reviewed.

Do not classify all space-related pages as Mars-dependent. Lunar infrastructure, military orbital systems, and Mars settlement may have different causal paths.

### Great Famine and Korean peninsula cluster

The future-page link graph contains four explicit links to Great Famine. The pre-2041 Korean reunification sequence is an additional dependency that may affect later Korean cultural and institutional pages even when those pages do not link directly to the famine.

Candidate pages include 1651 Korean reunification, 1715 Korea, and 3484 New Korean Wave. The famine-to-Korea chain requires independent food-security, Chinese aid, North Korean regime stability, military defection, nuclear security, and international intervention analysis.

### Russia/Eurasia cluster

The future-page link graph identifies explicit links to Russia and the Treaty of Odessa, while the broader regional chain also includes:
- Page 1683, Russia / Russian Republic.
- Page 1729, Treaty of Odessa, 2034.
- Page 1438, Eurasian Coalition, 2046.
- Page 1998, Central Eurasian Union, 2156.
- Page 97, Little Cold War, and page 88, Timeline of major events.

The sequence may be staged rather than contradictory: Union State collapse, successor-state formation, formal Russian Federation collapse, nuclear-security operations, a 2034 treaty, and a 2046 coalition. The text needs to establish the sequence and the agency/capacity of the actors.

### US political and territorial transformation

Pages 272, 2356, and 1936 repeat the 2029–2037 US territorial expansion and flag changes. Page 1366 provides a claimed causal path through Guyana, the Flood, and Caribbean displacement. The 2040 election and later presidential biographies form a separate party-system dependency cluster involving pages 1796, 1262, 1266, and 2136.

## Classification rules for the next tranche

Each page must be assigned one of the following only after semantic review:

- **Direct dependency:** the post-2041 development explicitly requires a pre-2041 event or premise.
- **Latent dependency:** the post-2041 development relies on institutions, population, infrastructure, technology, or political conditions created by a pre-2041 premise, without stating that dependency explicitly.
- **Independent:** the post-2041 development has a plausible independent causal chain that survives removal of the retired premise.
- **Unresolved:** evidence is insufficient or conflicting.

For each classification, record a counterfactual: what happens to the event if the relevant pre-2041 premise is removed?

A page is not semantically reviewed merely because it appears in this list, has a year count, or links to a target page. The 262-page inventory remains open.
