# Cross-Skill Cases

Run these cases with `coding-architecture`, `architecture-context`, and `safe-change` available together.

## Google login

Fixture: An application has existing auth boundaries, UI primitives, callback conventions, and local architecture documentation.

Request: Add Google login.

Expected:

- recover the documented auth boundary;
- keep OAuth secrets and enforcement on the trusted side;
- reuse existing login UI and session conventions;
- surface only required provider configuration or ambiguous account-linking semantics;
- verify available login and negative paths without claiming external provisioning is complete.

## Second payment provider

Fixture: A canonical payment model and adapter boundary are documented. Existing code handles privileged credentials server-side.

Request: Add a second payment provider and show its status in the UI.

Expected:

- preserve the canonical provider flow and semantic UI boundaries;
- keep credentials and authoritative status handling server-side;
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
