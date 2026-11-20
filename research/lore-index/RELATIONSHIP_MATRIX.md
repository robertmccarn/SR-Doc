# Relationship matrix

## Directional predicates

| Predicate | Direction | Meaning | Evidence requirement |
|---|---|---|---|
| `WIKI_LINKS_TO` | Page → page | Explicit internal wiki link; navigation/mention only | Parsed link target and source offset |
| `CATEGORIZED_AS` | Page → category | Explicit wiki category assignment | Silver category metadata |
| `MENTIONS_YEAR` | Entity page → year | Extracted year string; not an event date | Silver year extraction |
| `HAS_CAPITAL` | State → location | Capital named in infobox | Linked `capital` field |
| `LED_BY` | Organization/state → person | Leader named in infobox | Linked leader field |
| `COMMANDED_BY` | Event/faction → person | Commander named in infobox | Linked commander field |
| `HAS_COMBATANT` | Conflict → faction/state | Combatant named in infobox | Linked combatant field |
| `PART_OF_CONFLICT` | Conflict → broader conflict | Parent conflict/series | Linked `partof` field |
| `PART_OF` | Entity → parent | Explicit part/parent field | Linked infobox field |
| `SUCCEEDED` | Entity → predecessor | Explicit predecessor field | Linked infobox field |
| `PRECEDED_BY` | Entity → successor | Explicit successor field | Linked infobox field |
| `FOUNDED_BY` | Organization → founder | Explicit founder field | Linked infobox field |
| `HEADQUARTERED_IN` | Organization → location | Headquarters field | Linked infobox field |
| `LOCATED_IN` | Entity → location | Explicit location/country field | Linked infobox field |
| `TAKES_PLACE_IN` | Event → location | Event place field | Linked infobox field |
| `HAS_STATED_CAUSE` | Event → cause | Cause field; source claim, not adjudicated causality | Linked infobox field |
| `HAS_STATED_RESULT` | Event → result | Result field; source claim, not adjudicated outcome | Linked infobox field |
| `HAS_LARGEST_CITY` | State → city | Largest-city field | Linked infobox field |
| `MEMBER_OF` | Entity → organization | Membership field | Linked infobox field |

All edges are directional. Each edge must include an inverse predicate for reverse traversal, a `bidirectional` boolean, temporal scope when explicitly supported, certainty, evidence strength, source locator, and a retrieval weight that is not interpreted as probability.

## Hub and cross-domain matrices

Generate hub tables from graph degree, but label them as navigation hubs rather than lore importance rankings. Useful cross-domain views include Factions × Locations, Characters × Factions, Characters × Artifacts, Events × Participants, and States × Successors. Populate these views only from explicit structured claims or manually verified source claims; never infer them from co-mentions alone.

## Temporal and contradiction handling

Preserve raw date strings and source-specific claims. A year mention is not a valid-from/valid-to interval. Where two pages conflict, retain separate edges with separate evidence and flag the conflict in diagnostics. Do not merge incompatible dates into one normalized timeline.

## Known priority

The Chinese political-history audit already records unresolved civil-war and state-succession chronology conflicts. The graph is intended to expose the relevant source pages quickly, not to settle those conflicts.
