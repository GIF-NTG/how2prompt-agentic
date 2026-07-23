# Software Requirements Specification (SRS) — How2Prompt Web App

This document integrates all requirements from the PRD, technical specifications, architecture decisions, and epic/story breakdowns into a single Software Requirements Specification (SRS) for the **How2Prompt** platform.

---

## 1. Introduction & Vision

### 1.1 Product Vision
**How2Prompt** is a minimal web application designed to train and improve users' prompt engineering skills through direct practice with standard prompt structures. It enforces a core three-part structure: **Role, Context, and Constraints**.

Unlike tools that provide static pre-written prompts, How2Prompt offers **Empty Templates** with placeholder fields. Users interact directly with these templates, filling in their context inline, and use keyboard-first operations to compile, optimize, and copy high-quality prompts to their clipboard.

### 1.2 User Personas & Jobs To Be Done (JTBD)
* **Guest (Unauthenticated User):** Wants to browse templates, fill in placeholders, and quickly copy prompt outputs without the friction of account creation.
* **Member (Authenticated User):** Wants to automatically save prompt history snapshots to reload and reuse past prompt configurations, as well as configure personalized/team-wide global variables.
* **Team Lead (Authenticated Admin/Manager):** Wants to define organization-wide variables that automatically populate into team member templates to enforce standardized coding or environment constraints.

### 1.3 Non-Goals
* No direct AI chat interface (e.g. ChatGPT/Gemini window) inside How2Prompt itself. The app is dedicated to prompt drafting and copy-to-clipboard.
* No Cloud synchronization or history persistence for Guests.
* No automated template generation or AI-based template recommendations for users.

---

## 2. Key User Journeys

* **UJ-1: Guest fills inline template and copies prompt using keyboard-first flow.**
  * *Context:* Nam, a developer, wants to quickly generate a debug prompt.
  * *Journey:* Open homepage ➔ Press `Ctrl+K` to open the Command Palette search ➔ Type "debug" and press `Enter` to load the template ➔ Press `Tab` to navigate through empty placeholder pills ➔ Type inline values directly (the input box auto-resizes dynamically) ➔ Press `Ctrl+Enter` to resolve variables, compile the prompt, and copy it to the clipboard ➔ Paste into an external AI chat.
* **UJ-2: Team Lead configures shared team variables.**
  * *Context:* Minh, a QA lead, wants to enforce a team-wide coding guideline variable.
  * *Journey:* Log in ➔ Navigate to Settings ➔ Define global team variable `{team_coding_standards}` ➔ Save (stores as JSONB in DB). Developers on the same team open templates referencing this variable, and it pre-populates automatically.
* **UJ-3: Member accesses history drawer to reload past prompt settings.**
  * *Context:* Chi, a developer, wants to re-run a prompt used yesterday.
  * *Journey:* Log in ➔ Open the Quick-History Drawer ➔ Browse the list of the last 20 compiled prompts ➔ Click a history card ➔ The Canvas reloads the template and restores all variables to their exact past values.

---

## 3. System Requirements

### 3.1 Functional Requirements (FRs)
* **FR-001 (Authentication):** Users MUST authenticate via stateless JWT tokens on all API calls (except public templates list retrieval).
* **FR-002 (Template Catalog):** The homepage MUST display public templates as cards, showing the title, description, and tags (e.g. `#debugging`, `#marketing`).
* **FR-003 (Command Palette):** The application MUST support a fuzzy-search Command Palette triggered by `Ctrl+K` to find and load templates with under 50ms latency.
* **FR-004 (Variable Canvas):** The loaded template MUST render placeholders as inline input pills. The canvas MUST support keyboard navigation (`Tab` and `Shift+Tab`) to cycle focus through editable variable pills.
* **FR-005 (Inline Auto-Resize):** Inline variable input fields MUST auto-resize their width dynamically based on the character length typed, preserving sentence flow.
* **FR-006 (Draft Auto-Save):** The client application MUST automatically save draft variable inputs to `localStorage` per template, persisting state across page refreshes (F5).
* **FR-007 (Input Validation):** If the user triggers copy execution while mandatory variable pills remain empty, the copy action MUST block and automatically shift focus to the first empty pill.
* **FR-008 (Prompt Compiler):** Resolving variables compiles the prompt by replacing placeholders, stripping empty optional variables, cleaning up extra whitespaces, and copying the result to the clipboard.
* **FR-009 (Copy Feedback):** Copying to the clipboard triggers a non-blocking toast notification reading "Copied!" for 2 seconds.
* **FR-010 (Stateless Prompt Optimization):** The backend MUST delegate prompt optimizations to a stateless Python Prompt Service that formats the template and checks structured schemas.
* **FR-011 (JSONB User Variables):** The backend MUST support GET/PUT routes for users to store global variable configurations in PostgreSQL JSONB fields.
* **FR-012 (History Snapshots):** Copy execution for Members automatically pushes a snapshot of the variables and the compiled prompt to the PostgreSQL database (maximum 20 items per user).
* **FR-013 (History Reloading):** Clicking a card in the history list MUST reload the associated template and restore all placeholder values on the Variable Canvas.
* **FR-014 (History Management):** Members can delete individual prompt history entries from the database.

