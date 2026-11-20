# Relationship matrix — semantic expansion pass 001

## Scope and result

Scanned all 507 main-namespace pages. Found 119 calls across five modeled infobox templates:
Infobox officeholder (29), Infobox Military Conflict (18), Infobox country (34),
Infobox former country (33), and Infobox political party (5).

The pass identified 113 exact linked-field candidates. Fifty-five equivalent claims were
already present in the graph; 58 new edges were added. The graph now contains 7,073 nodes
and 16,025 edges, including 116 structured infobox edges.

## New edges

| Predicate | Added | Source field |
|---|---:|---|
| MEMBER_OF | 29 | officeholder party |
| HAS_COMMANDER | 11 | military-conflict commander1..3 |
| HAS_COMBATANT | 10 | military-conflict combatant1..3 |
| HOLDS_OFFICE_IN | 5 | officeholder office |
| HAS_STATED_RESULT | 3 | military-conflict result |

## Predicates already represented

The additional extraction found 55 equivalent claims already represented, including predecessor,
successor, conflict parent, combatants, and event location. These were not duplicated.

## Evidence contract

Every new edge includes source page ID/title/path/revision, template name, exact field name,
raw parameter value, linked target title, target page ID, and target source path. Edges are
directional and marked explicit_infobox_field / structured_source_claim. Temporal scope remains
null unless independently supplied by source evidence.

## Limitations

- Only exact wikilinks resolving to existing main-namespace entity nodes are emitted.
- Plain-text values are not automatically resolved.
- Five infobox templates are modeled; 23 calls across election, government agency, company,
  military unit, and international-organization templates remain outside this pass.
- Raw Wikitext parameters are inspected; templates are not rendered/expanded.
- Infobox claims are not adjudicated canon. No transitive semantic edges are generated.
