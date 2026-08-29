# AI Coding Architecture Contract

## Core Principle

Build the application as a maintainable, composable, and scalable system rather than a collection of page-specific implementations.

Prioritize:

1. Reuse existing implementations.
2. Compose existing components.
3. Extract repeated logic.
4. Introduce abstractions only when there is a concrete architectural reason.

Follow this order:

**Reuse → Compose → Extract → Abstract**

Do not prematurely generalize code or introduce abstractions based only on hypothetical future requirements.

---

# 1. Architecture

Use a **feature-based, component-driven architecture**.

Organize code around product features and domain concepts rather than only technical file types.

Prefer:

```text
features/
  trip/
    components/
    hooks/
    services/
    schemas/
    types/
    utils/

  itinerary/
    components/
    hooks/
    services/
    schemas/
    types/

  map/
    components/
    hooks/
    services/

shared/
  components/
  hooks/
  utils/
  types/

lib/
  api/
  adapters/
  validation/
```

Avoid dumping unrelated application code into generic directories such as:

```text
components/
utils/
helpers/
misc/
common/
```

unless the code is genuinely shared across multiple features.

Feature-specific code should remain inside the feature that owns it.

---

# 2. Separation of Concerns

Maintain clear boundaries between:

```text
UI
↓
Application / Feature Logic
↓
Domain Model
↓
Services / Adapters
↓
External APIs / Data Sources
```

UI components must not directly depend on raw external API responses.

External data should first be normalized into internal domain models.

Preferred flow:

```text
External Data
↓
Parser / Adapter
↓
Validation
↓
Normalized Domain Model
↓
Feature Logic
↓
UI Components
```

For example:

```text
PDF
Excel
Markdown
JSON
Text
External API
↓
Adapters / Parsers
↓
Canonical Trip Schema
↓
Application
↓
UI
```

The UI should primarily consume the canonical internal schema rather than knowing where the original data came from.

---

# 3. Schema-First Development

Use a **schema-first architecture** for important domain data.

Define the internal data structure before implementing UI logic that depends on it.

Prefer strongly typed schemas.

Examples:

```text
Trip
Day
ItineraryItem
Location
Transportation
Accommodation
Reservation
Expense
Note
```

All external input formats should be converted into these internal structures.

Do not allow multiple incompatible representations of the same domain concept to spread across the codebase.

Use runtime validation where external data enters the system.

Preferred tools may include:

```text
TypeScript
Zod
Valibot
JSON Schema
```

depending on the existing project stack.

---

# 4. UI Framework and Design System

Use the project's existing UI framework and design system.

Examples may include:

```text
shadcn/ui
Radix UI
Material UI
Ant Design
Chakra UI
Headless UI
Tailwind CSS
```

Do not recreate primitive UI components when an equivalent component already exists in the chosen UI library.

Before implementing:

```text
Button
Dialog
Modal
Drawer
Dropdown
Select
Tabs
Tooltip
Popover
Accordion
Card
Input
Checkbox
Radio
Toast
Navigation
Date Picker
```

check whether the UI framework already provides the primitive.

Prefer wrapping or composing existing primitives instead of rebuilding them.

---

# 5. Design-System Driven Development

Use consistent design tokens for:

```text
spacing
typography
colors
border radius
shadows
breakpoints
container sizes
z-index
animation duration
```

Avoid arbitrary values unless there is a strong visual reason.

Bad:

```text
margin-top: 17px
border-radius: 13px
padding-left: 23px
```

Prefer values defined by the design system.

Do not introduce page-specific visual conventions that conflict with the rest of the application.

---

# 6. Component-Driven UI

Components should be:

```text
small
focused
reusable
composable
predictable
easy to test
```

Follow the **Single Responsibility Principle**.

A component should primarily represent one UI responsibility.

Avoid God Components.

A component that handles all of the following simultaneously is usually too large:

```text
data fetching
API transformation
business rules
state management
routing
rendering
modal logic
form validation
analytics
responsive behavior
```

Split responsibilities when appropriate.

---

# 7. Composition Over Configuration

Prefer composition over components with excessive configuration.

Avoid large components controlled by many boolean props.

Bad:

```tsx
<TravelCard
  compact
  editable
  showMap
  showPrice
  showWeather
  showActions
  horizontal
  mobile
  highlighted
/>
```

