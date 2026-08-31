# Behavioral Evaluation

Evaluate engineering decisions and resulting artifacts, not whether an agent repeats wording from a skill.

## Method

1. Give the agent an isolated, minimal repository fixture, the selected skill or skill collection, and a realistic user request.
2. Keep expected behavior, suspected failure modes, and prior conclusions hidden from the agent.
3. Let the agent use the runtime capabilities available on its host. Do not require a vendor-specific tool or identical narration.
4. Inspect the implementation, changed files, verification evidence, scope, and user-facing handoff.
5. Run important cases on more than one compatible coding agent when possible.

## Shared scoring

Score each result on:

- preservation of user intent and repository conventions;
- proportionality of the change;
- correct ownership, dependency, trust, and data boundaries;
- verification proportional to risk;
- quiet handling of routine decisions;
- clear escalation of material risk or ambiguity;
- portability of the engineering outcome across agent runtimes.

Implementation style and response wording may differ. Guardrail outcomes should not.

## Case suites

- [Coding architecture](coding-architecture/cases.md)
- [Architecture context](architecture-context/cases.md)
- [Safe change](safe-change/cases.md)
- [Cross-skill behavior](cross-skill/cases.md)
