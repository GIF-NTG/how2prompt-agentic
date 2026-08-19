# User Story 9.6: Rename or Delete a Project (UC-09.06)

## Overview
- **Epic**: Epic 9: Prompt Projects
- **Priority**: Medium
- **User Persona**: Logged-in User

## Story Description
- **As a** logged-in User who owns a project,
- **I want to** rename it or delete it,
- **So that** I can keep my project list accurate as my work evolves.

## Acceptance Criteria (BDD Format)
- **Given** I am in a project's settings
- **When** I edit the name and save
- **Then** the frontend calls `PATCH /api/v1/projects/{id}`
- **And** the backend updates `projects.name`.
- **Given** I am in a project's settings
- **When** I click `[Delete project]` and confirm
- **Then** the frontend calls `DELETE /api/v1/projects/{id}`
- **And** the backend soft-deletes the `projects` record (`deleted_at`)
- **And** removes its `project_prompts` links
- **And** the underlying `generated_prompts` rows are untouched.

## Technical Implementation Details
- **Frontend Layer**:
  - Project settings page: rename field, `[Delete project]` action with a confirmation dialog.
- **Backend Layer**:
  - `PATCH /api/v1/projects/{id}` — updates `projects.name` (also used by US-9.4 for `custom_instructions`).
  - `DELETE /api/v1/projects/{id}` — sets `projects.deleted_at`, deletes associated `project_prompts` rows; `generated_prompts` rows are never touched.
- **Database Layer**:
  - `projects.deleted_at` (nullable timestamp), with a partial index for `WHERE deleted_at IS NULL` queries.

## Business Rules
- Deleting a project never deletes the prompts inside it — they simply become unassigned and remain visible in personal history (US-4.2).

## Verification & Testing
- Rename a project → verify the new name shows on `/projects` and the project page.
- Delete a project → verify it disappears from `/projects`, and its former prompts still exist in history with no project assignment.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