Prefer composable structures:

```tsx
<TravelCard>
  <TravelCard.Header />
  <TravelCard.Location />
  <TravelCard.Schedule />
  <TravelCard.Price />
  <TravelCard.Actions />
</TravelCard>
```

Use **Compound Component Pattern** when several related UI parts belong to the same conceptual component.

Do not create excessive compound-component APIs for trivial components.

---

# 8. Props

Keep component APIs small and intentional.

Avoid excessive boolean props.

Avoid passing entire application state into deeply nested components.

Prefer semantic props:

```tsx
status="confirmed"
```

instead of:

```tsx
isConfirmed
isPending
isCancelled
```

when the states are mutually exclusive.

Avoid prop drilling across many component layers.

Consider:

```text
composition
feature-level context
local context
state stores
```

when appropriate.

Do not use global state simply to avoid passing one or two props.

---

# 9. Hooks and Composables

Extract reusable stateful logic into hooks or composables.

React examples:

```text
useTrip
useItinerary
useReservation
useMapNavigation
useWeather
useExpenseSummary
```

Vue examples:

```text
useTrip
useItinerary
useReservation
```

Hooks/composables should contain reusable behavior, state coordination, or feature logic.

UI components should focus primarily on:

```text
rendering
interaction
composition
```

Do not extract every small function into a hook.

A hook should have a meaningful behavioral responsibility.

---

# 10. Business Logic

Keep business logic outside presentational components whenever practical.

Business rules should live in:

```text
domain functions
feature services
hooks/composables
use cases
selectors
dedicated utilities
```

depending on complexity.

Avoid embedding important business rules inside JSX/template conditionals.

Bad:

```tsx
{trip.days.length > 3 &&
 totalPrice > 10000 &&
 user.country === "TW" &&
 !trip.isDomestic &&
 ...
}
```

Prefer:

```tsx
const shouldShowTravelNotice = getTravelNoticeVisibility(...)
```

when the rule carries meaningful domain logic.

---

# 11. Services

Use a service layer for interactions with external systems when those interactions contain meaningful application behavior.

Examples:

```text
TripService
WeatherService
GeocodingService
ReservationService
StorageService
```

Services should provide application-friendly interfaces.

Avoid leaking vendor-specific API formats throughout the application.

---

# 12. Adapter Pattern

Use adapters around external dependencies.

Examples:

```text
GoogleMapsAdapter
MapboxAdapter
GeminiAdapter
OpenAIAdapter
SupabaseTripRepository
LocalStorageTripRepository
PdfTripParser
ExcelTripParser
MarkdownTripParser
```

External systems should be replaceable without requiring widespread UI changes.

Adapter output should match internal domain contracts.

---

# 13. Dependency Direction

High-level application logic should not depend directly on low-level vendor implementation details.

Prefer:

```text
Feature
↓
Internal Interface
↓
Adapter
↓
Vendor
```

rather than:

```text
Feature
↓
Vendor SDK everywhere
```

Use dependency inversion when it creates a useful boundary.

Do not create interfaces for every class or function merely for theoretical purity.

---

# 14. Repository Pattern

Use repository abstractions when the application has meaningful persistence logic.

Examples:

```text
TripRepository
UserRepository
ItineraryRepository
```

Possible implementations:

```text
SupabaseTripRepository
LocalTripRepository
IndexedDbTripRepository
```

Repositories should expose domain-oriented operations rather than raw database operations where practical.

Example:

```text
getTripById()
saveTrip()
deleteTrip()
listTrips()
```

Do not use repository abstractions for trivial one-off requests unless they provide clear value.

---

# 15. Avoid Premature Abstraction

Do not introduce abstraction solely because code might theoretically need it later.

Create abstractions when they solve at least one concrete problem:

```text
duplicated implementation
external dependency isolation
complex business logic
multiple implementations
testing boundaries
frequently changing rules
repeated UI structure
```

Avoid speculative generalization.

Three similar lines of code are often cheaper than the wrong abstraction.

Prefer duplication temporarily when the correct abstraction is not yet clear.

Refactor once the pattern becomes visible.

---

# 16. Existing Code First

Before adding a new:

```text
component
hook
utility
helper
service
type
schema
context
store
adapter
repository
```

search the existing codebase for equivalent or closely related functionality.

