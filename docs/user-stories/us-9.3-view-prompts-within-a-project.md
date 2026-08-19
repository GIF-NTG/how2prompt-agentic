# User Story 9.3: View Prompts within a Project (UC-09.03)

## Overview
- **Epic**: Epic 9: Prompt Projects
- **Priority**: High
- **User Persona**: Logged-in User

## Story Description
- **As a** logged-in User who owns a project,
- **I want to** see all prompts grouped under it, filterable by template and date,
- **So that** I can find and reuse prompts from a specific piece of work.

## Acceptance Criteria (BDD Format)
- **Given** I open `/projects/{id}`
- **When** the page loads
- **Then** the frontend calls `GET /api/v1/projects/{id}/prompts`
- **And** the backend returns prompts joined through `project_prompts`, paginated (cursor-based).
- **Given** I am viewing a project's prompt list
- **When** I apply a template or date-range filter
- **Then** the list re-fetches with the filter applied as query parameters.

## Technical Implementation Details
- **Frontend Layer**:
  - `/projects/{id}` page: prompt list with template and date-range filters, reusing the history list component (US-4.2).
- **Backend Layer**:
  - `GET /api/v1/projects/{id}/prompts` — joins `project_prompts` to `generated_prompts`, filters by `template_id`/date range, verifies `project.owner_id == current_user`.
- **Database Layer**:
  - Read path only; no schema changes beyond `project_prompts` (see US-9.2).

## Exception Scenarios
- Accessing a project owned by another user → `403 Forbidden`.

## Verification & Testing
- Open a project with several prompts → verify the list matches what was added via US-9.2.
- Filter by template → verify only matching prompts show.
- Filter by date range → verify only prompts within range show.
- Attempt to open another user's project → verify `403 Forbidden`.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
