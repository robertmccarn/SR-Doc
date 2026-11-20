# Research documentation governance — agent protocol

**Status:** Normative instructions for every AI agent and automated contributor working in this repository's research documentation.  
**Owner:** User-directed SR-Doc research workflow.  
**Applies to:** `agents.md`, `research/README.md`, `research/continuity/MASTER-RESEARCH-REGISTER.md`, `research/session-log.md`, ledgers, tranche notes, thematic notes, and any future research documentation.

This document is intentionally self-referencing: it defines how this document itself, its parent index, and the rest of the documentation system must be maintained. It is the governing procedure; the master register is the current factual status; `agents.md` is the concise agent entry point.

## 1. Required reading order

At the start of every session that touches this repository:

1. Read `agents.md`.
2. Read this document: `research/continuity/DOCUMENTATION-GOVERNANCE.md`.
3. Read `research/continuity/MASTER-RESEARCH-REGISTER.md`.
4. Read `research/README.md`.
5. Read the relevant detailed evidence notes and ledgers.
6. Read recent entries in `research/session-log.md` when resuming ongoing work.

If the agent guide and this protocol disagree, this protocol governs documentation operations. If this protocol and the master register disagree about factual status, verify against the underlying source/ledger and update the register; never assume either document is factually correct merely because it is canonical.

## 2. Stable document responsibilities

Each document has one job. Do not let responsibilities drift.

| Document | Sole responsibility | Must not become |
|---|---|---|
| `agents.md` | Short entry point, safety rails, required reading, reporting rules | Append-only diary, detailed findings archive |
| This governance file | Rules for creating, updating, organizing, and reconciling documentation | Research findings or a second status register |
| `research/README.md` | Concise navigation and status snapshot | Full audit narrative or duplicate session log |
| `MASTER-RESEARCH-REGISTER.md` | Canonical current status, definitions, findings index, unresolved work, inventory | Raw evidence dump or chronological diary |
| `session-log.md` | Append-only chronology of completed work and corrections | Current status authority or place for full findings |
| Ledgers (CSV/structured files) | Row-level machine-readable inventory and status | Narrative explanation |
| Tranche notes | Complete evidence/method/results for a bounded batch | Global status or speculative conclusions |
| Thematic/continuity notes | Detailed synthesis across named source records | Unreferenced canon rewrite or general session diary |
| Historical archives | Preserve superseded documentation exactly | Current instructions or current status |

Every new file must have one clearly assigned role. If its purpose overlaps an existing file, extend the existing file unless a distinct bounded scope justifies a new note.

## 3. Evidence and authority rules

Use this precedence for factual claims:

1. Original Bronze source bytes and their manifests for what was captured.
2. Reproducible computations and current ledgers for derived inventory/checksum facts.
3. Detailed notes for the methods, excerpts, and findings they actually document.
4. Master register for the latest reconciled interpretation and current status.
5. README for a compact presentation of that status.
6. Session log for the sequence of work, not present-day truth.
7. Agent instructions for process, not source facts.
8. Archived notes and conversation history for historical context only.

A higher-level summary does not override source evidence. When two sources conflict, record the conflict and investigate. Do not silently choose the more convenient value.

Every substantive finding must be labelled or phrased so the reader can distinguish:
- **Observed:** directly present in a source or tool result.
- **Computed:** produced by a documented repeatable calculation.
- **Inferred:** a reasoned interpretation supported by observations.
- **Hypothesis:** a plausible explanation needing confirmation.
- **Unresolved:** evidence is insufficient or conflicting.

For important claims, cite exact page title/ID, manifest entry, source path, note, or ledger row. Record method and limitations. Do not upgrade a mention to a dependency, a dependency to rendered use, or absence to orphan status without the relevant verification.

## 4. Change protocol — before editing

Before changing any research document:

1. Confirm the active branch is `audit/continuity-research`, unless the user explicitly authorizes another branch.
2. Fetch the current branch version of every file to be edited. Do not trust stale local copies, previous conversational contents, or old blob SHAs.
3. Identify the document's role from section 2.
4. Determine whether the proposed information is a new finding, a correction, a status change, a navigation change, or a process change.
5. Identify all dependent summaries/indexes that must be synchronized.
6. Preserve existing information. Do not delete, condense, or rewrite detailed evidence merely to make a document shorter.
7. If a claim is uncertain, retain the uncertainty instead of making the prose sound definitive.

Never use an append operation as a substitute for understanding the existing structure. In particular, do not add another addendum to `agents.md`; update the relevant focused note and the canonical register.

## 5. Change protocol — after editing

Apply only the updates required by the nature of the work:

### New bounded research finding
- Create or update one focused note containing scope, exact sources, method, observations, computed results, interpretation, confidence, limitations, and unresolved questions.
- Update the master register's findings index, current status, and next actions.
- Update README only if the status snapshot or navigation changes.
- Append a dated, concise session-log entry.
- Update `agents.md` only if the operating procedure or immediate handoff materially changes.

### Correction to an existing finding or count
- Re-open the relevant primary source or reproduce the computation.
- Correct the detailed note/ledger first, with a clear correction history where the previous claim was material.
- Reconcile the master register and README.
- Append a session-log correction explaining what changed, why, and which previous statement is superseded.
- Never silently rewrite history or erase the old claim from the chronological log.

### Process or governance change
- Update this governance file first.
- Update `agents.md` to point to the new rule and reflect only the concise operational consequence.
- Update README/master register navigation only if paths or responsibilities changed.
- Record the change in the session log.

### Pure navigation or formatting change
- Update only the affected index/document unless another document contains a now-broken path or contradictory instruction.
- Do not create a session-log entry for trivial whitespace or cosmetic-only edits unless the user specifically asks for a complete change record.

## 6. Synchronization rules

The master register is the only canonical current status summary. README is a compact mirror, not a competing authority.

Whenever a material status changes:
1. Update the detailed evidence/ledger.
2. Update the master register.
3. Mirror only the necessary summary in README.
4. Append the action to session log.
5. Update agent guide only when process or handoff changes.

Use the same definitions, units, date ranges, and denominators everywhere. Always state denominators for percentages and distinguish records, unique titles, physical files, references, and edges. Do not mix tranche-level counts with corpus totals.

Do not copy a large body of findings into multiple files. Use concise summaries and relative links to the authoritative detailed note.

## 7. Preservation and refactoring rules

- Never delete detailed source-grounded notes, ledgers, or historical records merely because a master summary now exists.
- Consolidation means indexing, cross-linking, deduplicating repeated summaries, and clarifying authority—not discarding unique facts.
- When replacing a major document, first preserve its complete prior version in a clearly named archive and verify the archive after creation.
- Mark archives as historical and non-authoritative. Never direct future agents to follow archived instructions when current guidance differs.
- Do not archive every routine revision; archive only material structural replacements or when explicitly requested.
- Keep `agents.md` concise. Put durable findings in focused notes, not agent instructions.
- Keep README short enough to scan. Put definitions and detailed reconciliation in the master register.
- Keep session log append-only. Add corrections, never retroactively erase earlier entries.
- Do not rename or move existing notes unless every inbound link and inventory is updated and the change is justified.
- Avoid duplicate files with names like `final-v2-revised`; use stable topic names and explicit pass numbers.

## 8. Self-maintenance of this governance document

This file must remain the single authoritative documentation-maintenance protocol.

When changing this file:
1. Read the entire current file before editing.
2. Preserve all existing rules unless there is an explicit reason to supersede them.
3. Add a short "Supersedes" or "Change history" note when a material rule changes; do not append an unbounded diary.
4. Update `agents.md` if required reading or operating behavior changes.
5. Update the master register/README only if navigation, hierarchy, or document responsibilities change.
6. Append a session-log entry describing material governance changes.
7. Re-fetch and verify this file and all dependent documents after commits.

Do not create a second governance file that competes with this one. If the protocol becomes too long, reorganize its sections without losing any rule; keep its path stable.

## 9. Git and execution safety

- Use the branch specified in `agents.md` and current master register.
- Fetch current content and blob SHA immediately before each update.
- Commit logically related documentation changes with clear messages.
- If a multi-file operation partially fails, report the partial state and repair it before declaring completion.
- After writes, fetch every changed file again and verify its expected content.
- Never claim a successful commit or verification without tool confirmation.
- No merge, pull request, branch promotion, or canon edits without explicit user approval.
- Bronze source files and manifests are immutable.

## 10. Completion checklist

Before reporting a documentation task complete, confirm:

- [ ] Correct branch verified.
- [ ] Current versions fetched before edits.
- [ ] Each changed file still has one clear responsibility.
- [ ] Unique evidence and detail were preserved.
- [ ] Counts, definitions, dates, and links are consistent across summaries.
- [ ] Master register is current.
- [ ] README mirrors only the necessary current status.
- [ ] Session log records material work/corrections.
- [ ] Agent guide reflects current process without accumulating findings.
- [ ] All changed files were fetched and verified after writing.
- [ ] No unauthorized merge, PR, promotion, or canon modification occurred.

## 11. Change history

- 2026-11-20 — Initial protocol established after consolidation of the research documentation system. It formalizes the stable roles of `agents.md`, README, master register, session log, detailed notes, ledgers, and historical archives.