Reuse or extend existing implementations where appropriate.

Do not create duplicate concepts with slightly different names.

Avoid situations such as:

```text
TripCard
TravelCard
TripInfoCard
JourneyCard
TripSummaryCard
```

when they represent essentially the same UI concept.

If overlapping implementations already exist, consolidate them when doing so is safe and improves clarity.

---

# 17. DRY Without Over-Abstraction

Follow DRY for meaningful repeated knowledge, not merely repeated syntax.

Do not extract code just because two blocks look similar.

Extract when they represent the same underlying concept or behavior.

Prefer:

```text
semantic reuse
```

over:

```text
syntactic reuse
```

---

# 18. Naming

Names should describe domain meaning.

Prefer:

```text
TripDay
ItineraryItem
ReservationStatus
TripSummary
AccommodationCard
TransportationSegment
```

Avoid vague names:

```text
Data
Info
Manager
Helper
Thing
Common
Utils2
ComponentNew
FinalComponent
```

Hooks must generally follow:

```text
useXxx
```

Handlers should describe the event or action:

```text
handleTripSave
handleReservationDelete
handleDateChange
```

Booleans should read naturally:

```text
isLoading
isEditable
hasReservation
canDelete
shouldCollapse
```

---

# 19. Types

Avoid `any` unless absolutely unavoidable.

Prefer explicit domain types.

Do not repeatedly redefine similar inline object types.

Shared domain models should have canonical definitions.

External API types and internal domain types should remain separate when their structures or responsibilities differ.

Do not force internal application architecture to match vendor API structures.

---

# 20. State Management

Keep state as local as possible.

Use this preference order:

```text
local component state
↓
feature-level shared state
↓
URL state
↓
server/cache state
↓
global application state
```

depending on the nature of the data.

Do not place everything in a global store.

Distinguish:

```text
server state
client state
UI state
derived state
URL state
```

Avoid storing derived values when they can be calculated reliably from existing state.

---

# 21. Derived State

Prefer deriving state rather than synchronizing duplicated state.

Bad:

```text
trip
tripDays
tripDayCount
tripHasDays
```

when these values can all be derived from `trip`.

Avoid unnecessary `useEffect` synchronization.

Use memoization only when there is a measurable or structurally meaningful reason.

---

# 22. Effects

Avoid using effects as the default solution for application logic.

Effects should primarily synchronize React/application state with external systems.

Do not use effects to calculate values that can be derived during rendering.

Avoid chains such as:

```text
state changes
↓
effect updates state
↓
another effect updates state
↓
another effect triggers request
```

Prefer explicit data flow.

---

# 23. Forms

Use a consistent form architecture.

Keep:

```text
form state
validation
submission
domain transformation
API interaction
```

clearly separated.

Use schema-based validation when appropriate.

Validation errors should be predictable and structured.

Do not scatter validation rules across UI components.

---

# 24. Error Handling

Handle errors intentionally.

Distinguish between:

```text
validation errors
network errors
authentication errors
permission errors
not-found errors
unexpected system errors
```

Do not silently swallow errors.

Avoid broad empty catches:

```ts
try {
  ...
} catch {}
```

User-facing errors should provide useful recovery paths when possible.

Developer-facing errors should retain enough diagnostic context.

---

# 25. Loading and Empty States

Every asynchronous feature should explicitly consider:

```text
loading
success
empty
error
partial data
```

Do not treat empty data as an error unless the domain requires it.

Prefer skeletons or contextual loading states over blocking the entire page.

---

# 26. Responsive Design

Build responsive behavior intentionally.

Prefer responsive layouts driven by component constraints rather than separate mobile and desktop implementations.

Avoid duplicating entire page trees for mobile and desktop unless truly necessary.

Design mobile layouts based on information priority.

Use progressive disclosure for secondary information.

---

# 27. Progressive Disclosure

Do not display every possible piece of information at once.

Prioritize:

```text
primary task
primary content
secondary metadata
advanced controls
rare actions
```

Use expandable sections, dialogs, drawers, tabs, or contextual controls when appropriate.

UI complexity should increase only when the user asks for more detail.

---

# 28. Accessibility

Use semantic HTML.

Preserve keyboard navigation.

Ensure interactive elements are actually interactive elements.

Prefer:

