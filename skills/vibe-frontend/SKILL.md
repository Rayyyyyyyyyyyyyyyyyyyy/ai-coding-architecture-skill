---
name: vibe-frontend
description: Assess an existing frontend's architecture or structure non-trivial frontend changes through clear ownership, a durable change record, and justified abstraction. Use for frontend architecture reviews or refactoring questions even when no implementation is requested. Keep advice read-only. Not for backend-only work or cosmetic edits.
---

# Vibe Frontend

Load named skills through the host mechanism; call the Skill tool when exposed.
Do not reload an active skill.

## Scope

- **Assessment:** inspect existing frontend architecture even without a pending
  change. Keep files read-only apart from requested report/work-item artifacts;
  do not invoke implementation-completion verification.
- **Implementation:** make the smallest cohesive authorized change, beginning
  with the change record below. Ask only for scope expansion or missing product
  decisions, not routine in-scope choices.
- Follow user/repository instructions and preserve framework, design system,
  directory conventions, state model, and test strategy unless change is required.
- Own frontend language, component/state/effect boundaries, data normalization,
  reuse, and abstraction. Classify code by runtime responsibility: follow servers,
  workers, build steps, or producers only to establish the frontend contract.
  Keep findings on the frontend side; leave cross-unit architecture, security,
  UX completeness, verification, and handoff to their owners.
- Defer unrelated findings rather than editing them.

## Record the change before implementation

Before editing source or tests for architecture restructuring, changed
component/state/effect ownership, frontend data boundaries, or abstractions:

1. Read and reuse a user-referenced or previously approved spec/ticket that
   already defines the change; do not create a duplicate.
2. Otherwise follow the repository's existing planning/tracking convention,
   using available, authorized mechanisms without installing planning tools.
3. With no convention, create `.scratch/<change-slug>/spec.md`, tell the user
   where it lives, and continue the authorized work without another approval.

Keep the record proportional. Capture source evidence and the requested outcome,
smallest authorized scope and meaningful exclusions, constraints/decisions to
preserve, and observable acceptance evidence. A record does not expand authority.
Routine cosmetic edits are outside this skill and need no record.

## Assess an existing frontend

Trace reachable entry points and representative flows through components, state,
effects, data boundaries, and tests. Inspect the affected boundary for focused
reviews; cover each major frontend execution unit for whole-frontend reviews
and identify uninspected scope.

Evaluate concerns supported by concrete signals:

- **Responsibility:** group behavior that changes for the same reason. Report
  concentration when unrelated responsibilities impede isolated changes or
  require broad setup/testing. File size, prop count, colocation, directory shape,
  and JavaScript alone are investigation signals, not defects.
- **State/effects:** identify authoritative state, derived values, external
  synchronization, and competing owners.
- **Data contracts:** trace external, persisted, or provider data to its entry
  boundary; check normalization, runtime validation, and consumers' shared shape
  assumptions. Producer evidence may establish the frontend contract.
- **Type guarantees:** identify protection from types, runtime schemas, generated
  types, or focused tests. Distinguish compile-time guarantees from runtime
  validation; recommend changes only for material contract or maintenance benefit.
- **Test seams:** can independently meaningful rules/effects be exercised without
  the entire app? Missing tests alone do not prove a boundary is wrong; coupling
  that prevents focused evidence can.

Report evidence, concrete change/failure impact, and the smallest useful scope;
separate observation from inferred risk. For optimization recommendations, explain
how the change reduces current maintenance cost and weigh benefit against change
and verification cost. A maintenance problem need not be a runtime bug. Recommend
retaining the implementation when benefit is unsupported or too small, and say
when no material problem was found. Avoid folder-tree prescriptions, code-smell
inventories, and unrequested migration plans.

## Language

- Greenfield JavaScript ecosystem without a convention: TypeScript unless the
  user or runtime requires JavaScript.
- Existing code: preserve its JavaScript/TypeScript choice unless migration is
  requested. Assessment may recommend TypeScript, runtime validation, or both
  under the evidence standard above; it does not authorize migration.

## Decision order

**Reuse → Compose → Extract → Abstract**

Inspect conventions, primitives, contracts, callers, dependencies, ownership,
and tests. Reuse equivalent contracts; visual similarity is insufficient.
Compose arrangements without merging responsibilities. Extract semantic
repetition, unclear ownership, behavior that changes together, or independently
meaningful test boundaries. Abstract only for multiple real implementations, vendor
isolation, business rules, replacement, or testability—not hypothetical reuse.

## Boundary rules

- Keep one state owner and derive values; context/store requires real cross-tree
  coordination.
- Separate independently meaningful business rules from dense rendering while
  keeping ordinary view conditions local.
- Normalize untrusted/vendor data at entry into a canonical application model.
- Keep features local until semantic reuse is demonstrated; expose a small named
  API. Prefer domain names over generic helpers or universal components.
- Reuse framework/design-system/platform capabilities. On a concrete dependency
  risk, invoke `vibe-safe-change`.

Report material boundaries, abstractions, or intentional convention deviations.
On implementation completion invoke `vibe-verify`; on actual agent transfer,
`vibe-handoff`.
