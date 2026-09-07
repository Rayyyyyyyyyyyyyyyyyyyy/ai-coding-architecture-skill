# Architecture Context Cases

## Task directly depends on recorded ownership

Fixture: Feature-level architecture documentation assigns filter state to the feature subtree; a global store also exists.

Request: Share the filter with another nearby component.

Expected: Discover the local documentation and preserve feature ownership.

## Explicit semantic separation

Fixture: Two visually similar components are documented as separate domain contracts that change independently.

Request: Add shared visual behavior.

Expected: Reuse low-level primitives while preserving semantic separation; do not create one boolean-driven component.

## Cross-agent provider continuation

Fixture: A previous agent documented `provider → adapter → canonical model → feature`.

Request: Add another provider.

Expected: Recover and preserve the documented flow without relying on conversation history.

## Architecture-changing request

Fixture: Existing documentation records state ownership and a public dependency boundary.

Request: Legitimately move ownership or change the boundary.

Expected: Implement the change and synchronize the nearest relevant architecture document without rewriting unrelated documentation.

## Trivial presentational badge

Fixture: A simple feature directory has no architecture documentation.

Request: Add a local status badge.

Expected: Implement normally and do not create `ARCHITECTURE.md`.

## Stale documentation conflict

Fixture: Local documentation conflicts with current types, callers, tests, and a recent repository decision.

Request: Change the public boundary governed by the conflicting documentation.

Expected: Identify the exact conflict and synchronize the stale side when intent is clear. If materially ambiguous, preserve the current boundary and surface the decision instead of guessing.

## Unfamiliar repository negative control

Fixture: A large unfamiliar repository has architecture documents, but the requested change is a self-contained validation message with no effect on ownership, dependencies, public boundaries, state, external boundaries, or invariants.

Request: Improve the validation copy and its local test.

Expected: Do not load the design-context workflow merely because the repository is unfamiliar or the task requires several code edits. Use nearby code and tests without creating or updating architecture documentation.

## Non-trivial implementation negative control

Fixture: A feature has no architecture record and a multi-file refactor preserves all existing module responsibilities and public contracts.

Request: Deduplicate an internal calculation without changing behavior or ownership.

Expected: Do not create `ARCHITECTURE.md` or attempt to record the whole feature. Architecture context is unnecessary unless the refactor exposes a durable, non-obvious decision that the task actually depends on.

## Source narration negative control

Fixture: Types and tests already make a module's exports and behavior explicit.

Request: Preserve the module's architecture context for the next agent.

Expected: Do not turn file structure, exports, prop lists, or test-enforced behavior into architecture context. Record only an actual non-obvious decision if one exists; otherwise create no document and explain that code and tests already carry the relevant facts.

## Inquiry finds stale documentation

Fixture: An architecture record conflicts with current callers and tests; the intended ownership is recoverable from a recent decision.

Request: Explain the ownership boundary and tell me whether the document is current.

Expected: Explain the boundary, cite the conflicting evidence, and propose the correction without editing code or documentation. Do not treat a confidently identified stale record as implementation authorization.

## Documentation-only correction

Fixture: A recorded decision and current code disagree at a public boundary.

Request: Update the architecture document to describe the current implementation; do not change behavior.

Expected: Update only the relevant document from corroborated evidence. Do not change code to enforce the prior design or request redundant permission for the authorized documentation edit.

## Consistent design inquiry

Fixture: [consistent-intent](fixtures/consistent-intent/ARCHITECTURE.md) records why persisted document state excludes local selection. The implementation matches the record.

Request: Why is selection kept outside the persisted document? Explain the reasoning from this repository.

Expected: Answer with the documented intent and corroborating code evidence even though nothing changed or conflicts. Distinguish supported reasoning from unknown history; keep the fixture unchanged.
