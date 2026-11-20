# Agent navigation guide

Use this index before traversing raw wiki pages, but never treat graph topology alone as proof of a lore claim.

1. Search `ENTITY_INDEX.md` or `entity_index.json` for the canonical page candidate. Treat IDs and classifications as provisional; check aliases for ambiguity.
2. Retrieve the entity node from `relationship_graph.json` and inspect both incoming and outgoing edges. Filter by predicate and namespace.
3. Interpret each predicate according to `schema.json`. In particular:
   - `WIKI_LINKS_TO` means an explicit internal link, not an in-world relationship.
   - `CATEGORIZED_AS` means explicit wiki category membership.
   - `MENTIONS_YEAR` means a year string was extracted; it does not establish an event date.
   - Infobox-derived predicates preserve a structured source claim; they do not certify that the claim is correct or current.
4. Follow each edge's evidence locator to the cited Bronze Wikitext. Read surrounding text before answering.
5. For multi-hop questions, verify every hop independently. Do not assume transitivity (for example, a leader of a faction does not automatically control every place linked from that faction).
6. Check diagnostics for unresolved targets, alias ambiguity, missing pages, and classification limitations. Unresolved link targets may be special pages, files, templates, interwiki links, or other non-entity targets; they are not automatically broken links.
7. Keep Talk, Thread, User, and other community namespaces separate from canon claims. They can establish editorial intent or discussion, not automatically canon.
8. For Chinese political-history succession questions, also consult `../continuity/china-political-history-pass-001.md`; the known chronology conflicts remain unresolved.

## Evidence labels

- `explicit_link`: parsed internal wiki link.
- `explicit_metadata`: extracted category metadata.
- `explicit_infobox_field`: linked value in a recognized infobox parameter.
- `explicit_text_extraction`: extracted year mention only.
- `provisional`: heuristic entity classification awaiting validation.
- `source_context`: non-main namespace record retained for provenance.

When a graph edge and source prose disagree, preserve the contradiction and cite both. Never silently promote an inference to an explicit source claim.
