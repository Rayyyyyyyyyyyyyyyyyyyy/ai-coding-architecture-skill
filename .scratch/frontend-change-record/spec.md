# Frontend change record gate

Require `vibe-frontend` to establish a durable, project-linked basis before it
starts a non-trivial frontend implementation or refactor.

The skill should reuse an existing user-referenced or previously approved spec
or ticket when one already defines the change. Otherwise it should follow the
repository's configured planning mechanism, including OpenSpec or an issue
tracker, without requiring a particular tool to be installed. If the repository
has no configured mechanism, it should create a lightweight local change record
before editing source code.

The record must capture the evidence that motivates the change, the intended
outcome, the smallest authorized scope, and relevant constraints or acceptance
evidence. It is a traceability gate, not a second approval gate. Advice and
assessment remain read-only, routine cosmetic edits remain outside this skill,
and newly discovered unrelated problems must not silently expand implementation
scope.
