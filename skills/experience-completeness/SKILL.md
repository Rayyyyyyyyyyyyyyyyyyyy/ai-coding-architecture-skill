---
name: experience-completeness
description: Complete user-visible states justified by changed async, data-backed, state-changing, content, layout, or interactive-control signals. Not for backend, copy-only, or cosmetic work.
---

# Experience Completeness

Complete only the states signaled by the changed journey.

Load each named skill through the host mechanism; call the Skill tool when exposed. Do not reload an active skill.

## Ownership

- Own user-visible state and recovery, not auth policy, server idempotency, persistence, schema, or other trusted enforcement.
- When the experience depends on a trusted guarantee, define the interface and invoke `safe-change`.
- Preserve the existing state owner, design system, and interaction conventions.

## Select states

Map concrete signals to states:

| Signal | State |
| --- | --- |
| async work or latency | pending/slow |
| valid zero results | empty |
| fallible recoverable action | error/recovery |
| state-changing action | success/repeated action |
| variable or localized content | long content |
| changed supported viewport behavior | responsive |
| changed control, focus, status, or validation | keyboard/semantics/announcement |

No signal, no state. Do not turn a local toggle or color change into a journey audit.

Read only the selected sections of [references/state-guide.md](references/state-guide.md). Do not create duplicate request state, a second design system, or client-side security claims.

Exercise the primary path and highest-impact selected non-happy path. Verify focus, disabled state, preserved input, retry, and responsive behavior only when selected. On completion invoke `verify-before-done`; on actual agent transfer invoke `a2a-handoff`.
