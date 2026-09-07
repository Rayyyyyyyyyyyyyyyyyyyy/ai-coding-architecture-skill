# Repository Architecture Context

Read this reference when a task creates or changes a meaningful architectural boundary, disputes an existing architecture record, directly depends on a recorded decision, or needs durable non-obvious intent recorded for future agents. The mere presence of architecture documentation is not a trigger.

The outcome is a repository that preserves the non-obvious intent future contributors must retain. This is not complete project memory: code, types, schemas, tests, and operational documentation remain responsible for facts they already express well. Do not turn ordinary implementation work into a documentation project.

## Locate the established source of truth

Before creating a document, search for the repository's existing convention. It may use:

- `ARCHITECTURE.md` at repository, package, feature, or module scopes;
- an architecture directory or architectural decision records;
- package or feature READMEs that explicitly carry architecture decisions;
- repository instructions containing ownership or dependency rules.

Use `ARCHITECTURE.md` as the default only when no equivalent convention exists. Do not introduce a second competing convention.

When the task directly depends on architectural intent, read relevant context from general to local:

```text
user and repository instructions
↓
repository-level architecture
↓
parent scope architecture
↓
nearest feature or module architecture
↓
code, types, schemas, and tests
```

The nearest document may add local specificity, but it must not silently contradict higher-level rules. Read only documents relevant to the changed scope.

## Reconcile intent with implementation

Architecture documentation represents intended design. Code, types, schemas, tests, and callers represent implemented reality. Neither is automatically current when they conflict.

When they disagree:

1. Identify the exact conflicting responsibility, ownership rule, dependency, public boundary, or invariant.
2. Use the current task, repository instructions, tests, callers, and version history to determine whether the implementation or documentation is stale.
3. If the intent can be determined safely, update the stale side only within an authorized implementation or documentation change. For inquiry or review, report the conflict, evidence, and proposed correction without editing either side. Permission to update documentation does not itself authorize changing executable behavior.
4. If resolution requires a product decision, destructive migration, or material scope expansion, preserve the current boundary where possible and ask the user instead of guessing.

Do not replace explicit repository evidence with a preferred pattern merely because another architecture seems more familiar.

## Decide whether documentation is warranted

Architecture documentation follows meaningful boundaries, not directory depth. A scope may deserve documentation when it owns one or more of:

- important state or a canonical model;
- domain or business rules;
- dependency direction or a public module boundary;
- an external API, persistence, auth, file, or AI-data boundary;
- non-obvious compatibility constraints or invariants;
- a deliberate separation that future agents are likely to undo.

Create a new architecture document only when all of these are true:

1. The directory represents a real architectural scope rather than file organization.
2. The intent is durable and cannot be safely reconstructed from code, types, or tests alone.
3. A future agent could reasonably make a costly wrong assumption without it.
4. No existing architecture document is a better home for the decision.
5. The current task introduces, changes, or directly depends on that intent; do not proactively document unrelated areas.

Prefer updating the nearest existing document over creating a new one.

## Record only decision-relevant context

Include only sections that carry non-obvious knowledge. Useful subjects are:

### Responsibility

What the scope owns and why it exists.

### Internal structure

The meaning of major layers or subdirectories when names alone do not explain it.

### Dependency rules

What the scope may depend on, what may depend on it, and which internals must not be imported directly.

### State ownership

Where canonical mutable state belongs and which values are derived outputs rather than second sources of truth.

### Public boundary

How other scopes should interact with this one.

### Important invariants

Rules a future change must preserve.

### External boundaries

Where vendor responses, APIs, files, persistence, auth, or AI output are validated and normalized.

### Explicit non-goals

Responsibilities intentionally excluded from this scope.

### Important rejected alternatives

Record an alternative only when it is tempting, likely to recur, and rejected for a durable reason.

For example:

```markdown
TripCard and PublicationCard intentionally remain separate. They share visual
primitives but represent different domain contracts and change independently.
```

Avoid prop lists, export inventories, file-by-file narration, and facts already enforced clearly by types or tests.

## Keep context synchronized

Update the nearest relevant document when a material change alters:

- responsibility or ownership;
- dependency direction or public APIs;
- canonical models or state ownership;
- persistence or external-system boundaries;
- significant invariants or an important rejected alternative.

Do not update architecture documentation for renames or implementation details that leave architectural intent unchanged. Remove or revise claims that no longer describe the system.

Use this decision gate:

```text
Did this change alter durable intent that a future agent cannot reliably infer
from the implementation alone?

Yes → update the nearest established architecture document.
No  → do not create documentation noise.
```

For a material architecture change, mention the synchronized document in the final response. Do not narrate the entire context-recovery workflow unless the user needs it.
