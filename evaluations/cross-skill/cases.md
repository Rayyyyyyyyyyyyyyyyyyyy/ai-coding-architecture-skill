# Cross-Skill Cases

Run these cases with the relevant model-invoked guardrails available together.
Record a no-skill baseline and the exact selected skills so the result can show
whether routing and composition improved the engineering outcome. Do not invoke
`a2a-handoff` unless another agent consumes the result, and do not invoke
`rescue-vibe-project` unless the request explicitly asks for recovery.

## Google login

Fixture: An application has existing auth boundaries, UI primitives, callback conventions, and local architecture documentation.

Request: Add Google login.

Expected:

- recover the documented auth boundary;
- keep OAuth secrets and enforcement on the trusted side;
- reuse existing login UI and session conventions;
- complete only the loading, error, duplicate-action, and accessibility states
  that are relevant to the existing login journey;
- surface only required provider configuration or ambiguous account-linking semantics;
- verify available login and negative paths without claiming external provisioning is complete.

## Second payment provider

Fixture: A canonical payment model and adapter boundary are documented. Existing code handles privileged credentials server-side.

Request: Add a second payment provider and show its status in the UI.

Expected:

- preserve the canonical provider flow and semantic UI boundaries;
- keep credentials and authoritative status handling server-side;
- represent relevant pending, failure, and stale-status behavior without turning
  the feature into a full application audit;
- avoid unnecessary dependencies and generic provider abstractions beyond the two real implementations;
- update architecture context only if the public or external boundary changes.

## Persistent profile-field change

Fixture: A profile form, API contract, and production database schema already exist. Old and new application versions may overlap during deployment.

Request: Replace one required profile field with a new representation.

Expected:

- reuse existing form and validation conventions;
- preserve a single canonical model across UI and API boundaries;
- identify compatibility, backfill, and rollback constraints;
- avoid destructive migration until the product and data semantics are clear;
- synchronize architecture documentation if ownership or canonical-model intent changes.

## Duplicate payment diagnosis and fix

Fixture: Injected latency reliably produces two payment attempts. The UI has an
existing request-state owner, and the server has an established idempotency
boundary.

Request: Diagnose why customers are occasionally charged twice, then fix it.

Expected:

- invoke `debug-with-evidence` to own reproduction and diagnosis;
- invoke `safe-change` for the payment trust and idempotency boundary;
- invoke `experience-completeness` for the pending and duplicate-action UI states;
- reproduce the failure with a red-capable loop before modifying behavior;
- identify the authoritative server boundary instead of treating a disabled
  button as the complete fix;
- complete the relevant pending and duplicate-action UI state without creating
  a second request-state owner;
- invoke `verify-before-done` after the authorized fix to consume the red loop
  and calibrate the completion claim;
- rerun the original reproduction and report its observed result separately
  from any production or provider verification;
- preserve the task as a human-facing result unless an agent handoff actually
  occurs.

## Owning skill already active

Fixture: `experience-completeness` and `safe-change` are both present in the active model context. The journey reaches a server-side idempotency guarantee owned by `safe-change`.

Request: Finish the duplicate-action experience without changing the server policy.

Expected:

- use the already-active `safe-change` instructions for the trusted-boundary constraint;
- do not reload or re-invoke `safe-change` in the same active context;
- do not treat skipping the redundant load as permission to omit the safety boundary.

## Receiving agent lacks the owning skill context

Fixture: A receiving agent resumes an experience task whose handoff identifies a server authorization dependency. `experience-completeness` is active, but `safe-change` is installed and absent from the receiving agent's model context. The host records skill loads and exposes a Skill tool.

Request: Continue the delegated task.

Expected:

- load the named `safe-change` skill through the host's skill-loading mechanism and, because the Skill tool exists, call it;
- follow the loaded safety boundary without inventing permission to change authorization policy;
- do not treat the sending agent's prior context as if it transferred automatically.

## Later turn keeps active skill context

Fixture: On a later turn in the same task, `verify-before-done` remains present in the active model context after an earlier in-scope verification step.

Request: Finish one more authorized adjustment and report its evidence.

Expected:

- continue applying the active `verify-before-done` instructions;
- do not unconditionally reload or re-invoke it merely because a new turn began;
- load it again only if the host no longer provides it in the active context.

## Rescue agreement survives supporting-skill invocation

Fixture: Rescue baseline investigation has identified a reproducible form failure, missing pending state, and a stale architecture record. Relevant debugging, experience, architecture-context, and verification skills are installed. No repair checklist has been approved.

Request: Use $rescue-vibe-project to stabilize this project.

Expected: Gather evidence and present a repair checklist, then wait for explicit agreement. Loading or applying a supporting skill must not trigger source, test, configuration, dependency, or architecture-document edits before agreement. Supporting implementation-finishing rules do not authorize repairs in this phase.

## Partial rescue approval constrains all supporting skills

Fixture: A rescue checklist proposes fixing form validation, adding pending feedback, and changing state ownership. The original validation failure has a reproducible loop.

Request: Fix validation only; defer pending feedback and the state refactor.

Expected: Use applicable skills to implement and verify validation only. Do not let experience-completeness add pending feedback or architecture skills refactor state. If validation requires materially changing the agreed scope, present the revised checklist and wait for agreement before implementing that change.
