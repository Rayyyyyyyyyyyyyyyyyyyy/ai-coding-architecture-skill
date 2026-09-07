# Add a pre-implementation change-record gate

Status: resolved
Triage: ready-for-agent

Update `vibe-frontend` so non-trivial frontend implementation begins from a
durable work record rather than moving directly from discovery into source edits.

Acceptance criteria:

- A user-referenced or previously approved spec or ticket satisfies the gate
  without creating a duplicate artifact.
- Otherwise the skill uses the repository's existing OpenSpec, issue-tracker, or
  planning convention when available.
- When no repository convention exists, the skill creates a lightweight local
  record before source edits and tells the user where it was written.
- The record includes motivating evidence, intended outcome, authorized scope,
  constraints, and acceptance evidence appropriate to the change.
- The gate does not create a redundant approval pause for already authorized
  implementation.
- Assessment remains read-only, cosmetic edits remain outside the skill, and
  unrelated findings do not expand implementation scope.
- Behavioral cases and discovery metadata agree with the workflow.
- The skill passes applicable validation.

## Comments

Claimed on 2026-09-08 in response to observed behavior where the skill moved
directly from finding an architecture problem into editing code.

## Answer

Added a pre-implementation change-record gate to `vibe-frontend` for
non-trivial frontend work. The skill now reuses a user-referenced or previously
approved work item, follows an existing OpenSpec or issue-tracker convention when
available, and otherwise writes a concise `.scratch/<change-slug>/spec.md`
without installing planning tooling.

The record preserves motivating evidence, the requested outcome, authorized
scope and exclusions, constraints, and observable acceptance evidence. It does
not create new implementation authority or require redundant approval. Advice
and assessment remain read-only, cosmetic work remains outside the skill, and
unrelated findings are deferred instead of silently added to the implementation.

Updated the skill metadata, README, composition guidance, and behavioral cases
for existing work-item reuse, tool-free fallback, and scope containment.

Verification evidence:

- `quick_validate.py skills/vibe-frontend` reported `Skill is valid!`.
- `git diff --check` passed.
- Static checks confirmed the skill, cases, composition guidance, and README all
  expose the change-record rule and fallback.
- The behavioral cases were specified but not executed as recorded agent runs;
  they are not claimed as runtime evidence.
- The globally installed copy under `~/.agents/skills` was inspected and remains
  separate from this repository source; updating this repo does not update that
  installed copy.
