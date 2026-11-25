# RAG readiness and implementation plan

**Status:** Read-only lexical retrieval prototype implemented; exact-title/redirect lookup and date-bearing contrast retrieval are available. Source-aware infobox extraction has now been executed against the pinned archive and all emitted records passed schema and offset validation (2026-11-21). No hosted retrieval service is claimed.
**Working branch:** `audit/continuity-research`
**Goal:** Make SR-Doc usable as a portable, source-grounded retrieval corpus for ChatGPT and later applications.

## 1. Objective and success definition

Build an informal retrieval-augmented generation (RAG) workflow in which a user can ask natural-language questions about the SR-Doc universe and receive answers grounded in captured source passages, with citations, contradiction handling, and explicit abstention.

The repository—not model memory, conversation history, or the graph alone—is the knowledge authority.

Initial acceptance target:
- A manually curated set of 20 representative questions.
- At least 15 straightforward questions answered correctly with supporting primary-source passages.
- Difficult/contradictory questions correctly expose the conflict rather than inventing a resolution.
- Questions unsupported by the captured corpus result in explicit abstention.
- No fabricated citations or unsupported factual claims in the evaluated answers.

This is a proposed first gate, not a claim that the target has been achieved.

## 2. Existing assets and readiness

| Asset | Current state | RAG role | Readiness caveat |
|---|---|---|---|
| Bronze Wikitext + manifests | 3,579 captured page records; source archive supplied separately | Primary source text and provenance | Need stable, reproducible corpus ingestion into the repository or local build input |
| Silver `pages.jsonl` | 3,579 page records | Page metadata and extracted text/index seeds | Validate fields and source mapping before treating as retrieval text |
| Silver `relations.jsonl` | 11,462 parsed links | Entity/navigation discovery | Wiki links are not semantic claims |
| Silver `timeline.jsonl` | 4,447 year mentions | Temporal search leads | Year mentions are not event dates or validity intervals |
| Lore graph | 7,073 nodes; 16,025 edges in semantic pass 001 package | Entity and relationship candidate retrieval | Derived graph; 116 structured infobox edges are source claims, not adjudicated canon |
| Entity index | In graph package | Candidate entity lookup | Alias/title disambiguation remains incomplete |
| Research notes and ledgers | Existing detailed audit collection | Quality warnings, contradictions, evidence context | Not a substitute for primary lore passages |

The graph package is currently a distributed artifact, not a guarantee that the complete graph is present in the Git branch. The Bronze/Silver archive is also supplied as an external ZIP input. The ingestion process must record exact archive identity and hashes rather than assuming files are always mounted at one path.

## 3. Source authority and ingestion contract

Use the classifications in [RESEARCH-ASSISTANT-PROTOCOL.md](RESEARCH-ASSISTANT-PROTOCOL.md).

Minimum source record fields:

| Field | Requirement |
|---|---|
| `source_id` | Stable ID derived from immutable source identity; never title alone |
| `page_id` | Original captured page ID |
| `title` | Exact captured title |
| `namespace` | Numeric and/or named namespace |
| `revision_id` | Captured revision ID when available |
| `source_path` | Exact archive-relative Bronze path |
| `capture_id` | Manifest/archive identity |
| `content_sha256` | Hash of exact source bytes |
| `section_path` | Heading hierarchy or structural locator |
| `text` | Retrieval text with raw source preserved separately |
| `source_class` | Primary, structured extraction, audit, synthesis, community |
| `extractor_version` | Reproducible extraction version |
| `chunk_id` | Stable chunk identifier |
| `chunk_index` | Order within page |
| `token_or_char_range` | Original text span where available |

Do not normalize or rewrite Bronze source bytes. Derived normalized/chunked text must be a separate artifact with source offsets and transformation metadata. Preserve Wikitext constructs where their semantics matter (templates, infoboxes, links, tables, galleries, redirects).

## 4. Retrieval architecture

Start with a local, inspectable Python implementation. Avoid a hosted vector database or agent framework until measured need justifies it.

### Logical components

