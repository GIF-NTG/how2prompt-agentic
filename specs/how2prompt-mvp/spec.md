# Feature Specification: how2prompt-mvp

**Feature Branch**: `how2prompt-mvp`

**Created**: 2026-07-22

**Status**: Draft

**Input**: User description: "Build the MVP of how2prompt platform, including React frontend, Spring Boot backend, Postgres database, and FastAPI prompt optimizer service."

---

## User Scenarios & Testing

### User Story 1 - Create and Copy Prompt (Priority: P1)
The primary user (software engineer) logs in, searches for a template, loads it, enters variable values, and copies the compiled prompt using the keyboard in under 3 seconds.

**Why this priority:** This is the core loop of the application. Without prompt assembly and keyboard-first copying, the application has no viable value proposition.

**Independent Test:** Run the frontend, load the "C# Code Review" template, tab to the `{code_to_review}` pill, paste a snippet of code, press `Ctrl+Enter`, and verify that the compiled text is copied to the clipboard.

**Acceptance Scenarios:**
1. **Given** a logged-in user on the dashboard, **When** they press `Ctrl+K`, **Then** the Command Palette opens displaying a template search bar.
2. **Given** the Command Palette is open, **When** they type "review" and hit `Enter`, **Then** the "C# Code Review" template loads onto the Variable Canvas.
3. **Given** the template is loaded on the Canvas, **When** they press `Tab`, **Then** the focus moves to the first editable Variable Pill (`{code_to_review}`).
4. **Given** the user has entered text into the variable pills, **When** they press `Ctrl+Enter`, **Then** the variables are resolved, empty optional variables are stripped, the assembled prompt is copied to the clipboard, and a notification toast is shown.

---

### User Story 2 - Configure Team Variables (Priority: P2)
The Team Lead logs in and defines organization-wide variables so that they are automatically propagated to all team member templates.

**Why this priority:** Allows standardization of prompts across a team (e.g. coding guidelines, environment targets).

**Independent Test:** Log in as Team Lead, set global variable `{team_coding_standards}` in Settings. Log in as a developer, load a template containing `{team_coding_standards}`, and verify the input field is pre-populated with the Team Lead's value.

**Acceptance Scenarios:**
1. **Given** a Team Lead in Settings, **When** they update `{team_coding_standards}` and save, **Then** the Spring Boot database stores this value in `user_variables` as JSONB.
2. **Given** a developer opening a template, **When** the template loads, **Then** the Variable Canvas queries the API and auto-populates the `{team_coding_standards}` pill with the team's saved string.

---

### User Story 3 - Quick-History Drawer (Priority: P2)
A user accesses their history to reload a previously compiled prompt with its variables.

**Why this priority:** Enables developers to quickly re-run prompts with past context without re-typing.

**Independent Test:** Copy a prompt, open the Quick-History Drawer, verify the prompt snapshot is listed, click it, and confirm the canvas re-loads the exact template and variable values.

**Acceptance Scenarios:**
1. **Given** a successfully copied prompt, **When** `Ctrl+Enter` is clicked, **Then** a background POST API call saves the snapshot to PostgreSQL `history`.
2. **Given** the history drawer is opened, **When** the user clicks a history card, **Then** the canvas loads the saved template and restores all variable snapshot values.

---

### Edge Cases
- **Empty Mandatory Variables:** If a user copies a prompt where a mandatory variable is empty, the copy action must block and focus the empty pill.
- **Upstream LLM Timeout:** If the Python agentic optimizer fails to respond within 5 seconds, the Spring Boot gateway must return an RFC-7807 Bad Gateway error and the frontend must show an error alert.

---

## Requirements

### Functional Requirements
- **FR-001:** Users MUST authenticate via stateless JWT tokens on all API calls.
- **FR-002:** The system MUST support fuzzy search in the Command Palette (`Ctrl+K`) with latency under 50ms.
- **FR-003:** The Variable Canvas MUST support keyboard navigation (`Tab` and `Shift+Tab`) to cycle through variable pills.
- **FR-004:** The system MUST strip empty optional variables and clean up extra whitespaces before copying to the clipboard.
- **FR-005:** The backend MUST store user-defined variables in a PostgreSQL JSONB column mapped by `user_id`.
- **FR-006:** The system MUST automatically save a snapshot of resolved variables on copy to a `history` table (maximum 20 items per user).
- **FR-007:** The Python prompt service MUST optimize inputs and output a structured JSON containing the template and variables.

### Key Entities
- **User:** Represents the developer (username, password hash, team reference).
- **Team:** Collection of users sharing templates.
- **Template:** A reusable prompt skeleton (name, content text, list of tags).
- **Variable Mapping:** User configurations stored as JSONB.
- **History Snapshot:** Log record of execution (user reference, template reference, variables snapshot).

---

## Success Criteria

### Measurable Outcomes
- **SC-001:** Prompt copy-to-clipboard action completes in under 3 seconds using only the keyboard.
- **SC-002:** Command Palette search returns results in under 50ms.
- **SC-003:** First Contentful Paint (FCP) of the React workspace is under 200ms, and Time to Interactive (TTI) is under 500ms.
- **SC-004:** Upstream LLM rate limit and connection errors are successfully retried up to 3 times before returning an HTTP 502 error.