```html
<button>
<a>
<input>
<label>
<nav>
main
section
```

over clickable generic containers.

Use ARIA attributes only when semantic HTML is insufficient.

All meaningful interactive controls should have accessible labels.

---

# 29. Navigation and URL State

Important navigational state should be represented in the URL when useful.

Examples:

```text
trip ID
selected day
active tab
filters
search query
map focus
```

Do not put temporary visual state into the URL unnecessarily.

Pages should remain reloadable and deep-linkable where appropriate.

---

# 30. API Boundaries

Keep API communication centralized by feature or service.

Do not call external APIs from arbitrary deeply nested UI components.

Normalize API errors and response formats at the boundary.

UI should consume application-level data structures.

---

# 31. Data Transformation

Perform data normalization once near the system boundary.

Avoid repeatedly transforming the same raw data in multiple components.

Preferred:

```text
API
↓
Adapter
↓
Normalized Model
↓
Application
```

Not:

```text
API
↓
Component A transformation
↓
Component B different transformation
↓
Component C another transformation
```

---

# 32. Parsing Architecture

For user-provided travel documents, treat each input format as a parser/adapter.

Example:

```text
Input
├── PDF
├── Excel
├── CSV
├── Markdown
├── JSON
├── Plain Text
└── Images
     ↓
Parser
     ↓
Intermediate extraction
     ↓
Validation
     ↓
Canonical Trip Schema
```

Parsing logic must not be coupled directly to UI rendering.

Adding support for a new input type should ideally require a new parser rather than changes throughout the application.

---

# 33. External AI Output

Treat AI-generated responses as untrusted external input.

AI output should:

```text
follow a defined schema
be validated before use
have fallback handling
support partial failure
```

Never assume model output always perfectly follows instructions.

Prefer structured output over parsing prose.

Example:

```text
AI
↓
Structured JSON
↓
Schema Validation
↓
Normalization
↓
Domain Model
```

---

# 34. AI Prompt Boundary

Prompts should live outside UI components.

Centralize prompts by feature.

Separate:

```text
prompt templates
model configuration
response schemas
domain normalization
UI
```

Do not concatenate large prompts inside event handlers.

Prompt changes should not require rewriting presentation components.

---

# 35. Utility Functions

Utility functions should:

```text
do one thing
have deterministic behavior when possible
use clear names
avoid hidden global state
```

Do not create a giant `utils.ts`.

Prefer focused modules:

```text
date.ts
currency.ts
geo.ts
trip-format.ts
reservation.ts
```

Feature-specific utilities belong inside the feature.

---

# 36. Comments

Comments should explain:

```text
why
constraints
non-obvious tradeoffs
external quirks
```

Avoid comments that merely restate the code.

Bad:

```ts
// increment count
count++;
```

Good:

```ts
// The API occasionally returns duplicate segments.
// Deduplicate here before calculating itinerary duration.
```

---

# 37. File Size and Complexity

Do not use line count as an absolute rule, but treat unusually large files as a signal.

When a component or module becomes difficult to understand without scrolling through many unrelated responsibilities, evaluate whether it should be decomposed.

Refactor based on conceptual boundaries rather than arbitrary file-size limits.

---

# 38. Testing Boundaries

Prioritize tests around:

```text
business rules
data normalization
parsers
schema validation
critical user flows
complex hooks/composables
important adapters
```

Avoid tests that only assert implementation details.

UI tests should focus on user-visible behavior.

Domain logic should ideally be testable without rendering the UI.

---

# 39. Refactoring Rule

Do not rewrite working architecture unnecessarily.

When changing existing code:

1. Understand the current implementation.
2. Identify the smallest useful boundary.
3. Preserve behavior.
4. Refactor incrementally.
5. Avoid unrelated rewrites.

Do not perform large architectural rewrites unless explicitly requested or clearly necessary.

---

# 40. Dependency Rule

Before installing a new package:

1. Check whether the project already has equivalent functionality.
2. Check whether the framework or standard library already solves the problem.
3. Evaluate maintenance cost.
4. Prefer mature and focused dependencies.
5. Avoid adding large dependencies for trivial functionality.

Do not install a package simply to save a few lines of straightforward code.

---

# 41. Performance

Do not optimize blindly.

Prioritize:

