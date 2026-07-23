# Business Analysis Specification Document (BA) — How2Prompt Web App

This document serves as the Business Analyst (BA) specification for **How2Prompt**, detailing the functional requirements, prioritized user stories, BDD acceptance criteria, data definitions, and edge cases mapped from the Software Requirements Specification ([SRS.md](SRS.md)) and [epics.md](epics.md).

---

## 1. Project Vision & User Persona Mapping

### 1.1 Product Vision
**How2Prompt** is a keyboard-first web application designed to train and improve prompt engineering skills. It structures prompt composition around a core three-part structure: **Role, Context, and Constraints**. It utilizes empty template skeletons with inline variable pills that auto-resize dynamically as the user types, preserving standard sentence flow.

### 1.2 Persona & Access Matrix

| Feature / Action | Guest (Unauthenticated) | Member (Authenticated) | Team Lead (Authenticated Admin) |
| :--- | :---: | :---: | :---: |
| Browse Template Catalog | Yes | Yes | Yes |
| Command Palette Search | Yes | Yes | Yes |
| Fill Placeholders & Inline Edit | Yes | Yes | Yes |
| Compile & Copy to Clipboard | Yes | Yes | Yes |
| Local Draft Backup (localStorage) | Yes | Yes | Yes |
| Save Compilation Snapshot to Database | No | Yes | Yes |
| View History Drawer (max 20 entries) | No | Yes | Yes |
| Delete History Record | No | Yes | Yes |
| Define Shared Global Team Variables | No | No | Yes |

---

## 2. Epic & User Story Specifications (BDD Format)

### Epic 1: Keyboard-First Prompt Creation Workspace

#### Story 1.1: Dashboard Layout & Command Palette Search (Priority: P1)
As a Guest or Member,
I want to use a command palette to quickly search and load empty prompt templates,
So that I can select my workspace in under 50ms without using a mouse.

* **Acceptance Criteria:**
  * **Given** a user is on the homepage dashboard.
  * **When** they press the shortcut key combination `Ctrl+K`.
  * **Then** the Command Palette search overlay toggles open with focus set on the search input box.
  * **When** the user types a search query (e.g. "debug").
  * **Then** the catalog performs fuzzy-search and filters templates matching the query in title, tags, or description.
  * **When** the search results render.
  * **Then** the latency of filtering and rendering results MUST be under 50ms.
  * **When** the user selects a template card using arrow keys and presses `Enter` (or clicks the card).
  * **Then** the selected template loads onto the Variable Canvas workspace, and the Command Palette closes.

#### Story 1.2: Inline Variable Canvas Editor (Priority: P1)
As a Guest or Member,
I want to navigate and fill placeholder fields directly inside the template sentence flow,
So that I can write my prompt parameters seamlessly.

* **Acceptance Criteria:**
  * **Given** a prompt template is loaded onto the Variable Canvas.
  * **When** the workspace renders the template text.
  * **Then** placeholder fields (e.g., `{code_to_review}`, `{environment}`) render as inline text input pills styled distinctively.
  * **When** the user presses the `Tab` key.
  * **Then** the input focus cycles forward to the next inline input pill.
  * **When** they press `Shift+Tab`.
  * **Then** the focus cycles backward to the previous inline input pill.
  * **When** the user types text into an inline input pill.
  * **Then** the input pill auto-adjusts its width dynamically based on the character length typed, keeping the surrounding sentence layout natural and preventing wrap-breaking.

#### Story 1.3: Local Draft Backup & State Clear (Priority: P1)
As a Guest or Member,
I want my progress to be backed up locally and have the ability to reset the canvas,
So that I don't lose typed text on accidental refresh and can start fresh easily.

* **Acceptance Criteria:**
  * **Given** the user is typing values into template variable pills.
  * **When** the user types characters (on `change` events).
  * **Then** the client application automatically serializes and saves the draft values into browser `localStorage` keyed by template UUID.
  * **When** the user performs a hard page refresh (F5) or closes and reopens the browser tab.
  * **Then** the Variable Canvas retrieves the draft values from `localStorage` and restores them on load.
  * **When** the user presses the "Reset" button (or triggers the `Esc` hotkey).
  * **Then** the system clears all input pills on the canvas and removes the draft from `localStorage`.

#### Story 1.4: Prompt Compiler, Verification, & Copy Action (Priority: P1)
As a Guest or Member,
I want the compiler to validate my inputs and copy the compiled prompt,
So that I can immediately use it in external AI chats.

