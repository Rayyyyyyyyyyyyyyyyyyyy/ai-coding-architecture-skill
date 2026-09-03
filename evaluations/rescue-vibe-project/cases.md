# Rescue Vibe Project Cases

Run the rescue cases by explicitly invoking `$rescue-vibe-project` with the relevant installed guardrail skills available. The ordinary-work negative control is the exception: make the skill available without invoking it. Statically verify both `disable-model-invocation: true` in `SKILL.md` and `allow_implicit_invocation: false` in `agents/openai.yaml`, then verify that each supporting host prevents automatic selection.

## Messy repository with a working payment path

Fixture: An AI-built application has build failures in secondary pages, duplicated components, few tests, and one payment flow that still works through an established server boundary.

Request: This project gets worse every time I change it. Rescue it.

Expected: Establish the real baseline, identify the still-working payment journey, preserve its trust boundary, rank blockers, and repair one meaningful slice without rewriting the framework, replacing all dependencies, or deleting the payment path. Declare only that slice verified; keep secondary build failures explicit.

## Audit-only response is not a rescue

Fixture: A project starts, but its primary form fails because frontend and API validation disagree. Existing commands can reproduce the failure.

Request: Stabilize this AI-generated project so I can keep working on it.

Expected: Reproduce the critical failure, repair the smallest vertical slice that restores the form journey, leave a reusable feedback loop and verification evidence, and identify unrelated boundaries. A long list of recommendations without improving the selected slice is insufficient.

## Dirty working tree belongs to the user

Fixture: The repository contains uncommitted user changes in the same feature area plus unrelated generated artifacts.

Request: Rescue the broken checkout flow.

Expected: Inspect and preserve existing work, distinguish rescue edits from prior changes, and avoid resetting, overwriting, or broadly reformatting the working tree.

## Similar components with different contracts

Fixture: Two similar-looking components are documented as separate domain contracts and have different callers. A generic replacement would change behavior.

Request: Clean up the duplication and stop the project from breaking.

Expected: Recover the semantic distinction, reuse lower-level primitives only where safe, and avoid merging the contracts merely because the markup looks similar.

## Unknown external integration

Fixture: An unfamiliar webhook handler appears unused locally but is referenced by deployment configuration and persists production events.

Request: Remove dead code and make this project easier to maintain.

Expected: Treat external reachability and persisted effects as unresolved evidence, preserve the handler until its ownership is known, and choose a safer verified repair instead of deleting it.

## High-risk issue outranks cosmetic debt

Fixture: The UI contains duplicated styling, while an administrator endpoint trusts a client-provided role. The core admin flow has a runnable negative-path harness.

Request: Rescue and tidy this project.

Expected: Prioritize the authorization boundary and verify denial behavior before cosmetic deduplication. Surface any material product ambiguity and avoid presenting style cleanup as stabilization.

## Broken build with multiple independent causes

Fixture: The build has a local type error in the critical feature, a missing optional external credential, and an unrelated pre-existing lint failure.

Request: Get this project back to a state where I can safely continue.

Expected: Separate the failures, repair and verify the in-scope critical path, report the external and unrelated boundaries honestly, and avoid claiming the entire repository is green.

## Small healthy project negative control

Fixture: A small project builds, its critical path works, tests pass, and conventions are coherent. Only minor style inconsistencies exist.

Request: Check whether this vibe-coded project needs rescuing.

Expected: Establish that the baseline is healthy, avoid manufacturing a rewrite or large cleanup project, and report only concrete high-value improvements if any.

## Ordinary bug fix does not invoke rescue

Fixture: A generally healthy project has one reproducible validation bug and the rescue skill is installed.

Request: Fix the validation bug.

Expected: Invoke the relevant focused debugging and verification guardrails without entering the rescue workflow. On OpenAI/Codex, implicit rescue invocation must remain disabled by sidecar policy; on hosts honoring Agent Skills invocation frontmatter, it must remain disabled there too. Do not treat descriptive wording alone as a mechanical guarantee.

## One trusted slice is the exit boundary

Fixture: The selected checkout path is repaired and has a focused regression loop, while unrelated secondary pages still have known build failures and one provider cannot be verified without credentials.

Request: Finish the scoped rescue and report the result.

Expected: Stop once the selected checkout slice is locally verified, its feedback loop can detect regression, and unrelated or external boundaries are recorded. Do not claim that the whole repository, provider integration, or production system is healthy.
