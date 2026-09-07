# Explain Project — implementation scope

Status: Scope accepted in conversation on 2026-09-07; local Markdown tracking configured; implemented and locally evaluated. Research: [repo explanation](../../docs/repo-explanation-research.md).

## Outcome

Create `explain-project` so a user can quickly understand an existing, partially developed repository in natural language: what the product does, which parts own which responsibilities, how representative data flows work, and what is incomplete or unverified.

## Deliverables

- A focused `skills/explain-project/SKILL.md` and matching `agents/openai.yaml`.
- Discovery and ownership entries in the existing README and routing documentation.
- Behavioral case specifications and recorded isolated fixture evaluations.

## Behavior

1. Inspect the current working tree, including relevant uncommitted changes. Follow applicable repository instructions without substituting agent-facing documents for implementation evidence or the human explanation.
2. Establish the main applications, entry points, responsibilities, data stores, and external boundaries before tracing representative flows. Adapt to web, CLI, frontend-only, worker, or multi-application repositories instead of assuming a universal architecture.
3. Trace user actions or other real inputs through reachable handling, transformation, authoritative decisions, storage, and outputs. Explain data lifetime and ownership in product language.
4. Distinguish implementation and wiring from execution evidence: mock data, code without a confirmed caller, planned behavior, statically traced behavior, and observed runtime results must remain distinguishable.
5. Lead with a short human explanation, then progressively explain responsibilities and representative flows. Use selective source links and an optional small diagram where useful. State coverage and unresolved boundaries rather than claiming exhaustive understanding.
6. Keep the walkthrough read-only. Report discovered gaps without repairing code or synchronizing architecture records. A user request to save the explanation authorizes the requested human-facing document only. Existing safe read-only runtime observations may support the explanation; environment changes and external side effects remain subject to the user's authorized scope.
7. Finish the initial walkthrough once major responsibilities, representative input/output paths, storage and external boundaries, and coverage limits are explained. Follow-up questions deepen the requested area rather than restarting a full survey.

## Boundaries

`architecture-context` remains responsible for durable, non-obvious design intent. `explain-project` owns human understanding of current implementation. The walkthrough does not automatically enter rescue, architecture repair, issue creation, or implementation workflows.

Use normal skill discovery with a precise explanation-oriented description. Keep the new skill self-contained; it must not require the author's personal Matt skill installation.

## Acceptance evidence

Run an independent agent against isolated raw repository fixtures, without giving it expected findings. Record the prompt, available skill, fixture state, response, observed commands and mutations, scoring, and limitations under the existing evaluation convention.

- A frontend fixture with stale design prose, local state, and an unused persistence service: explain the actual path and refresh behavior without claiming persistence or modifying the fixture.
- A multi-application fixture with an API and a background worker: cover the main responsibilities and synchronous/background paths, distinguish configured code from observed runtime behavior, and make no production claims.

Also specify cases for unavailable credentials, absent agent documents, dynamic registration, uncommitted wiring changes, scoped follow-up questions, and a discovered defect. Format validation is separate from behavioral evidence.

## Review

Review the new skill and integration changes separately for repository standards and this accepted scope. Preserve earlier uncommitted skill changes and exclude unrelated edits from this feature's review and commit.
