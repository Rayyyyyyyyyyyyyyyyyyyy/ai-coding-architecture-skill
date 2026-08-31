# Architecture Context Cases

## New agent enters an existing feature

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

Request: Make a nearby non-trivial change.

Expected: Identify the exact conflict and synchronize the stale side when intent is clear. If materially ambiguous, preserve the current boundary and surface the decision instead of guessing.
