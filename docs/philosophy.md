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

Each skill should answer one recurring engineering question:

- `coding-architecture`: How should this feature grow into the existing codebase?
- `architecture-context`: How can another agent recover why this repository is structured this way?
- `safe-change`: Which hidden decisions in this change could create security, data, compatibility, or operational risk?

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

Host metadata and integrations may differ, but they must not redefine core behavior. If an agent lacks an optional capability, it should use the closest available method rather than abandon the guardrail.

Cross-agent evaluations should allow implementation and wording to differ while requiring consistent safety, boundary, scope, and verification outcomes.

## Evidence-driven growth

The current foundation contains three skills. Add project bootstrap, dedicated verification, dependency, auth, data-boundary, or database-change skills only when behavioral evidence shows that an existing concern is overloaded or a distinct failure mode recurs.

Do not create skills to complete a taxonomy.
