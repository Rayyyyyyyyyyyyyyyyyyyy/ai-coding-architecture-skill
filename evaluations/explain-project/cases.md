# Project Explanation Cases

Run current cases with `vibe-project` in explain mode. This directory retains its
historical name for existing fixture and execution-record links; recorded runs
under `runs/` describe the old skill and are not evidence for the merged one.

Use the shared [evaluation method](../README.md). Observe the explanation and any mutations, not whether the agent repeats skill headings. Keep fixture expectations out of the evaluated agent's prompt. A passing static walkthrough is not runtime verification of the fixture.

## Frontend with local state and unused persistence

Fixture: [frontend](fixtures/frontend/) has a static form and an unused API client. Its historical architecture note describes server persistence; the active form uses in-memory state. No local storage is used.

Request: 我剛接手這個做到一半的專案。請用白話說明它的架構、資料怎麼走、目前哪些地方還沒接好；不用改程式。

Expected: Explain the form-to-view path and loss of newly added items on reload. Distinguish the unused API client and historical persistence claim from active wiring. Do not claim an existing or verified backend, write files, or repair the missing connection. Use natural product language with optional evidence links and state that runtime was not observed if it was not exercised.

## API and background worker

Fixture: [background](fixtures/background/) contains a static order page, a registered HTTP API, SQLite-backed order and job storage, and a worker that calls a notification provider. The page polls order status; provider credentials are unavailable.

Request: 我想快速看懂這個專案。請說明整體架構，從建立訂單到通知完成，資料如何流動、存在哪裡，以及哪些事情目前還不能確定。先不要改動。

Expected: Account for the page, API, worker, database, and external notification service. Trace order creation, enqueue, worker processing, status persistence, and polling to the page. Explain authoritative data ownership and the distinction between accepting an order and completing a notification. Label provider and runtime uncertainty without claiming deployment or delivery success. Do not mutate the project or contact the provider.

## No agent-facing documents

Fixture: The background fixture has no AGENTS.md or CLAUDE.md.

Request: 帶我看懂這個 repo 的架構。

Expected: Explain it from entry points, registration, callers, and storage. Do not require or create agent documentation before proceeding.

## Indirect registration

Fixture: An application registers route modules dynamically. A handler has no direct function-call match but is reachable through the route table.

Request: 使用者送出資料之後，哪個地方接手？

Expected: Resolve the registered path before describing reachability. Do not classify the handler as dead or disconnected solely because a textual caller search returns no match.

## Uncommitted wiring change

Fixture: The committed frontend calls a persistence client. In the current working tree, that caller has been replaced with local state; the client still exists.

Request: 以現在的版本為準，新增資料會存去哪裡？

Expected: Inspect and explain the current working tree, identify the consequential wiring difference when relevant, and preserve all uncommitted work. Do not describe only the committed version.

## Scoped follow-up

Fixture: A previous walkthrough covered the applications and order flow; the user now asks about the notification retry path.

Request: 如果通知服務沒回應，這筆訂單會怎樣？

Expected: Inspect and explain the affected failure and retry path, including any uncertainty, without restarting the entire repository survey or inventing retry behavior. Do not implement a retry.

## Requested human-facing document

Fixture: The user has received a source-grounded walkthrough and wants to preserve it.

Request: 把這份白話解說存成 docs/project-tour.md，方便同事看。

Expected: Save the requested explanation with its evidence limits. Do not update agent instructions, architecture decisions, application code, or unrelated documentation.

## Library rather than an application

Fixture: A parsing library exposes public functions and has examples and tests but no web UI, server, database, or deployment configuration.

Request: 我不熟這個 repo，請說明它怎麼處理輸入和產生結果。

Expected: Explain consumer input, public API, transformation, and output with evidence. Do not impose a frontend/API/database pipeline or speculate about deployment.

## Implementation request negative control

Fixture: A well-understood application needs a specific form validation change.

Request: 修正這個欄位的必填驗證。

Expected: Do not automatically activate a whole-project walkthrough. Use the applicable implementation workflow for the authorized change.
