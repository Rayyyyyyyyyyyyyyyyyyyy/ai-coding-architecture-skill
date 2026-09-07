# Journey State Guide

Read only the sections for states selected from concrete signals in the active
journey. This is not a universal UI checklist.

## Loading or slow

Show progress at the owning boundary, prevent misleading actions, and avoid
layout shifts or blank screens that hide whether work is active.

## Empty

Explain the absence in context and provide the next useful action when one
exists. Do not render a broken-looking shell or fake data.

## Error and recovery

Keep enough input and context to recover. Describe the actionable failure
without leaking sensitive internals, and provide retry only when retry is safe.

## Success

Make completion observable and leave the interface in a coherent next state.

## Repeated action

Make pending and repeated input understandable and prevent accidental client
duplication when appropriate. Consequential server-side idempotency and replay
safety belong to the trusted boundary; UI disabling does not prove at-most-once
execution.

## Long or unexpected content

Preserve meaning without clipping critical controls, overflowing containers, or
assuming a fixed language or text length.

## Responsive layout

Keep the primary action and essential information usable at the repository's
supported viewport sizes.

## Keyboard and assistive technology

Use semantic controls, associated labels, logical and visible focus, meaningful
names, and appropriate status or error announcements. Verify focus transitions
when the selected state opens, closes, validates, or completes an action.
