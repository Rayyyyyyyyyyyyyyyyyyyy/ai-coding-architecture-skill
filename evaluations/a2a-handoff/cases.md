# A2A Handoff Cases

## Completed code change

Fixture: An agent changed two files, ran a focused test and build successfully, and has a commit identifier.

Request: Hand this completed task to another agent.

Expected: Invoke `a2a-handoff` at this actual transfer and let it be the single source for native fields or fallback labels. With native A2A use `TASK_STATE_COMPLETED`; with the text fallback use `completed`. Return generated outputs through supported artifacts and distinguish changed files from observed checks using the collection's `change` and `evidence` labels only where the host permits names or metadata. Do not interchange native and fallback state names or invent protocol fields. Omit a message when no response is required and avoid narrating the work chronology.

## Missing product decision

Fixture: Implementation cannot continue until the owner chooses whether deleting an account also deletes shared team data.

Request: Hand off the blocked task.

Expected: With native A2A use `TASK_STATE_INPUT_REQUIRED`; with the text fallback use `input-required`. Preserve current generated work through supported artifacts and send one precise message describing the decision and its concrete alternatives. Do not interchange native and fallback state names, invent an enum, or mark the task failed or completed.

## Destructive operation needs approval

Fixture: An authenticated agent has prepared a production cleanup that will irreversibly delete retained backups, but execution requires the owner's explicit approval.

Request: Hand off the task before execution.

Expected: With native A2A use `TASK_STATE_AUTH_REQUIRED`; with the text fallback use `auth-required`. Preserve the prepared plan, request only the exact destructive-operation approval, and do not execute the cleanup. Do not use input-required merely because the response comes from a person, and do not place credentials in the handoff.

## Credentials required

Fixture: The code and local checks are ready, but production deployment requires authentication credentials.

Request: Continue the release through another agent.

Expected: With native A2A use `TASK_STATE_AUTH_REQUIRED`; with the text fallback use `auth-required` because authentication is missing. Distinguish local evidence from production verification. Do not treat missing product content or a product choice as auth-required, interchange native and fallback state names, place credentials in the handoff, or claim production completion.

## Failed execution

Fixture: A deterministic build failure remains after in-scope attempts, and resolving it requires an unrelated framework migration.

Request: Return the task state.

Expected: With native A2A use `TASK_STATE_FAILED`; with the text fallback use `failed`. Attach the reproducible failure through a supported artifact or durable reference, and label the migration as `remaining` only as a collection convention. Do not interchange native and fallback state names or disguise failure as a recommendation list.

## Critical result belongs in an artifact

Fixture: An agent produced a schema migration plan and compatibility constraints needed by the next agent.

Request: Send an A2A update.

Expected: Store the plan and constraints in durable artifacts or repository files; use a message only for necessary interaction. The critical plan must not exist solely in transient status prose.

## Context continuity

Fixture: The host supplies an existing `Task.id` and `contextId`; the follow-up `Message.taskId` references that task.

Request: Hand the task to another compatible agent.

Expected: Preserve `Task.id` and `contextId`, keep `Message.taskId` as a reference to `Task.id`, and reject or surface mismatches rather than silently creating unrelated context.

## No native A2A runtime

Fixture: The host can exchange plain text only.

Request: Produce a compact agent-facing handoff.

Expected: Use the A2A-inspired semantic fallback with `task`, `status`, only material `artifacts`, and an optional `message`. Explicitly treat the fallback as a readable convention, not an A2A payload. Do not invent transport or interoperability claims or emit a large pseudo-protocol envelope.

## Native and fallback state representation

Fixture: The same missing-product-fact handoff is run once with a native A2A 1.0 runtime and once through the text-only fallback.

Request: Transfer both blocked tasks using the supported representation.

Expected: The native `TaskStatus.state` uses `TASK_STATE_INPUT_REQUIRED` and never the lowercase fallback alias. The text fallback uses `input-required` and never a `TASK_STATE_*` value. Any cross-representation state name is a hard failure.

## Ordinary implementation without delegation

Fixture: One agent is implementing and reporting a focused change directly to a person. No other agent or session will consume the result.

Request: Add the requested behavior and explain what changed.

Expected: Do not invoke the handoff contract merely because implementation finished. Report naturally to the person and reserve A2A semantics for an actual delegation, transfer, resume, or agent-consumer event.

## Human-only negative control

Fixture: A person asks for a beginner-friendly explanation and no agent will consume the result.

Request: Explain what changed.

Expected: Answer naturally and concisely for the person. Do not force an A2A object dump into a human-only response.
