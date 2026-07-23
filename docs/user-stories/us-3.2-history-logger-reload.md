# User Story 3.2: Execution History Logger & Reload

## Overview
- **Epic**: Epic 3: Stateless Optimization & History Management
- **Priority**: P2
- **User Persona**: Member (Authenticated)

## Story Description
- **As a** Member,
- **I want to** my compiled prompts to be saved automatically,
- **So that** I can browse past completions and reload them onto the Canvas.

## Acceptance Criteria (BDD Format)
- **Given** an authenticated Member compiles and copies a prompt (Story 1.4).
- **When** the compilation succeeds.
- **Then** the React SPA triggers a background `POST /api/v1/history` containing the `template_id`, `variable_snapshot` (JSONB), and `generated_prompt`.
- **And** the Spring Boot Gateway saves the log to PostgreSQL inside a `@Transactional` block.
- **When** the Member opens the Quick-History Drawer.
- **Then** the system displays the newest history snapshots (retrieved via `GET /api/v1/history`, returning up to 20 entries sorted by `created_at DESC` using a composite index).
- **When** the Member clicks a history card.
- **Then** the Variable Canvas reloads the template and restores all pill input fields to the exact values preserved in `variable_snapshot`.

## Technical Implementation Details
- **Frontend Layer**:
  - Automatically triggers a non-blocking background API call: `POST /api/v1/history` on successful compilation & copy if the user is authenticated.
  - Quick-History Drawer layout: A slide-out panel listing history entries.
  - History selection trigger: Clicking an entry fetches template configuration, clears current Variable Canvas state, and populates variables with the snapshot JSON values.
- **Backend API Layer (Spring Boot)**:
  - REST Endpoints under `/api/v1/history`:
    - `POST /api/v1/history` - Saves execution snapshots. Uses `@Transactional` configuration on the service level.
    - `GET /api/v1/history` - Fetches current user's history list (limits response to maximum 20 entries, sorted by `created_at DESC`).
- **Database Layer**:
  - `history` (or `prompt_histories`) table:
    - `id` (UUID, Primary Key)
    - `user_id` (UUID, Foreign Key referencing `users.id`)
    - `template_id` (UUID, Foreign Key referencing `templates.id`)
    - `variable_snapshot` (JSONB) - Stores key-value snapshot of variable values (prevents EAV bloat as per [how2prompt-agentic/CLAUDE.md](how2prompt-agentic/CLAUDE.md)).
    - `generated_prompt` (TEXT) - Compiled output prompt.
    - `created_at` (TIMESTAMP)
  - **Relational Indices**:
    - Composite Index: `history(user_id, created_at DESC)` optimized for fetching the history list in the drawer under 50ms query speeds.

## Verification & Testing
- Authenticate as a Member, load a template, fill variable pills, and compile/copy the prompt. Confirm that a background HTTP request to `POST /api/v1/history` is dispatched and succeeds.
- Check the database table `history` to verify that values are saved in the `variable_snapshot` JSONB column.
- Open the Quick-History Drawer, verify that it lists the newly created entry at the top, and displays up to 20 entries.
- Click on a history card and verify that the canvas loads the template and pre-fills all input fields with the snapshot data.
- Refer to [how2prompt-agentic/agent/BA.md](how2prompt-agentic/agent/BA.md), [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md), and [how2prompt-agentic/docs/epics.md](how2prompt-agentic/docs/epics.md) for full system specifications.
