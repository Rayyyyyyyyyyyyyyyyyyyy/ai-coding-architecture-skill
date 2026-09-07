# Experience Completeness Cases

## Async form submission

Fixture: A form submits to an API and currently handles only immediate success.

Request: Finish the profile form.

Expected: Map asynchronous latency, recoverable failure, and state-changing submission to pending, error/recovery, success, and repeated-action UI. Preserve input and verify those states without redesigning the page or inventing unrelated empty-state work.

## Empty collection

Fixture: A dashboard renders a table frame with no rows and no guidance when a new account has no records.

Request: Make the dashboard usable for first-time users.

Expected: Provide a contextual empty state and the appropriate first action while preserving the established table and page primitives. Do not insert fake records.

## Destructive retry

Fixture: A delete request can time out after the server commits the deletion.

Request: Add retry to the error state.

Expected: Recognize duplicate side-effect risk, keep the user informed, and define the needed reconciliation or idempotency guarantee for the trusted boundary. Route server-side replay safety through `safe-change`; do not implement or claim it as a UI guarantee.

## Consequential submission splits experience from enforcement

Fixture: A purchase button can be clicked repeatedly while a request is pending, and the server has no documented idempotency policy.

Request: Make checkout handle repeated clicks.

Expected: Complete the pending and repeated-action experience using the existing UI owner, identify the missing server guarantee, and route that guarantee to `safe-change`. Do not claim disabling the button prevents duplicate charges or silently invent a server policy in this skill.

## Long translated content

Fixture: A card and action row work in English but overflow with long localized labels and user content.

Request: Support the translated copy.

Expected: Preserve readable content and reachable controls using existing responsive primitives; do not truncate critical meaning or create a one-language special case.

## Keyboard-operated dialog

Fixture: A custom dialog opens visually but has no semantic name, initial focus, focus containment, Escape behavior, or focus return.

Request: Make the confirmation flow complete.

Expected: Prefer the repository's accessible dialog primitive; verify keyboard opening, action, cancellation, and focus return rather than only visual appearance.

## Slow list replacement

Fixture: Changing a filter clears the current list for several seconds and permits conflicting repeated changes.

Request: Improve the filtering experience.

Expected: Represent pending state at the correct owner, keep the interface understandable, handle stale responses or repeated actions, and avoid synchronized duplicate state.

## Local synchronous toggle negative control

Fixture: An existing semantic checkbox toggles local display density with no asynchronous work or persistence.

Request: Add a second density option.

Expected: Implement and verify the focused interaction without manufacturing loading, retry, empty, or global error infrastructure.

## Cosmetic change negative control

Fixture: An existing accessible, responsive button changes only its border color.

Request: Apply the new color token.

Expected: Do not invoke a journey-state, responsive, keyboard, or site-wide accessibility audit. Verify the scoped visual-token change at its actual boundary.

## Signal selects one relevant state

Fixture: A synchronous client-side list filter can validly produce zero matches; it performs no network work and changes no persistent data.

Request: Make filtering understandable when nothing matches.

Expected: Add and verify the contextual empty result state. Do not add loading, retry, duplicate-submission, server idempotency, or production-security work because those signals are absent.

## Authorization remains an external policy input

Fixture: A UI must display an existing server `403` response, but the role policy and enforcement are already owned by the server.

Request: Complete the denied experience.

Expected: Represent the denial accessibly and provide an appropriate next action using the existing policy. Do not redefine roles, move enforcement to the client, or treat the UI state as authorization proof.

## Backend-only change negative control

Fixture: A server-side parser changes an internal canonical format with no user-facing behavior change.

Request: Update the parser.

Expected: Do not invoke an experience-state audit. Verify the parser at its actual boundary.

## Assessment of missing states

Fixture: A profile form lacks pending and recoverable-error states, with an existing request-state owner and runnable local evidence.

Request: Look at this flow and tell me which states are missing.

Expected: Present a state checklist with evidence, impact, and proposed scope. Do not edit UI, tests, or configuration, and do not invoke implementation-completion verification. Wait for an implementation request.

## Completion with an unresolved product choice

Fixture: A failed submission can retain a draft locally or persist it to the user's account; no draft storage policy exists.

Request: Complete this form's loading and error experience.

Expected: Complete routine authorized pending and error feedback using existing conventions. Present the unresolved persistent-draft choice before implementing it; do not invent storage behavior or block unrelated authorized states.

## Assessment followed by implementation approval

Fixture: The user has received a checklist of missing pending and error states for a form.

Request: Implement those two states using the existing form conventions.

Expected: Implement and verify the agreed states without asking for the same approval again or adding unrelated journey work.
