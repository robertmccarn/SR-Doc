# RAG readiness and implementation plan

**Status:** Initial implementation specification; no retrieval service is claimed to exist yet.
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
- [x] Implement exact page-ID lookup and title/section/body lexical search. Alias resolution remains outstanding.
- [x] Return source passages with stable page/revision/hash/path/section/character-offset citations.
- [x] Add CLI search command that emits evidence packets conforming to schema 1.0.
- [x] Test exact-name/phrase retrieval and page-ID lookup against known corpus passages.
- [ ] Add explicit title alias/redirect resolution and retrieval evaluation.

### Phase 3 — Graph-assisted and semantic retrieval
- [ ] Load the versioned graph package as optional sidecar.
- [ ] Implement entity resolution and bounded graph expansion.
- [ ] Add embeddings only if evaluation shows lexical retrieval gaps.
- [ ] Retrieve competing evidence for contradictions and date conflicts.
- [ ] Preserve predicate direction and edge provenance.

### Phase 4 — ChatGPT workflow
- [ ] Define a repeatable handoff format for evidence packets.
- [ ] Add Project-level assistant instructions using the protocol.
- [ ] Ensure each answer is based on the supplied evidence packet or explicitly reports unavailable retrieval.
- [ ] Validate citations and abstention behavior manually.

### Phase 5 — Evaluation and iteration
- [ ] Author and review the 20-question benchmark.
- [ ] Score retrieval and answer quality separately.
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
