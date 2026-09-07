---
name: vibe-frontend
description: Assess an existing frontend's architecture or structure non-trivial frontend changes through clear ownership and justified abstraction. Use for frontend architecture reviews or refactoring questions even when no implementation is requested. Keep advice read-only. Not for backend-only work or cosmetic edits.
---

# Vibe Frontend

Assess whether an existing frontend has material architecture problems, or make
the smallest cohesive frontend change that fits the existing system.

Load each named skill through the host mechanism; call the Skill tool when exposed. Do not reload an active skill.

## Scope

- **Advice or assessment:** use this mode when asked whether an existing frontend
  has architecture problems or where it should be refactored. A pending code
  change is not required. Report findings with evidence, impact, and recommended
  scope; do not edit files or invoke implementation-completion verification.
- **Implementation:** when development or refactoring is requested, apply the decision order within the authorized scope. Do not require a second approval for routine in-scope choices; obtain agreement before expanding the scope or resolving a missing product decision.
- Follow user and repository instructions.
- Preserve the framework, design system, directory conventions, state model, and test strategy unless the task requires change.
- Own frontend language selection, component/state boundaries, semantic reuse, frontend data normalization, and abstraction decisions.
- In a mixed repository, classify code by its runtime responsibility rather than
  its directory or tooling name. Follow a server, worker, build step, or data
  producer only far enough to establish the frontend contract; identify an
  external dependency without assessing or recommending changes to that other
  architecture under this skill.
- Do not reorganize unrelated modules or absorb cross-unit project architecture,
  security, UX completeness, verification, or handoff ownership.

## Assess an existing frontend

Inspect reachable implementation before judging its directory or file layout.
Start from the frontend entry points and representative user flows, then follow
the components, state, effects, data boundaries, and tests that govern them. For
a focused review, inspect only the affected boundary; for a whole-frontend
review, account for each major frontend execution unit and label uninspected
scope.

Evaluate these concerns when the repository provides a concrete signal:

- **Responsibility and change boundaries:** determine whether modules and
  components group behavior that changes for the same reason. A large file,
  many components in one file, prop count, or a sparse directory tree is an
  investigation signal, not a defect by itself.
- **Component, state, and effect ownership:** identify who owns authoritative
  state, which values are derived, and where external synchronization occurs.
  Report concentration only when unrelated responsibilities make a change hard
  to isolate, create competing owners, or force broad setup and testing.
- **Frontend data contracts:** trace untrusted, persisted, or provider data at
  its entry boundary. Check whether it is normalized and runtime-validated
  before components rely on it, and whether several consumers silently depend
  on the same shape. Evidence from the producer may establish the contract, but
  findings and recommended scope stay on the frontend side of the boundary.
- **Type guarantees:** determine what protects consequential contracts today:
  TypeScript, runtime schemas, generated types, focused tests, or nothing. Treat
  JavaScript alone as no defect. Recommend a typing or validation change only
  when concrete contract or maintainability evidence justifies its cost, and
  distinguish compile-time guarantees from runtime validation of external data.
- **Test seams:** check whether independently meaningful rules and external
  effects can be exercised without rendering or configuring the entire
  application. Missing tests alone do not prove a boundary is wrong; coupling
  that blocks focused evidence can.

Each finding must identify the source evidence, the change or failure scenario
that creates impact, and the smallest recommended scope. Separate observed
structure from inferred risk and say when no material problem was found. Do not
turn the assessment into a preferred folder tree, a code-smell inventory, or an
unrequested migration plan.

## Language

- Greenfield JavaScript ecosystem with no convention: TypeScript unless the user or runtime requires JavaScript.
- Existing TypeScript scope: stay in TypeScript.
- Existing JavaScript implementation: stay in JavaScript unless migration is
  requested; do not turn feature work or refactoring into an incidental
  migration. A read-only architecture assessment may recommend TypeScript,
  runtime validation, or a focused combination only under the evidence standard
  above; assessment does not authorize migration.

## Decision order

**Reuse → Compose → Extract → Abstract**

1. Inspect conventions, primitives, data shapes, state ownership, dependencies, callers, and tests.
2. Reuse an equivalent contract; visual similarity alone is insufficient.
3. Compose when consumers need arrangement without merged responsibilities.
4. Extract behavior that repeats semantically, changes for the same reason, obscures ownership, or needs an independent test boundary.
5. Abstract only for a concrete boundary: multiple real implementations, vendor isolation, business rules, replacement, or testability.

Line count, prop count, and hypothetical reuse are investigation signals, not extraction criteria.

## Boundary rules

- Keep one state owner; derive values instead of synchronizing copies. Use context/store only for real cross-tree coordination.
- Keep business rules outside dense rendering conditionals when independently meaningful.
- Normalize untrusted or vendor data at its entry boundary into a canonical application model.
- Keep feature code local until semantic reuse is demonstrated; expose shared code through a small named API.
- Prefer existing framework/design-system/platform capability. On a real dependency-risk signal, invoke `vibe-safe-change`.
- Prefer domain names over `utils`, `helpers`, `common`, or universal configurable components.

Report only a material boundary, abstraction, or intentional convention deviation. On implementation completion invoke `vibe-verify`; on actual agent transfer invoke `vibe-handoff`.
