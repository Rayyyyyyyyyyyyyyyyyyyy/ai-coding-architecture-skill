---
name: vibe-project
description: Explain an existing repository's architecture and data flow, assess material architecture problems, or do both when requested. Use for project walkthroughs and repo-wide or system-boundary reviews, including partially built projects. Keep inquiry read-only; use vibe-frontend for detailed frontend structure and vibe-design-context for durable design intent.
---

# Vibe Project

Give the user a grounded understanding or assessment of the implemented project.

## Choose the requested outcome

- **Explain:** “how does this work?” or “help me understand this repo.” Explain reachable behavior and meaningful gaps without starting a general architecture audit.
- **Assess:** “where is the architecture problematic?” or “review these system boundaries.” Judge material problems using [assessment guidance](references/assess.md).
- **Both:** when the user asks to understand and assess, establish the map once, explain the relevant flows, then report the supported findings. Read the assessment guidance as well.

The user can specify the outcome in ordinary language; do not require mode names
or a second confirmation. A later follow-up reuses available evidence and
rechecks changed or previously uninspected paths instead of restarting the map.

## Scope and authority

Use the current working tree, including relevant uncommitted changes. Follow
applicable repository instructions. Treat architectural claims in documentation
as intent to corroborate against reachable implementation.

Keep inquiry read-only: do not change code, configuration, dependencies, tests,
tickets, or architecture records. If asked to save the result, write only the
requested human-facing artifact. A later implementation request supplies its own
scope and workflow. Existing safe runtime observations may add evidence; do not
run a build that rewrites generated files merely to explain or assess the repo.
Do not expose secrets while tracing configuration or integration boundaries.

## Establish the map and trace real flows

Start from workspace configuration, executable entry points, route or command
registration, storage, integrations, and runtime/deployment setup. Identify what
the project does, who uses it, and what each major execution unit owns.
Classify units by runtime responsibility, including applications, APIs, workers,
CLIs, libraries, scheduled jobs, and build or generation steps.

For a whole-repository request, account for each major execution unit before
drawing conclusions, and label any uninspected unit. For a focused request,
trace only the relevant boundaries and do not generalize to repository health.

Choose representative user actions or other inputs that cover the consequential
distinct paths, including a background/event path when central. Follow the
registered entry through actual callers, transformations, authoritative
decisions, reads/writes, external calls, and observable outputs.

For important data, establish its origin, authoritative owner, transformations,
storage and lifetime, and whether it leaves the system. Distinguish view state,
caches, derived artifacts, and durable state. Follow results back to consumers
through polling, subscriptions, or a concrete missing return path.

Use registration and framework conventions to resolve indirect calls. A missing
search match alone does not prove code is dead. Stop at inaccessible boundaries
and state what remains unknown.

## Establish current state

Keep wiring and observations separate: reachable implementation, mock data,
unconfirmed entry points, and documented plans are different from behavior
exercised in a named environment or supported only by static inference.
Check active adapters, flags, callers, and relevant working-tree changes.

Explain code/document conflicts without repairing either side. Phrase uncertain
reachability as “not found in the inspected scope.” Schemas and migrations do
not prove deployed state; a service implementation does not prove product use.
Missing credentials still allow a bounded static explanation or assessment.

## Explain to the user

Apply this section in explain or combined mode. For assessment-only requests,
use the findings-first output in the assessment reference.

Use the user's language and product vocabulary. Lead with the project's purpose
and how its main parts cooperate, then explain selected inputs as cause and
effect: what happens, where data goes, and how results return. Keep filenames
subordinate to the explanation and link a few consequential source locations.

Use a small labeled diagram only when it clarifies an inspected relationship.
Finish with meaningful unfinished connections and evidence limits. Deliver once
the map, representative flows, ownership, and limits are understandable rather
than exhausting every file. In combined mode, follow with findings using the
assessment guidance and share the same evidence/coverage statement.

## Specialist ownership

Use already-loaded skill instructions; load a named specialist through the host
mechanism only when its concrete signal applies and it is available.

- `vibe-frontend` owns detailed component/state/effect, typing, and frontend refactoring judgments.
- `vibe-design-context` owns recovering and preserving non-obvious durable intent.
- `vibe-debug` owns causal diagnosis of broken or slow behavior.
- `vibe-safe-change` owns concrete trust, auth, data, runtime, and recovery safety judgments.
- `vibe-ux` owns user-visible journey-state completeness.

Assessment does not authorize specialist implementation or record updates.
Do not invoke `vibe-verify` merely to finish a read-only inquiry. Use `vibe-handoff` only
when another agent will consume or resume the work.
