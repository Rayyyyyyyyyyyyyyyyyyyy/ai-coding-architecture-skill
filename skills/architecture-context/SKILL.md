---
name: architecture-context
description: Recover or preserve non-obvious architectural intent when a task creates, changes, disputes, or depends on a durable ownership, dependency, public, state, or external boundary. Not for repository familiarization.
---

# Architecture Context

Keep durable architectural intent recoverable from the repository.

Load each named skill through the host mechanism; call the Skill tool when exposed. Do not reload an active skill.

## Recover

- Distinguish read-only inquiry/review from authorized implementation or documentation work. For inquiry or review, report the relevant intent, evidence, and conflicts without editing code or documents. Apply synchronization and record-creation rules only within an authorized change; clear evidence of staleness alone does not authorize a repair.

- Follow user and repository instructions.
- Use the established architecture-documentation convention; create `ARCHITECTURE.md` only when none exists.
- Read only the hierarchy governing the active boundary, then corroborate it with code, types, schemas, tests, and callers.
- Treat documentation as intended design and implementation as current reality. Resolve conflicts from repository evidence; surface only product decisions, destructive migrations, or scope expansion.

## Preserve

- Preserve documented ownership, dependency direction, public APIs, canonical state, external boundaries, and invariants unless the task changes them.
- When durable intent changes, update the nearest existing record in the same change.
- Create a record only when the intent is durable, non-obvious, consequential, and has no established home.
- Record decisions and invariants, not exports, props, filenames, or behavior already enforced by code and tests.

Read [references/architecture-context.md](references/architecture-context.md) only for conflict resolution or document-creation criteria.

Mention architecture context only when it changed or remains conflicted. On an actual agent transfer, invoke `a2a-handoff` and reference the durable record.