1. **Ingestion:** verify archive/manifest identity, parse page records, extract retrieval text, preserve source offsets and provenance.
2. **Lexical index:** SQLite FTS5 for exact titles, names, phrases, and rare terms.
3. **Semantic index:** optional local embedding index for paraphrases and concept queries.
4. **Entity resolver:** exact title/alias lookup and candidate disambiguation using page IDs, namespaces, redirects, and graph entity IDs.
5. **Graph retriever:** expand relevant entities and candidate relations, always retaining edge provenance and predicate semantics.
6. **Evidence packer:** deduplicate and rank source passages; include surrounding context, provenance, contradiction candidates, and retrieval warnings.
7. **Answer layer:** ChatGPT receives the evidence packet and follows the research assistant protocol.
8. **Verifier:** check citation existence, source/claim alignment, unsupported claims, and whether known contradictions were included.

### Initial implementation choice

- Python standard library for ingestion/orchestration where practical.
- SQLite FTS5 as the first lexical engine.
- Keep embeddings behind an interface; choose a local embedding model and vector index only after lexical baseline evaluation.
- JSONL for portable page/chunk/evidence exports.
- Existing lore graph JSON as an optional sidecar, not a mandatory dependency for simple factual lookup.
- No network service or external API required for the first local retrieval prototype.

## 5. Chunking and retrieval policy

- Prefer page-level records plus section-aware chunks. Keep a page summary/metadata record linked to its chunks.
- Do not split infoboxes, list entries, tables, or short sections in ways that detach values from their labels.
- Preserve title, section path, namespace, page ID, revision, source path, and chunk offsets on every chunk.
- Use overlapping chunks only where necessary; retain stable source offsets.
- Retrieve by a hybrid strategy: exact title/name and FTS lexical results first, semantic candidates second, graph expansion third.
- Rerank by source relevance, entity match, temporal relevance, source class, and passage completeness. Do not rank audit synthesis above primary evidence for a lore claim.
- Retrieve contradiction candidates by searching alternate dates/names and related pages, not just nearest-neighbor similarity.
- Return enough context to understand qualifiers, negation, table headers, and infobox parameter names.
- Never use a generated summary as the only citation target.

## 6. Evidence packet contract

The retrieval layer should return a versioned JSON object conceptually shaped as:

```json
{
  "schema_version": "1.0",
  "question": "user question",
  "resolved_entities": [],
  "retrieval": {
    "indexes_searched": [],
    "corpus_snapshot": "capture id and hashes",
    "warnings": []
  },
  "evidence": [
    {
      "evidence_id": "stable id",
      "source_class": "primary",
      "page_id": "original id",
      "title": "exact title",
      "namespace": "Main",
      "revision_id": "if available",
      "source_path": "archive-relative path",
      "content_sha256": "sha256",
      "section_path": [],
      "text": "verbatim or faithfully extracted passage",
      "locator": "heading/field/offset",
      "chunk_id": "stable chunk id"
    }
  ],
  "candidate_relationships": [],
  "contradiction_candidates": [],
  "unresolved_questions": []
}
```

The packet is evidence transport, not a final truth judgement. The answer model must retain the source classifications and limitations.

## 7. Evaluation set and metrics

Create a versioned evaluation set with at least these categories:

| Category | Initial target | What it tests |
|---|---:|---|
| Direct page fact | 5 | Exact retrieval and citation |
| Entity/alias resolution | 3 | Titles, redirects, aliases, ambiguous names |
| Timeline/chronology | 3 | Date extraction and temporal qualification |
| Relationship question | 3 | Graph-assisted discovery without semantic overclaim |
| Contradiction detection | 3 | Retrieval of competing claims |
| Unanswerable/absence | 3 | Correct abstention and search-coverage wording |
| **Total** | **20** | |

Record for each case: question, expected evidence page IDs, expected answer elements, known pitfalls, acceptable uncertainty, and expected abstention status.

Measure:
- **Evidence recall@k:** expected supporting source records retrieved in top k.
- **Citation precision:** cited passages actually support their associated claims.
- **Claim support rate:** factual answer claims with direct evidence or explicit inference labels.
- **Contradiction recall:** known conflicting source claims retrieved and disclosed.
- **Abstention quality:** unsupported questions are not answered as fact.
- **Entity resolution accuracy:** correct page/entity selected.
- **Retrieval coverage:** indexes, namespaces, and corpus snapshot actually searched.

