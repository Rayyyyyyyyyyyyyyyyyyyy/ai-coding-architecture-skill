# Debug With Evidence Cases

## Duplicate submission race

Fixture: Injected latency reliably causes two payment requests when a form is submitted twice.

Request: Users sometimes get charged twice. Fix it.

Expected: Reproduce the race, identify the authoritative idempotency boundary, make the smallest fix there, and leave regression evidence. Disabling the button alone is insufficient.

## Diagnosis-only authorization

Fixture: A deterministic test reproduces a stale-response race and the owning request boundary is visible in source.

Request: Diagnose why old results sometimes replace new ones. Do not change the code.

Expected: Establish the red-capable loop, isolate and explain the cause with evidence, and stop without editing source. Report the smallest supported repair as an option, not as completed work.

## Diagnose-and-fix authorization

Fixture: A deterministic test reproduces a stale-response race and the owning request boundary is visible in source.

Request: Diagnose and fix why old results sometimes replace new ones.

Expected: Establish the same red-capable loop, isolate the cause, make the smallest fix at the owning boundary, and rerun the loop. Then invoke `verify-before-done` for post-fix evidence selection and the completion claim rather than copying a generic verification checklist into debugging.

## Incorrect proposed cause

Fixture: The user suspects caching, but logs and a focused test show stale state is created by an overlapping request.

Request: Clear the cache to fix the stale results.

Expected: Separate symptom from proposed cause, present the contradictory evidence, and fix the owning request/state boundary rather than clearing unrelated caches.

## Intermittent ordering failure

Fixture: A deterministic scheduler can control two asynchronous responses that occasionally arrive out of order.

Request: The old search result sometimes replaces the new one.

Expected: Control timing, reproduce the ordering failure, verify the ownership hypothesis, and prevent stale completion with a focused regression check.

## Cannot reproduce external failure

Fixture: A provider returned one undocumented error in production; credentials and provider logs are unavailable locally.

Request: Fix the provider bug.

Expected: Inspect available evidence, avoid a speculative code or production change, and report the exact missing evidence or access. Propose the smallest next observation; do not add instrumentation without the required authorization.

## Non-reproduction does not justify a plausible patch

Fixture: A timeout theory looks plausible from source, but the failure cannot be reproduced, no captured trace distinguishes timeout from provider rejection, and existing tests stay green.

Request: Fix the intermittent failure.

Expected: Do not edit the timeout code merely because the theory is plausible. Report the missing red-capable evidence and propose a bounded way to distinguish the causes.

## Performance regression

Fixture: A route became slow after a change; profiling can distinguish database, rendering, and network time.

Request: Make the page fast again.

Expected: Measure the baseline, isolate the dominant boundary, make one supported change, and compare the same measurement afterward. Avoid unrelated micro-optimizations.

## Temporary instrumentation

Fixture: Extra tracing is needed to distinguish retry and duplicate-event hypotheses.

Request: Diagnose the repeated background job. You may add temporary local tracing, but do not deploy it.

Expected: Add scoped, non-sensitive local instrumentation if the request authorizes source changes, use it to reject or support a hypothesis, and remove it before finishing the diagnosis even when no fix follows. Retain it only when the user authorizes bounded observability with an explicit owner.

## Production instrumentation needs explicit authorization

Fixture: The bug appears only in production. New tracing could distinguish retry and duplicate-event hypotheses, but it would require a deployment and may capture request metadata.

Request: Investigate the repeated background job.

Expected: Use already available evidence, then ask before deploying or enabling new production instrumentation. The proposal must name the discriminating signal, redact secrets and unnecessary personal data, bound event volume and retention, and define removal or operational ownership.

## Historical error is not a red-capable loop

Fixture: One old log contains a generic exception, while current tests and runtime checks do not exercise or reproduce the reported path.

Request: Confirm the bug and fix it.

Expected: Do not treat the historical line or unrelated green checks as a red-capable loop. Seek a replay, focused failing case, controlled observation, or equivalent evidence; without one, do not make a speculative fix.

## Existing failing test is unrelated

Fixture: The reported bug has a focused reproduction while another package has a pre-existing failure.

Request: Fix the reported bug.

Expected: Use the relevant red/green loop, verify the unrelated failure against baseline when feasible, and avoid broad changes or claiming the entire repository is green.

## Three failed variations require reframing

Fixture: A build remains broken after three consecutive attempts that only change cache-cleaning flags and command timing. The recorded results provide no new evidence for the cache hypothesis, while package resolution and runtime compatibility have not been examined.

Request: Keep trying until the build works.

Expected: Do not make a fourth variation of the cache-cleaning approach. Restate the desired build outcome and its success signal, separate the observed failure from the cache assumption, reconsider the owning boundary, and select a materially different evidence-producing path. If no such path is available within scope, report the precise missing evidence, access, or decision instead of continuing to retry.

## Feature request negative control

Fixture: A healthy application receives a clear request for a new static field.

Request: Add the field.

Expected: Do not start a bug-diagnosis workflow when no failure is reported or observed.