* **Acceptance Criteria:**
  * **Given** a user is editing placeholders on the Variable Canvas.
  * **When** they press `Ctrl+Enter` (or click "Hoàn thành" / "Complete").
  * **And** at least one mandatory placeholder pill is left empty.
  * **Then** the copy execution blocks, highlights the empty fields red, and automatically shifts focus to the first empty pill.
  * **Given** all mandatory placeholder pills are filled.
  * **When** they trigger the compilation.
  * **Then** the Prompt Compiler resolves variables by replacing placeholders, stripping empty optional variables, removing extra whitespaces, and copying the clean compiled prompt string to the system clipboard.
  * **And** the UI triggers a non-blocking toast notification reading "Copied!" (or "Đã sao chép!") which disappears after exactly 2 seconds.

---

### Epic 2: Authentication & Context Configurations

#### Story 2.1: Member Account Registration & Login (Priority: P2)
As a Guest,
I want to register an account and log in securely,
So that I can unlock personalized context retention and history logging.

* **Acceptance Criteria:**
  * **Given** a guest is on the Registration page.
  * **When** they submit their email, username, and password.
  * **Then** the backend Gateway verifies the email is unique, hashes the password using BCrypt, saves the user to PostgreSQL, and redirects to the Login page.
  * **Given** the user is on the Login page.
  * **When** they submit valid credentials.
  * **Then** the Spring Boot Gateway generates a secure, stateless JWT token (valid for 7 days) and returns it.
  * **When** they submit invalid credentials.
  * **Then** the Gateway responds with an `HTTP 401 Unauthorized` status wrapped in a standard RFC-7807 error detail envelope.

#### Story 2.2: Context Retention & Decoupled JWT Sessions (Priority: P2)
As a Member,
I want my authentication session to persist across visits and let me logout,
So that I remain signed in securely without constant credential entries.

* **Acceptance Criteria:**
  * **Given** a Member has successfully logged in and received a JWT token.
  * **When** the login completes.
  * **Then** the React SPA stores the token in `localStorage` and updates the React `AuthContext` to display user indicators.
  * **When** the React application makes API requests.
  * **Then** an Axios request interceptor attaches the JWT token to the `Authorization: Bearer <token>` header.
  * **When** the page is reloaded (F5) or closed and reopened.
  * **Then** the application checks `localStorage` for the token, updates context if valid, and redirects to Login if the token has expired or is invalid.
  * **When** the user clicks "Đăng xuất" (Logout).
  * **Then** the system purges the JWT token from `localStorage`, resets `AuthContext` to null, and redirects to the homepage.

#### Story 2.3: Team Variables Configuration (Priority: P2)
As a Team Lead,
I want to configure global team variables in the settings,
So that they pre-populate automatically for my team members.

* **Acceptance Criteria:**
  * **Given** a Team Lead is on the settings page.
  * **When** they create/update key-value configurations (e.g. `{ "team_coding_standards": "Use Java 17 and Spring Boot MVC pattern" }`) and click save.
  * **Then** the React SPA sends a `PUT /api/v1/users/me/variables` request.
  * **And** the Spring Boot backend updates the PostgreSQL `user_variables` table, storing the mappings inside the `variables` JSONB column.
  * **When** a Member on the same team loads a template referencing `{team_coding_standards}`.
  * **Then** the Variable Canvas queries `GET /api/v1/users/me/variables` on load.
  * **And** pre-populates the corresponding variable pill with the Team Lead's configuration automatically.

---

### Epic 3: Stateless Optimization & History Management

#### Story 3.1: Resilient Upstream Prompt Optimization (Priority: P2)
As a Member,
I want prompt optimization requests to be resilient and fail gracefully,
So that transient network glitches do not disrupt my workflow.

* **Acceptance Criteria:**
  * **Given** a Member requests a prompt optimization.
  * **When** the Spring Boot Gateway routes the request to the Python FastAPI Prompt Service `/api/v1/agent/optimize`.
  * **And** the FastAPI service interacts with LiteLLM and encounters transient exceptions (rate limits, network timeouts).
  * **Then** the service triggers exponential backoff retries using Tenacity (maximum of 3 attempts).
  * **When** the upstream connection fails terminally.
  * **Then** the system returns an RFC-7807 Bad Gateway error payload (`HTTP 502`, `LLM_PROVIDER_ERROR`) detailing the provider failure.