Do not report a reliability percentage until the test set is fixed and answers are scored against reviewed evidence.

## 8. Phased implementation

### Phase 0 — Governance and contracts (this pass)
- [x] Define the research assistant answer protocol.
- [x] Define the source/retrieval architecture and evidence packet.
- [x] Define evaluation categories and initial acceptance target.
- [x] Add machine-readable schema and evaluation cases.
- [x] Review and validate the supplied source archive structure, hashes, and ingestion inputs.

### Phase 1 — Corpus preparation
- [x] Inventory required Bronze/Silver archive paths and manifests; read-only validator committed at `validate_archive.py`.
- [x] Verify supplied archive SHA-256, manifest counts, page source paths/hashes, and Silver JSONL structure; result: `archive-validation-001.json`.
- [ ] Verify and document any additional source snapshot inputs (for example, separately distributed graph package) before indexing.
- [ ] Verify archive hash and source counts at ingestion time.
- [x] Produce stable section-aware chunk JSONL with page/revision/source hash/namespace/section/character-offset provenance.
- [x] Preserve original source bytes and hash linkage; source archive remains unchanged.
- [x] Validate chunk ID uniqueness, full page metadata coverage, FTS row parity, and source mapping. 3,092 pages have text chunks; 487 captured records have no non-whitespace text, including three empty main-namespace pages.

### Phase 2 — Lexical retrieval baseline
- [x] Build SQLite FTS5 database from prepared chunks.
- [x] Implement exact page-ID lookup and title/section/body lexical search. Exact title and explicit redirect lookup are available through `--title`.
- [x] Return source passages with stable page/revision/hash/path/section/character-offset citations.
- [x] Add CLI search command that emits evidence packets conforming to schema 1.0.
- [x] Test exact-name/phrase retrieval and page-ID lookup against known corpus passages.
- [x] Add exact title-key and captured Wikitext redirect resolution; redirect targets remain explicit mappings, not entity merges. Initial retrieval benchmark pass 001 is complete; answer-generation and citation scoring remain outstanding.

### Phase 3 — Graph-assisted and semantic retrieval
- [ ] Load the versioned graph package as optional sidecar.
- [ ] Implement entity resolution and bounded graph expansion.
- [ ] Add embeddings only if evaluation shows lexical retrieval gaps.
- [x] Add a first-pass date-bearing contrast mode that diversifies lexical results across pages and flags multiple year ranges in one passage as review candidates. This is retrieval support, not semantic contradiction adjudication.
- [x] Add source-aware infobox parameter extraction and a conservative comparison CLI that requires explicit reviewed event-scope alignment in addition to subject/template/field matching.
- [x] Run the five committed parser/comparison regression tests in GitHub Actions (Python 3.11.18); all passed on 2026-11-21.
- [x] Execute the committed extractor against the pinned archive and validate emitted records against the claim schema; 4,381/4,381 records passed, with deterministic output and zero offset/provenance mismatches. See `infobox-claim-validation-001.json`.
- [ ] Preserve predicate direction and edge provenance.

### Phase 4 — ChatGPT workflow
- [ ] Define a repeatable handoff format for evidence packets.
- [ ] Add Project-level assistant instructions using the protocol.
- [ ] Ensure each answer is based on the supplied evidence packet or explicitly reports unavailable retrieval.
- [ ] Validate citations and abstention behavior manually.

### Phase 5 — Evaluation and iteration
- [x] Draft source-reviewed expected evidence page IDs, locators, answer elements, pitfalls, and abstention expectations for all 20 cases; maintainer approved this baseline on 2026-11-21.
- [x] Independently verify all ten source-page identities, 51 cited locator/content ranges, and seven exact-title/map-boundary checks against the pinned archive; correct Q16/Q17 locators. Maintainer approval received.
- [x] Score initial retrieval page recall, passage-locator coverage, exact-title/redirect resolution, and exact-title abstention; results and limitations are recorded in `retrieval-benchmark-pass-001.json`.
- [x] Draft and manually score 20 source-grounded answer outputs for answer-key coverage, citation/provenance, contradiction disclosure, and abstention; 20/20 met the approved answer criteria. This was manual source review, not CLI-generated answer evaluation or independent scoring. See `answer-generation-pass-001.md`.
- [ ] Fix corpus/chunk/retrieval failures before tuning prompts.
- [ ] Record failure examples and regression tests.
- [ ] Expand only after the initial acceptance target is met.

