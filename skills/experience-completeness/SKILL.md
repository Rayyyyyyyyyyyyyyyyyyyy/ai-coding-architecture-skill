---
name: experience-completeness
description: Assess or complete user-visible states justified by async, data-backed, state-changing, content, layout, or interactive-control signals in the selected journey. Keep assessment read-only. Not for backend, copy-only, or cosmetic work.
---

# Experience Completeness

Complete only the states signaled by the changed journey.

Load each named skill through the host mechanism; call the Skill tool when exposed. Do not reload an active skill.

## Ownership

- **Assessment:** when asked to inspect a journey or identify missing states, present the relevant state checklist, evidence, impact, and proposed scope without modifying the project. Wait for an implementation request before completing those states.
- **Implementation:** when asked to complete or improve the journey, implement the signaled states within the authorized scope without reconfirming routine choices. If completion requires a new product behavior or policy not established by the request or repository, present the choice and obtain agreement before implementing that behavior.

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

For implementation, exercise the primary path and highest-impact selected non-happy path. Verify focus, disabled state, preserved input, retry, and responsive behavior only when selected. On implementation completion invoke `verify-before-done`; on actual agent transfer invoke `a2a-handoff`.