```text
clear architecture
correct data flow
avoiding unnecessary requests
avoiding unnecessary rerenders
lazy loading meaningful heavy features
efficient lists
image optimization
cache strategy
```

Measure before introducing complicated performance optimizations.

Do not use memoization everywhere by default.

---

# 42. Rendering Strategy

Choose rendering strategy intentionally based on feature needs.

Consider:

```text
SSR
SSG
CSR
server components
client components
streaming
```

depending on the framework.

Do not mark large application trees as client-side solely because one small interaction requires client state.

Keep client boundaries as small as practical.

---

# 43. Security Boundaries

Never expose secrets in client code.

Keep:

```text
API keys
service-role credentials
private tokens
server secrets
```

on trusted server boundaries.

Validate user-controlled input.

Treat uploaded files, URLs, AI output, and external API responses as untrusted input.

---

# 44. Canonical Domain Model

There must be one preferred representation for core domain entities.

For the travel application, favor a canonical model similar to:

```text
Trip
├── metadata
├── travelers
├── dateRange
├── destinations
├── days[]
│   └── itineraryItems[]
├── accommodations[]
├── transportation[]
├── reservations[]
├── expenses[]
├── notes[]
└── sourceMetadata
```

Different data sources should map into this model.

Components should not implement source-specific logic such as:

```text
if source === "excel"
if source === "pdf"
if source === "markdown"
```

unless the source itself is part of the user-facing behavior.

---

# 45. Feature Ownership

Each feature should own its:

```text
UI
business logic
hooks
types
schemas
feature services
feature utilities
```

until those pieces are genuinely reusable elsewhere.

Move code into `shared` only after multiple features actually need it.

Do not place code into shared directories merely because it might become reusable later.

---

# 46. Public Feature APIs

Where useful, expose a small public API for each feature.

Example:

```ts
features/trip/index.ts
```

may expose:

```text
TripCard
TripPage
useTrip
TripSchema
```

Other features should avoid reaching into arbitrary internal implementation files.

Prefer:

```ts
import { TripCard } from "@/features/trip"
```

over deep coupling:

```ts
import { TripCard } from "@/features/trip/components/internal/cards/TripCard"
```

when the project architecture supports public feature APIs.

---

# 47. No Architecture Theater

Do not introduce patterns merely to demonstrate architectural sophistication.

Avoid unnecessary combinations such as:

```text
Factory
Repository
Service
Manager
Facade
Provider
Controller
Adapter
```

for a simple operation.

Every architectural layer must justify its existence through:

```text
clear responsibility
replaceability
testability
complexity reduction
reuse
dependency isolation
```

Prefer the simplest architecture that preserves clear boundaries.

---

# 48. Implementation Decision Rule

When deciding whether to create something new, ask in this order:

```text
Does an equivalent already exist?
        ↓
Can the existing implementation be reused?
        ↓
Can it be composed?
        ↓
Is the behavior actually repeated?
        ↓
Is there a clear domain concept?
        ↓
Would an abstraction reduce coupling or complexity?
        ↓
Create the abstraction.
```

---

# 49. Code Review Checklist

Before considering implementation complete, verify:

- Existing components were searched before new ones were created.
- Existing hooks/utilities/services were searched before duplication.
- UI primitives come from the existing design system where possible.
- Components have clear responsibilities.
- No obvious God Component was introduced.
- Business logic is not unnecessarily embedded in presentation code.
- External data is normalized at system boundaries.
- Domain types are explicit.
- No unnecessary `any` was introduced.
- State is kept as local as practical.
- Derived state is not unnecessarily duplicated.
- Effects are not being used for derived calculations.
- External APIs are isolated behind reasonable boundaries.
- Important AI responses are schema validated.
- Input parsers output the canonical domain model.
- Responsive behavior was considered.
- Loading, empty, and error states exist where required.
- Accessibility was considered.
- No unnecessary dependency was added.
- No speculative abstraction was introduced.
- Naming reflects domain meaning.
- The implementation matches existing architectural conventions.

---

# 50. Final Rule

When multiple implementations are valid, prefer the solution with:

```text
fewer concepts
clearer boundaries
smaller public APIs
less duplication
lower coupling
higher composability
easier replacement
easier testing
```

Do not optimize for cleverness.

Optimize for code that another developer, or another AI coding agent, can understand and safely extend later.