## 9. Risks and controls

| Risk | Control |
|---|---|
| Model fills gaps from pretrained knowledge | Lore-only mode; evidence packet; abstention |
| Graph edge mistaken for canon | Require source passage and predicate semantics |
| Similar names merged incorrectly | Exact ID/title first; aliases remain candidate mappings |
| Contradiction hidden by top-k retrieval | Dedicated contradiction search and benchmark cases |
| Chunk loses context | Section-aware chunking and parent-page context |
| Stale or mixed snapshots | Corpus snapshot ID, source hashes, versioned indexes |
| Missing files/partial archive | Ingestion validation and retrieval warnings |
| Research notes treated as lore | Source-class metadata and ranking policy |
| Citation points to wrong passage | Stable locators and citation verification |
| Embeddings add complexity without value | Lexical baseline first; measured adoption |

## 10. First implementation tasks

The first coding unit is implemented as `validate_archive.py`; it accepts an explicit archive path and optional report-output path, and is read-only. It:
1. Computes and records the archive SHA-256.
2. Checks required Bronze manifest and Silver JSONL members, normalized ZIP path collisions, unique page IDs, expected manifest/JSONL counts, and JSONL parseability.
3. Enumerates all page-manifest source paths and recomputes SHA-256 for each captured Wikitext file.
4. Emits a machine-readable inventory report without modifying the archive.
5. Exits nonzero on missing members, malformed records, duplicate IDs/paths, source hash mismatches, or count mismatches.

The archive validator does not yet validate the separate graph package or deeply validate every Silver field schema. The chunk builder pins the expected archive SHA-256 and fails on mismatch unless explicitly overridden.

The section-aware chunker and FTS5 lexical baseline are now implemented. Next: alias/redirect resolution, retrieval evaluation, and contradiction-oriented retrieval. Do not build embeddings before the lexical baseline is measured.

### Rebuild and search

From the repository root, with the validated source archive available locally:

```powershell
python research/rag/build_index.py .\\SR-Doc-Audit.zip --chunks chunks.jsonl --db srdoc_fts5.sqlite --report chunk-build-report.json
python research/rag/search.py "Third Chinese Civil War 2105" --db srdoc_fts5.sqlite -k 8 --json
```

The builder rejects a different archive hash by default. Use `--allow-unpinned-archive` only when intentionally indexing a new snapshot, and retain its new build report. Search defaults to namespace 0; use `--include-context` only when editorial/community context is deliberately wanted. Retrieve a known page with `--page-id 1408 --db srdoc_fts5.sqlite --json`.

## 11. Initial corpus and lexical baseline results

- Archive SHA-256: `d1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8`.
- Page metadata rows: 3,579; text chunks: 7,598; unique chunk IDs: 7,598; FTS rows: 7,598.
- Pages with non-whitespace source text: 3,092. Captured records without text chunks: 487; three are main-namespace pages with zero-byte Wikitext (`New Lion City`, `Lakota Republic`, `Vietnam`). Other zero-text records are largely File and Message Wall pages. Their page metadata remains searchable by page ID in the index.
- Default lexical search is restricted to namespace 0. `--include-context` is required to search all namespaces; explicit page-ID retrieval can retrieve any namespace. This prevents Talk/Thread/User material from silently entering ordinary lore answers.
- Test query `Third Chinese Civil War 2105` returned the source page and section passages, including `First period of war (2105-2111)`; page-ID lookup for 1408 returned its ordered passages. This is a smoke test, not a benchmark score.
- Build output is packaged as `SR-Doc-RAG-Index-001.zip`; detailed counts are in `chunk-build-report-001.json`.

