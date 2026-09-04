---
name: debug-with-evidence
description: Diagnose failures or regressions with a red-capable feedback loop; fix only when requested. Not for feature work or speculative cleanup.
---

# Debug With Evidence

Establish evidence before changing behavior.

Load each named skill through the host mechanism; call the Skill tool when exposed. Do not reload an active skill.

## Authority

- **Diagnosis only:** inspect existing evidence and report the supported cause; no source or runtime mutation without authorization.
- **Diagnose and fix:** after isolating the cause, apply the smallest in-scope fix.

Ambiguous wording authorizes read-only diagnosis, not editing, deployment, provider mutation, production configuration, or instrumentation. Read [references/instrumentation.md](references/instrumentation.md) before adding instrumentation or observing production.

## Red-capable loop

- Separate observed symptom from proposed cause.
- Capture expected/actual behavior, path, environment, and smallest trigger.
- Reproduce with the smallest test, command, request, interaction, replay, trace, or authorized instrumentation.
- The loop must exercise the reported path, fail for the symptom before the fix, and rerun after one change. For intermittent/performance failures, use controlled scheduling, bounded trials, or the same before/after measure.
- Unrelated failures, one historical log, compilation success, or source inspection alone are not a red-capable loop.
- If no reproduction or equivalent signal exists, report the missing evidence; do not patch a plausible hypothesis.

## Isolate

- Reduce the failing path while preserving the symptom.
- Test one evidence-backed hypothesis at a time; predict the discriminating observation.
- Instrument only the owning boundary and remove temporary instrumentation per the reference.
- After rejection, obtain new evidence before forming another fix.

## Break stalled loops

Treat attempts as the same approach when they only vary parameters, timing, wording, or implementation details while keeping the same causal model, owning boundary, and evidence source.

After three consecutive unsuccessful attempts with the same approach, stop refining or repeating it. Before another attempt:

- restate the user's actual outcome and what observable evidence would count as success;
- separate established facts from assumptions, especially assumptions preserved only by the current framing;
- reconsider which boundary owns the problem and whether the task is solving a symptom instead of the cause;
- identify materially different paths, such as a different hypothesis, evidence source, owning boundary, simplification, or safe workaround;
- choose the next path for its ability to discriminate between causes, not because it is a fourth variation of the previous attempt.

A retry is materially new only when new evidence or changed external state alters what it can prove. If no materially different in-scope path remains, report the blocked outcome, the failed approach, and the smallest decision, evidence, or access needed instead of continuing the loop.

## Fix

Only in diagnose-and-fix mode:

- change the owning boundary, not an unrelated symptom layer;
- preserve contracts; exclude cleanup, dependency churn, and architecture migration;
- rerun the original loop and proportionate regression checks;
- retain bounded observability only when explicitly authorized.

After a fix, invoke `verify-before-done`. Report cause, decisive evidence, fix if authorized, and remaining uncertainty. On actual agent transfer invoke `a2a-handoff`.