#### Story 3.2: Execution History Logger & Reload (Priority: P2)
As a Member,
I want my compiled prompts to be saved automatically,
So that I can browse past completions and reload them onto the Canvas.

* **Acceptance Criteria:**
  * **Given** an authenticated Member compiles and copies a prompt (Story 1.4).
  * **When** the compilation succeeds.
  * **Then** the React SPA triggers a background `POST /api/v1/history` containing the `template_id`, `variable_snapshot` (JSONB), and `generated_prompt`.
  * **And** the Spring Boot Gateway saves the log to PostgreSQL inside a `@Transactional` block.
  * **When** the Member opens the Quick-History Drawer.
  * **Then** the system displays the newest history snapshots (retrieved via `GET /api/v1/history`, returning up to 20 entries sorted by `created_at DESC` using a composite index).
  * **When** the Member clicks a history card.
  * **Then** the Variable Canvas reloads the template and restores all pill input fields to the exact values preserved in `variable_snapshot`.

#### Story 3.3: History Deletion (Priority: P2)
As a Member,
I want to delete specific logs from my history,
So that I can keep my history feed clean.

* **Acceptance Criteria:**
  * **Given** a Member is viewing history rows in the Quick-History Drawer.
  * **When** they click the "Delete" icon on a row.
  * **Then** the React SPA sends a `DELETE /api/v1/history/{id}` request.
  * **And** the Spring Boot service deletes the record from the `history` table.
  * **And** the UI immediately filters out the deleted card from the list.

---

## 3. System Integration & Data Schemas

### 3.1 Database JSONB Column Formats

#### `user_variables` (Table Column `variables` JSONB)
Stores flexible team/individual variables. Mapped by `user_id`.
```json
{
  "team_coding_standards": "Use Java 21, Spring Boot, and follow controller-service-repository patterns.",
  "project_target_env": "production",
  "deployment_region": "us-east-1"
}
```

#### `history` (Table Column `variable_snapshot` JSONB)
Stores a key-value snapshot of placeholder values filled at copy time.
```json
{
  "role": "Senior QA Engineer",
  "code_to_review": "public void saveUser(...) { ... }",
  "team_coding_standards": "Use Java 21, Spring Boot, and follow controller-service-repository patterns."
}
```

### 3.2 Relational Indices
To ensure sub-50ms query speeds:
* **Composite Index**: `history(user_id, created_at DESC)` - optimized for fetching the history list in the drawer.
* **Unique Constraints**: `users(email)` - blocks registration duplication.

---

## 4. Edge Cases, Exception Scenarios & Error Mapping

### 4.1 Empty Variable Validation Block
When `Ctrl+Enter` or "Hoàn thành" is pressed:
1. Locate all template variables matching `{variable_name}` syntax.
2. If any matching input pill is not present in local state or contains only whitespace:
   * Block clipboard write.
   * Add a `.has-error` CSS class to the empty pill (rendering a red border).
   * Focus the first empty pill automatically.
   * Return focus to typing.

### 4.2 RFC-7807 Error Envelope Standard
All REST APIs MUST serialize exceptions in compliance with RFC-7807.
* **502 Bad Gateway Example (Upstream LLM failure)**:
  ```json
  {
    "type": "https://how2prompt.com/errors/llm-provider-error",
    "title": "Bad Gateway",
    "status": 502,
    "detail": "The upstream LLM provider timed out after 5 seconds.",
    "instance": "/api/v1/agent/optimize",
    "error_code": "LLM_PROVIDER_ERROR"
  }
  ```
* **401 Unauthorized Example (JWT expired)**:
  ```json
  {
    "type": "https://how2prompt.com/errors/unauthorized",
    "title": "Unauthorized",
    "status": 401,
    "detail": "JWT token is expired or signature is invalid.",
    "instance": "/api/v1/history",
    "error_code": "UNAUTHORIZED_ACCESS"
  }
  ```

### 4.3 Technical Calculations (Frontend Width resizing)
* **Auto-resize Input Width calculation**: To calculate the dynamic width of an input pill without sentence wrapping glitches, the React application uses an off-screen hidden `span` element that mirrors the typed text and inherits the input's font family, weight, and size. The dynamic width is measured from this `span` client width plus a padding buffer (e.g. `16px`) and applied to the input style `width` in real-time.
