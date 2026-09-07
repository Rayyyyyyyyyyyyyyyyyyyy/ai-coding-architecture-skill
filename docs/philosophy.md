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

The six routine engineering guardrails should each answer one recurring engineering question:

- `coding-architecture`: How should this frontend change grow into the existing codebase?
- `architecture-context`: How can another agent recover why this repository is structured this way?
- `safe-change`: Which hidden decisions in this change could create security, data, compatibility, or operational risk?
- `verify-before-done`: What evidence supports claiming that this change actually works?
- `experience-completeness`: Can the changed user journey still be completed under its relevant real-world states?
- `debug-with-evidence`: What reproducible evidence identifies the failure, and—when a fix was requested—supports the smallest repair?

`a2a-handoff` is a cross-cutting transfer contract reached only at a real delegation or agent-handoff event: What is the smallest precise task state another agent needs to continue correctly?

`explain-project` is a human-facing, read-only walkthrough: What does this project currently do, how do its parts and data fit together, and what remains incomplete or unverified? It explains implementation from evidence without turning the walkthrough into architecture maintenance or rescue.

`rescue-vibe-project` is an explicit user-invoked workflow that coordinates relevant guardrails to restore one trustworthy vertical slice.

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

Host metadata and integrations may differ, but they must not redefine core behavior. `rescue-vibe-project` declares `disable-model-invocation: true` in its skill frontmatter for hosts that honor it, and OpenAI/Codex metadata separately disables implicit invocation. Other hosts may implement user-only invocation differently or not support an equivalent policy. If an agent lacks an optional capability, it should use the closest available method without claiming the same invocation or interoperability guarantees.

Cross-agent evaluations should allow implementation and wording to differ while requiring consistent safety, boundary, scope, and verification outcomes.

## Evidence-driven growth

The current collection contains six routine engineering guardrails, one human-facing project walkthrough, one delegation-event handoff contract, and one explicit rescue workflow. Add project bootstrap, dependency, auth, data-boundary, database-change, release, or other skills only when behavioral evidence shows that an existing concern is overloaded or a distinct failure mode recurs.

Do not create skills to complete a taxonomy.

## Delegation-event handoffs

`a2a-handoff` owns task-state transfer only when work is actually delegated,
transferred, resumed, or returned to an agent consumer. It does not own
implementation quality and does not run for a human-only completion report.
Its [canonical skill](../skills/a2a-handoff/SKILL.md) is the single source for
native A2A semantics, collection labels, identifier preservation, and the
non-native fallback. Architecture context remains the durable repository source;
handoffs reference it rather than replacing it.

## Explicit workflow skills

User-invoked workflow skills may coordinate several guardrails for a recognizable project moment such as rescuing a brittle repository. Keep them explicit, thin, and outcome-oriented: they select scope and sequence but do not redefine the underlying engineering responsibilities. A rescue reaches its minimum outcome when one selected vertical slice is verified, has a reusable feedback loop, and leaves unrelated or external boundaries explicit; it does not certify the whole repository.

An explicit workflow must not turn a broad request into permission for destructive cleanup, framework replacement, production mutation, or unrelated modernization. Its value should be visible in repository state and verification evidence, not only in a generated audit report.
