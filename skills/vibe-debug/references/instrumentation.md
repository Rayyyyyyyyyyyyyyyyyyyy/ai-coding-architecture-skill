# Diagnostic Instrumentation

Read this reference only when diagnosis requires adding instrumentation,
retaining new observability, or observing a production environment. Existing
read-only logs, traces, and profilers do not require this branch.

## Temporary local instrumentation

- Add the narrowest signal that distinguishes the active hypotheses.
- In diagnosis-only mode, get authorization before modifying source or runtime
  configuration to add the signal.
- Do not capture secrets, credentials, session material, or unnecessary personal
  data.
- Remove temporary instrumentation before finishing, even when no fix follows.

## Production observation

Deploying or enabling new production instrumentation requires explicit
authorization. Before doing so, define:

- the observation that will support or reject the hypothesis;
- redaction rules for sensitive and personal data;
- a bound on event volume and retention;
- a stopping condition; and
- removal ownership, or an operational owner if the signal will remain.

Access to existing production evidence does not authorize configuration changes,
deployment, or a new telemetry destination.

## Durable observability

Retain new instrumentation only when the user authorized durable observability
and its redaction, volume, retention, and operational owner are explicit. Verify
that the retained signal is safe and bounded; diagnosis-only work is never
permission to leave tracing behind.
