# RAG source-aware infobox claims — pass 001

**Status:** Extractor, claim schema, and conservative comparison CLI committed. The committed CLI and regression tests still require runtime execution against the pinned archive.
**Scope:** Main namespace (507 captured pages), pinned Bronze/Silver archive SHA-256 `d1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8`.
**Evidence class:** Derived parser probe plus direct source-locator observations. No canon adjudication.

## Implementation

- `extract_infobox_claims.py` extracts one derived record per raw infobox parameter, retaining page ID/title, namespace, revision, capture/archive hash, source path/hash, exact template name, invocation ID and character range, parameter name/index, unmodified raw parameter value, value character range, linked wikilink targets/display text/offsets, and provenance locators.
- `infobox-claim.schema.json` defines the claim record. Optional `event_scope_id` is reserved for an explicit reviewed annotation; the extractor does not infer or populate it.
- `evaluate_infobox_claims.py` compares only claims sharing the same page ID, an explicit shared `event_scope_id`, template family, and exact normalized parameter name. It emits a review candidate, not a verdict.
- Repeated parameters without explicit event-scope annotation are reported under `unresolved_comparisons`, not called conflicts. A repeated parameter may encode multiple roles, appointments, or values rather than contradictory claims.

## Parser development probe

A local parser-equivalent scan of the pinned archive, with brace-stack-aware matching for nested templates and triple-brace parameters, found:

- 507 main-namespace pages scanned.
- 143 infobox invocations across the observed infobox template families.
- 4,381 parameter candidates.
- Two repeated-parameter groups with distinct values and no established event scope.

These figures are development-probe results, not output from an execution of the committed CLI. The committed extractor/evaluator and regression tests have not yet been run in the current environment.

## Unresolved repeated-parameter observations

1. **Page 636 — United States presidential election, 2132**
   - Revision: `11287`
   - Source: `bronze/pages/636/11287.wikitext`
   - Source SHA-256: `b4f05da845c07de15f11ef3fe1d01ad952317ec9c798aebfc527a5c695d99bb2`
   - Template: `Infobox election`
   - Parameter: `office`
   - Values at character ranges `733–754` and `996–1012`: `Chairman of the ITC`; `Vice President`.
   - Interpretation: observed duplicate parameter values. They may describe separate offices; event scope is not established. Do not label them contradictory.

2. **Page 1343 — Joseph Loveridge**
   - Revision: `8656`
   - Source: `bronze/pages/1343/8656.wikitext`
   - Source SHA-256: `df452d37f70f684303de486610c1b76d9399180e46605ba3fd48780030bbaca9`
   - Template: `Infobox officeholder`
   - Parameter: `order`
   - Values at character ranges `115–149` and `156–161`: `[[United States Space Force|1st]]`; `39th`.
   - Interpretation: observed duplicate parameter values. They may refer to distinct offices/roles; event scope is not established. Do not label them contradictory.

## Explicit non-comparison example

Page 1413, **Second Chinese Civil War**, contains:
- Infobox parameter `date`: `2027-2048`.
- A date-like string `2105-2111` inside parameter `combatant1`.

These are different parameter names and therefore different field meanings under the current contract. The extractor retains both raw values and offsets, but the evaluator must not compare them as if they were competing values for the same field. The existing date-bearing contrast retriever may still surface the passage as a review lead; it does not establish a contradiction.

The separate page 1408, **Third Chinese Civil War**, is a different page subject. No cross-page comparison is performed without explicit subject/entity equivalence and event-scope alignment.

## Limitations and next steps

- Execute the committed extractor on the pinned ZIP; compare its report to the development probe.
- Run `test_infobox_claims.py` and record exact output.
- Review the two unscoped duplicate-parameter groups in source context.
- Decide whether any reviewed, source-supported event-scope annotations are warranted; do not infer them from page proximity or matching date patterns.
- Complete reviewed source passages, page IDs, answer criteria, and abstention expectations for all 20 RAG evaluation cases.
- Measure retrieval and candidate-comparison quality before adding embeddings.

No Bronze/Silver source bytes, manifests, lore canon, or generated binary index were modified.