## 13. Answer-generation and citation evaluation — pass 001

- Added `answer-generation-pass-001.md` with source-grounded outputs for all 20 maintainer-approved questions.
- Manual scoring: 20/20 answer-key criteria met; 20/20 cases include source/evidence citations; 4/4 contradiction-disclosure cases handled; 3/3 required abstention/qualified-absence cases handled; no unsupported factual claims were identified in the same-pass review.
- These are manual answer-key compliance results, not a runtime test of model generation from CLI evidence packets. The answers were composed from the benchmark's retrieved page IDs plus full-page expansion and direct Bronze source review. Automated citation precision and independent claim-support scores remain unmeasured.
- The retrieval benchmark's source-equivalent reconstruction caveat remains open. Next: run exact committed index/search Git blobs against the pinned archive, regenerate evidence packets, then add a separate answer-generation runtime and independent/blind scoring pass.
- Do not change the approved 20-case baseline based on this pass.

## 12. Definition of done for the initial prototype

The prototype is ready for informal use only when:
- the source archive and snapshot are identified reproducibly;
- all indexed chunks map back to exact source pages and offsets;
- query results show supporting passages and provenance;
- the assistant protocol is available at answer time;
- unsupported questions abstain;
- contradiction tests surface competing evidence;
- the 20-case evaluation is scored and its limitations documented.

This plan describes intended work. A checked box means the artifact or decision exists in the repository; it does not imply runtime functionality or a passing evaluation unless explicitly stated.


## 10. Exact title and redirect resolution — pass 001

- Added `build_alias_index.py`, a post-build step that reads the immutable archive manifest and raw redirect source text, then creates a `title_keys` table in SQLite. It stores normalized exact-title keys, original title/page IDs, redirect target title, resolved target page ID (only when unique), and resolution status.
- Normalization is deliberately narrow: underscores become spaces, repeated whitespace is collapsed, and matching is case-insensitive. No fuzzy matching, namespace guessing, synonym inference, or entity consolidation.
- Added `--title` to `search.py`. Exact title lookup returns its page; a captured redirect returns target-page evidence while retaining redirect source page ID/title in `resolved_entities.via_*`. Ambiguous and unresolved targets are not silently selected.
- Build after base index: `python research/rag/build_alias_index.py SR-Doc-Audit.zip --db srdoc_fts5.sqlite`. Example: `python research/rag/search.py --title "Main Page" --db srdoc_fts5.sqlite --json`.
- Local archive test: 3,579 title-key rows and 3,575 distinct normalized titles; 83 redirects uniquely resolved, 101 unresolved, one ambiguous. Smoke tests: Main Page → Second Renaissance Wikia (84→2); File:180px-Gerald Ford.jpg → File:Gerald Ford.jpg (288→285); exact Third Chinese Civil War → page 1408; unknown title abstains.
- Limitations: first direct `#REDIRECT [[target]]` only. No redirect chains, fragments, namespace aliases, interwiki redirects, malformed syntax recovery, fuzzy matching, or automatic entity merging. Non-main namespace results are labelled context. No Bronze/Silver source bytes changed; SQLite remains a generated artifact.


## 13. Contrast retrieval — pass 001

- Extended `search.py` with `--contrast`. It retrieves a larger lexical candidate pool, first diversifies by page, then includes additional date-bearing passages within the result limit. Each evidence record carries heuristic `date_signals` extracted from the returned passage.
- The first candidate detector flags passages containing multiple distinct year ranges and groups multiple date-bearing chunks from the same page. These are explicitly marked `requires_source_review`, `multiple_date_ranges_single_passage`, or `intra_page_date_variance`; the detector does not claim that differing dates are semantically incompatible and never adjudicates which source is correct.
- Test case: `Second Chinese Civil War 2027 2048 2105 2111` retrieves page 1413 and its lead passage containing both `2027-2048` and `2105-2111`. This exposes the already-audited infobox inconsistency for review.
- Added `test_search.py`; four regression checks passed locally against the uploaded version-002 SQLite index: exact title/page identity; same-passage competing year-range candidate; default main-namespace restriction; explicit context opt-in.
- Limitations: lexical OR retrieval can return loosely related pages; date regex is heuristic and does not parse infobox field labels or distinguish event dates from publication dates. Candidate recall/precision has not been benchmarked. No reliability percentage is claimed.
- Example: `python research/rag/search.py "Second Chinese Civil War 2027 2048 2105 2111" --contrast --db srdoc_fts5.sqlite -k 16 --json`.
- No Bronze/Silver source bytes or canon pages changed. The local SQLite database remains a generated artifact; no binary DB is committed.