### 3.2 Non-Functional Requirements (NFRs)
* **NFR-1 (UI Performance):** Key press actions and inline input auto-resizing MUST execute with sub-50ms latency. The React workspace First Contentful Paint (FCP) MUST be under 200ms, and Time to Interactive (TTI) under 500ms.
* **NFR-2 (Resilient LLM Connections):** All upstream AI model requests made by the Python service MUST execute with exponential backoff retries (maximum 3 attempts) via Tenacity.
* **NFR-3 (Error Handling Standards):** In the event of terminal upstream LLM failures, the system MUST return RFC-7807 Bad Gateway details (`HTTP 502`, `LLM_PROVIDER_ERROR`). Validation errors must also return standard RFC-7807 JSON details.
* **NFR-4 (Security & Encryption):** User passwords MUST be benched and hashed using BCrypt. All JWT transmission MUST be encrypted over secure HTTPS channels.
* **NFR-5 (Cross-Browser Compatibility):** The client application must function correctly on Chrome, Safari, Edge, and Firefox (across desktop and mobile dimensions).

---

## 4. Technical Design & Databases

### 4.1 3-Tier Decoupled Architecture
The platform is split into three decoupled, single-responsibility layers:
1. **Frontend (React SPA):** Handles UI layout, keyboard bindings, input auto-resizing, and local draft synchronization.
2. **Gateway (Spring Boot):** Handles JWT validations, Postgres SQL migrations, business logic routing, and acts as the secure intermediary API gateway.
3. **Prompt Service (FastAPI):** A stateless Python service executing LLM prompt optimizations using LiteLLM. It maintains no DB connection or disk state; all guidelines are passed dynamically.

```
[React SPA Client] <---(HTTPS / JWT)---> [Spring Boot Gateway] <---(REST / JSON)---> [FastAPI Prompt Service]
                                                  |
                                           [PostgreSQL DB]
```

### 4.2 Database Schema
The relational schema uses PostgreSQL with UUID primary keys. Personal/team variables and prompt snapshots are stored inside JSONB columns:

* **`users`**
  * `id` (UUID, Primary Key)
  * `email` (VARCHAR, Unique)
  * `username` (VARCHAR)
  * `password_hash` (VARCHAR)
  * `created_at` (TIMESTAMP)
* **`teams`**
  * `id` (UUID, Primary Key)
  * `name` (VARCHAR)
* **`templates`**
  * `id` (UUID, Primary Key)
  * `title` (VARCHAR)
  * `description` (TEXT)
  * `raw_template` (TEXT) - Prompts with `{variable_name}` syntax
  * `tags` (VARCHAR[])
* **`user_variables`**
  * `user_id` (UUID, Foreign Key referencing `users.id`)
  * `variables` (JSONB) - Flexible key-value configurations (e.g. `{ "team_coding_standards": "..." }`)
* **`history`**
  * `id` (UUID, Primary Key)
  * `user_id` (UUID, Foreign Key referencing `users.id`)
  * `template_id` (UUID, Foreign Key referencing `templates.id`)
  * `variable_snapshot` (JSONB) - Snapshot of pills filled at copy time
  * `generated_prompt` (TEXT) - Compiled output prompt
  * `created_at` (TIMESTAMP) - Indexed with user_id: `(user_id, created_at DESC)`

### 4.3 REST API Endpoints & Error Payload
All endpoints are kebab-cased under the `/api/v1` namespace:

* **Auth Endpoints:**
  * `POST /api/v1/auth/register` - Create account
  * `POST /api/v1/auth/login` - Authenticate & receive JWT token (7-day validity)
* **Template Endpoints:**
  * `GET /api/v1/templates` - Retrieve public template cards
