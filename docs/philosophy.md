# Collection Philosophy

## Audience and outcome

This collection is for people who build products through AI-assisted vibe coding and should not need software-engineering vocabulary to receive responsible engineering behavior.

The desired outcome is simple:

```text
the product grows
without the repository becoming progressively harder or riskier to change
```

Hide engineering complexity from the user, not engineering responsibility from the agent.

## Quiet by default

Routine, reversible decisions should be handled without ceremony when repository evidence provides a safe answer. Reuse an existing primitive, follow the lockfile's package manager, keep local state local, and run available checks without narrating a pattern catalog.

Increase visibility only when the user needs to understand or decide a material impact, such as:

- secret or private-data exposure;
- destructive or difficult-to-reverse data changes;
- breaking compatibility;
- meaningful security or product ambiguity;
- new infrastructure, recurring cost, or operational ownership;
- verification that cannot be completed but materially affects confidence.

Explain the impact in plain language rather than teaching terminology during the task.

## Small, focused, composable skills

The seven project and engineering skills each answer a recurring question:

- `vibe-project`: How does this repository work, and—when requested—which architectural boundaries cause material problems?
- `vibe-frontend`: Is this frontend organized around maintainable boundaries, and how should a change grow into it?
- `vibe-design-context`: How can another agent recover why this repository is structured this way?
- `vibe-safe-change`: Which hidden decisions in this change could create security, data, compatibility, or operational risk?
- `vibe-verify`: What evidence supports claiming that this change actually works?
- `vibe-ux`: Can the changed user journey still be completed under its relevant real-world states?
- `vibe-debug`: What reproducible evidence identifies the failure, and—when a fix was requested—supports the smallest repair?

`vibe-handoff` is a cross-cutting transfer contract reached only at a real delegation or agent-handoff event: What is the smallest precise task state another agent needs to continue correctly?

`vibe-project` shares repository discovery between explanation and assessment. Select either mode or both from the user's request. Both preserve read-only authority and explicit evidence limits.

[Recovery](workflows/recovery.md) is a documented composition workflow for a broken repository, not another skill or a prerequisite for unfinished projects.

Do not turn one skill into a universal "be a good engineer" prompt. Add a new skill only when it has:

1. a clear and recurring agent failure mode;
2. observable expected behavior;
3. behavioral evaluation cases;
4. a concern independent enough to compose with existing skills;
5. value that does not require the user to understand specialist vocabulary.

## Signals, not universal patterns

Repository conventions and task context come before the collection's preferences. Patterns are responses to concrete signals, not requirements to apply everywhere.

The collection must not require one architecture, framework, language, state library, directory structure, test-coverage percentage, or abstraction style.

## Repository-resident context

Code records what currently exists. Architecture context records non-obvious reasons and boundaries that future work must preserve.

Keeping both in the repository reduces dependence on one conversation, model, agent, or human memory. Documentation must still earn its existence: record durable decision-making context, not source-code narration.

## Model and agent portability

`SKILL.md` is the canonical behavioral source. Write it in model-neutral language that describes outcomes and decisions instead of vendor-specific tools.

Host metadata may differ, but it must not redefine core behavior. Use the closest supported mechanism when optional capabilities are unavailable without claiming the same invocation or interoperability guarantees.

Cross-agent evaluations should allow implementation and wording to differ while requiring consistent safety, boundary, scope, and verification outcomes.

## Evidence-driven growth

The collection contains eight skills: one dual-mode project entry, six engineering skills, and one handoff contract. Recovery is documented composition. Add project bootstrap, dependency, auth, data-boundary, database-change, release, or other skills only when behavioral evidence shows that an existing concern is overloaded or a distinct failure mode recurs.

Do not create skills to complete a taxonomy.

## Delegation-event handoffs

`vibe-handoff` owns task-state transfer only when work is actually delegated,
transferred, resumed, or returned to an agent consumer. It does not own
implementation quality and does not run for a human-only completion report.
Its [canonical skill](../skills/vibe-handoff/SKILL.md) is the single source for
native A2A semantics, collection labels, identifier preservation, and the
non-native fallback. Architecture context remains the durable repository source;
handoffs reference it rather than replacing it.

## Documented workflows

User-selected documented workflows may coordinate several guardrails for a recognizable project moment such as rescuing a brittle repository. Keep them explicit, thin, and outcome-oriented: they select scope and sequence but do not redefine the underlying engineering responsibilities. A rescue reaches its minimum outcome when one selected vertical slice is verified, has a reusable feedback loop, and leaves unrelated or external boundaries explicit; it does not certify the whole repository.

An explicit workflow must not turn a broad request into permission for destructive cleanup, framework replacement, production mutation, or unrelated modernization. Its value should be visible in repository state and verification evidence, not only in a generated audit report.