## 14. Source-aware infobox claims and conservative comparison — pass 001

Added:
- `extract_infobox_claims.py` — read-only Bronze ZIP extractor. It verifies the pinned archive identity and each selected page's manifest SHA-256, defaults to namespace 0, and emits one JSONL record per infobox parameter.
- `infobox-claim.schema.json` — portable schema for the derived claim record.
- `evaluate_infobox_claims.py` — compares values only when page ID (subject), an explicit reviewed `event_scope_id`, template family, and exact normalized parameter name (field meaning) all match. Repeated parameters without explicit event-scope annotation are retained as unresolved comparison groups, because they may represent distinct roles/events or multi-valued fields. It never adjudicates them.
- `test_infobox_claims.py` — parser and comparison regression tests covering nested templates, nested parameter syntax, wikilink pipes/offsets, namespaced infobox templates, and scope gating.
- `infobox-claim-validation-001.json` — committed-source execution report for the pinned archive, JSON Schema validation, exact offset/provenance checks, deterministic repeat run, and conservative evaluator output.

Each claim retains original page ID/title, namespace, revision, archive SHA-256, source path and SHA-256, exact infobox template name, template invocation ID and character range, exact parameter name/index, raw parameter value, value character range, linked wikilink targets/display text and their offsets, and explicit provenance locators. The raw value is not normalized in the output.

Comparison is deliberately narrower than date-pattern matching. A `date` parameter and a date-like string embedded in `combatant1` are different fields and are not compared. Claims from different page subjects are not compared without an explicit entity-equivalence mapping. The extractor does not infer event scope: only a reviewed `event_scope_id` permits candidate comparison. Repeated parameters without that annotation are reported as unresolved, not as conflicts. Candidate conflicts require source review; no canonical value is selected.

Committed runtime verification is complete for the pinned snapshot: the exact committed extractor emitted 4,381 claims from 507 main-namespace pages and 143 infobox invocations; all 4,381 records passed the claim schema, raw-value and linked-entity offsets, template bounds, and source-provenance checks. A second run was byte-identical. The evaluator found zero scoped candidate conflicts and retained the two repeated-parameter groups (page 636 `office`; page 1343 `order`) as unresolved. See `infobox-claim-validation-001.json` and `infobox-claims-pass-001.md`.

The 20-case evaluation baseline was approved by the maintainer on 2026-11-21. Retrieval benchmark pass 001 found 100% expected-page recall by top five unique page candidates, but first-stage passage-locator coverage was 47/55 (85.5%); full-page expansion of already retrieved pages raised locator coverage to 55/55. Exact-title retrieval was precise, ordinary lexical retrieval had moderate candidate noise, and contrast mode at k=16 was noisy. See `retrieval-benchmark-pass-001.json`. Answer-generation/citation scoring remains outstanding. The benchmark also exposed a schema mismatch for `exact_title` and `redirect_target`; the schema enum was corrected, all 20 captured packets passed local Draft 2020-12 validation, and three contract tests passed in GitHub Actions run `44947776807`.

Example:
```powershell
python research/rag/extract_infobox_claims.py .\\SR-Doc-Audit.zip --output infobox-claims.jsonl --report infobox-claims-report.json
python research/rag/evaluate_infobox_claims.py infobox-claims.jsonl --output infobox-claim-comparison.json
python research/rag/test_infobox_claims.py
```

All outputs are derived artifacts; do not write them into Bronze/Silver source paths. The extractor defaults to main namespace; use `--include-context` only for an explicitly contextual/editorial extraction. No source capture, manifest, canon page, merge, PR, or branch promotion was changed or performed.
