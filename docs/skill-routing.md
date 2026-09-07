# Skill Routing and Ownership

Use the collection prefix `vibe-` plus a short invocation name and precise task
descriptions. The prefix identifies this collection; it does not alter scope.
Select only skills
whose concrete task signals apply; names alone do not broaden authorization.

| Requested outcome | Skill or mode | Owns |
| --- | --- | --- |
| Understand architecture or data flow | `vibe-project`: explain | Source-grounded human walkthrough, wiring, gaps, and evidence limits. |
| Identify system architecture problems | `vibe-project`: assess | Material system ownership, dependency, data, interface, recovery, and change-locality findings. |
| Understand and assess | `vibe-project`: both | One shared map and evidence set, followed by explanation and supported findings. |
| Assess or change frontend structure | `vibe-frontend` | Component/state/effect ownership, semantic reuse, frontend contracts, typing, and test seams. |
| Recover or preserve design intent | `vibe-design-context` | Non-obvious durable reasons and constraints. |
| Assess or complete relevant user-visible states | `vibe-ux` | Journey states and recovery feedback. |
| Diagnose broken or slow behavior | `vibe-debug` | Causal evidence and diagnosis; fixes only when requested. |
| Judge concrete trust, data, or runtime risk | `vibe-safe-change` | Relevant safety and recovery boundaries. |
| Verify an executable change or an explicit verification request | `vibe-verify` | Proportionate evidence and calibrated completion claims. |
| Transfer work to an agent consumer | `vibe-handoff` | Precise task state, artifacts, and limits at a real handoff. |

## Project modes

No pending implementation is needed to explain or assess an existing repository.
Choose the mode from the user's words without requiring a special command syntax.
“Show me how it works” selects explanation; “is this architecture problematic?”
selects assessment; “explain it and flag problems” selects both.

Share the repository map and already inspected evidence between modes and
follow-up turns. Recheck changed or previously uninspected boundaries. A pure
explanation reports meaningful implementation gaps without becoming a general
architecture audit. All project modes remain read-only, apart from explicitly
requested report artifacts.

For a frontend-only structural judgment, use `vibe-frontend`. A `vibe-project`
assessment may use it for detailed intra-frontend findings while retaining
responsibility for the overall coverage and cross-unit contracts. Neither mode
claims whole-repository health from one inspected slice.

## Composition and authorization

See [skill composition](skill-composition.md). Specialist invocation retains the
user's scope and does not automatically authorize code or record changes.

- `vibe-project` shares discovery between its modes and uses specialist judgment
  only where a concrete concern needs it.
- `vibe-frontend` owns frontend structure; `vibe-ux` owns which user-visible states
  need to exist, and `vibe-safe-change` owns trusted enforcement.
- `vibe-design-context` corroborates documented intent and preserves it only within
  authorized changes; stale records alone do not authorize a rewrite.
- `vibe-debug` supplies causal evidence; `vibe-verify` consumes relevant evidence when
  finishing an authorized fix rather than repeating diagnosis.
- `vibe-handoff` is for another agent, never a mandatory human-facing completion step.

## Recovery as a documented workflow

[Recovery](workflows/recovery.md) coordinates existing skills when the user asks
to stabilize a broken project. It is not a ninth skill or an automatically
invoked prerequisite for a partially built repository. Preserve the agreed
repair scope and record unverified or deferred work. Ordinary project inquiry
does not start repairs.

Historical names and snapshots are retained in prior specs and evaluation runs.
Current invocation names and installation directories are the eight listed in
[README](../README.md).
