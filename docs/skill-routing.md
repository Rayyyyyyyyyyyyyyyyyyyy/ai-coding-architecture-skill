# Skill Routing and Ownership

This collection separates human-facing project explanation, engineering guardrails,
delegation handoff, and an explicit recovery workflow. A compatible host may select more than one skill
for a task, but each skill owns one decision so composition does not turn into
duplicated checklists.

## Invocation categories

### Human-facing project explanation

`explain-project` may be selected when the user wants to understand an existing
project's architecture, responsibilities, or data flow. It reads current wiring
and explains representative paths in plain language, including incomplete work
and evidence limits. It is normally discoverable, with no user-only invocation
restriction. A walkthrough is read-only unless the user requests an explanation
artifact; it does not itself authorize application changes.

This entry point answers how the current project works for a human.
`architecture-context` answers which durable design intent a change must preserve.
A normal implementation task does not need a whole-project walkthrough.

### Model-invoked engineering guardrails

These skills may be selected when their concrete task signal is present:

| Skill | Select when | Owns |
| --- | --- | --- |
| `coding-architecture` | A non-trivial frontend, UI-state, design-system, or frontend data-boundary change is being implemented or refactored. | Frontend language selection, structure, semantic reuse, composition, and ownership boundaries. |
| `architecture-context` | Existing architecture documentation governs the changed scope, or the change alters a durable ownership, public-boundary, dependency, state, or external-boundary decision. | Recovering and preserving non-obvious architectural intent in the repository. |
| `safe-change` | Implementation or review touches a listed risk boundary, or diagnosis concerns a suspected violation of one. | Whether the boundary is violated and any mutation is safe, authorized, compatible, and recoverable. |
| `experience-completeness` | An interactive user journey has relevant asynchronous, data-dependent, destructive, responsive, keyboard, or assistive-technology states. | Selecting and completing the real-world states needed for that journey. |
| `debug-with-evidence` | Software is reported or observed as broken, slow, intermittent, flaky, or regressed. | The failure-investigation loop and the evidence-supported diagnosis. |
| `verify-before-done` | An executable change is being finished. | Selecting decisive evidence and calibrating the completion claim. |

Selection is signal-based, not mandatory for every task. A static copy edit
does not need a user-journey audit, and a healthy feature request does not need
a debugging workflow.

### Delegation-event handoff

`a2a-handoff` applies only when an agent task is delegated, transferred,
resumed by another agent, or returned to an agent consumer. It owns transfer
semantics and formatting, not implementation quality. It should not activate
for ordinary human-only explanations or every completed code change.

### Explicit recovery workflow

`rescue-vibe-project` coordinates recovery only when the user explicitly asks
to rescue, stabilize, untangle, or regain confidence in an existing project.
Its `SKILL.md` declares `disable-model-invocation: true` for Agent Skills hosts
that honor that field, while `agents/openai.yaml` sets
`allow_implicit_invocation: false` for OpenAI/Codex. Hosts that support neither
mechanism must still preserve the explicit-only behavior.

## Composition rules

See [Host-neutral skill composition](skill-composition.md) for signal-gated,
context-aware invocation and how it maps across hosts.

The user's request and repository instructions always take precedence. When
several skills apply, preserve these ownership boundaries:

- `explain-project` explains current implementation to the user; discovering a
  gap during a walkthrough does not trigger repair or architecture-record edits;
- `safe-change` may require a decision or authorization before a risky mutation;
- `debug-with-evidence` determines what failed and why, but does not invent
  permission to implement a fix;
- `experience-completeness` selects relevant journey states, while
  `coding-architecture` decides how their frontend implementation fits the
  existing codebase;
- `architecture-context` records only durable intent that future contributors
  could not reliably recover from implementation evidence;
- `verify-before-done` verifies the selected behavior and controls the final
  confidence claim instead of redefining the other skills' requirements;
- `a2a-handoff` transfers the resulting state and durable artifacts without
  becoming another implementation checklist;
- `rescue-vibe-project` sequences applicable guardrails for one recovery slice
  without absorbing their responsibilities.

These are ownership rules, not a fixed pipeline. When a concrete signal calls
for an installed owning skill, invoke it through the host's skill-loading
mechanism if it is not already present in the active context. Invoke
`a2a-handoff` only at an actual agent transfer. Apply only the skills and
ordering justified by the task.