* **Variable Endpoints:**
  * `GET /api/v1/users/me/variables` - Retrieve saved user/team variable settings
  * `PUT /api/v1/users/me/variables` - Store updated variable configurations
* **History Endpoints:**
  * `GET /api/v1/history` - Retrieve user's prompt history list (sorted by newest, max 20 entries)
  * `POST /api/v1/history` - Log a new prompt compilation snapshot
  * `DELETE /api/v1/history/{id}` - Remove a specific history snapshot
* **Agent Endpoints:**
  * `POST /api/v1/agent/optimize` - Stateless route called by the Gateway to process and optimize prompt models via FastAPI.

#### RFC-7807 Error Envelope Example (502 Bad Gateway):
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

---

## 5. Detailed Epics & User Stories

### Epic 1: Keyboard-First Prompt Creation Workspace
* **Story 1.1: Dashboard Layout & Command Palette Search**
  * *Acceptance Criteria:* Pressing `Ctrl+K` toggles a fuzzy-search Command Palette search box. Selecting an option loads the template onto the Canvas. Search responses load under 50ms.
* **Story 1.2: Inline Variable Canvas Editor**
  * *Acceptance Criteria:* Placeholders render as inline input text pills. Tabbing focuses through consecutive pills. Inputs auto-adjust their width to match the length of the string typed.
* **Story 1.3: Local Draft Backup & State Clear**
  * *Acceptance Criteria:* Changes to variables auto-save to `localStorage`. Page reload (F5) restores the draft. Pressing the "Reset" hotkey or button clears current inputs.
* **Story 1.4: Prompt Compiler, Verification, & Copy Action**
  * *Acceptance Criteria:* Pressing `Ctrl+Enter` checks variable inputs. If mandatory fields are empty, the copy action blocks, highlights the empty fields red, and focus is shifted to the first empty pill. Otherwise, variables are compiled, whitespaces are formatted, and the compiled string is written to clipboard alongside a 2-second "Copied!" toast.

### Epic 2: Authentication & Context Configurations
* **Story 2.1: Member Account Registration & Login**
  * *Acceptance Criteria:* Registers users and hashes passwords via BCrypt. Login checks password and issues a 7-day JWT token. Invalid authentication responds with a standard RFC-7807 401 Unauthorized envelope.
* **Story 2.2: Context Retention & Decoupled JWT Sessions**
  * *Acceptance Criteria:* JWT is saved to `localStorage` and sent with requests via Axios client interceptors. F5 reload restores user context. Logging out clears the JWT and redirects back to homepage.
* **Story 2.3: Team Variables Configuration**
  * *Acceptance Criteria:* Team Leads can save key-value variable mappings. The backend gateway stores configuration objects in PostgreSQL JSONB column `user_variables.variables`. When members load templates containing team variables, values are pre-populated automatically.

### Epic 3: Stateless Optimization & History Management
* **Story 3.1: Resilient Upstream Prompt Optimization**
  * *Acceptance Criteria:* Spring Boot routes requests to Python FastAPI `/api/v1/agent/optimize`. The FastAPI client manages LiteLLM calls. Transient errors trigger up to 3 retries (exponential backoff). Hard timeouts return standard RFC-7807 Bad Gateway error detail envelopes.
* **Story 3.2: Execution History Logger & Reload**
  * *Acceptance Criteria:* Member copy commands trigger gateway requests to `POST /api/v1/history` under a `@Transactional` boundary, saving snapshot values inside `history.variable_snapshot` (JSONB). Drawer displays up to 20 past snapshots sorted by newest. Clicking a card restores the template and values to the Canvas.
* **Story 3.3: History Deletion**
  * *Acceptance Criteria:* Clicking delete on history drawer rows executes `DELETE /api/v1/history/{id}` and updates UI immediately.

---

## 6. Glossary
* **Empty Template:** A predefined prompt outline containing fixed instructions and variable placeholder slots.
* **Variable Pill:** An inline input block within the template body where users type custom parameters.
* **Command Palette:** A keyboard-triggered search drawer (`Ctrl+K`) used to search and swap template canvas workspaces.
* **Prompt Compiler:** The utility that replaces variables within a template, formats whitespaces, and writes the output string to clipboard.
* **JSONB Columns:** PostgreSQL binary JSON format used to store variable mappings and snapshot logs dynamically without tabular structure bloat.
* **RFC-7807:** The internet standard (RFC-7807) detailing uniform JSON error shapes in HTTP responses.
