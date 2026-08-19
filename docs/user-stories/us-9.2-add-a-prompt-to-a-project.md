# User Story 9.2: Add a Prompt to a Project (UC-09.02)

## Overview
- **Epic**: Epic 9: Prompt Projects
- **Priority**: High
- **User Persona**: Logged-in User

## Story Description
- **As a** logged-in User who owns a generated prompt and a project,
- **I want to** add that prompt to a project, or generate a new one directly inside a project,
- **So that** related prompts stay grouped together instead of scattered across my history.

## Acceptance Criteria (BDD Format)
- **Given** I have a generated prompt not yet assigned to a project
- **When** I select `[Add to project]` and pick a target project
- **Then** the frontend calls `POST /api/v1/projects/{id}/prompts` with the `generated_prompt_id`
- **And** the backend inserts a `project_prompts` record linking the prompt and the project.
- **Given** I am inside a project's page
- **When** I click `[Generate]` on a template from within the project view
- **Then** `POST /api/v1/templates/{id}/generate` includes `project_id` in the payload
- **And** the resulting prompt is linked to the project in the same call, without a separate request.

## Technical Implementation Details
- **Frontend Layer**:
  - `[Add to project]` action on a generated prompt's result view and on history items.
  - `[Generate]` inside a project page passes the current `project_id` through to the generate call.
- **Backend Layer**:
  - `POST /api/v1/projects/{id}/prompts` — inserts a `project_prompts` row for `(project_id, generated_prompt_id)`; if the prompt is already linked to another project, moves the link (see US-9.5).
  - `POST /api/v1/templates/{id}/generate` — when `project_id` is present in the payload, creates the `project_prompts` link in the same transaction as the `generated_prompts` insert.
- **Database Layer**:
  - `project_prompts` table: `project_id`, `generated_prompt_id`, `added_at`, with a unique constraint on `generated_prompt_id` (a prompt belongs to at most one project).

## Business Rules
- A prompt can belong to at most one project at a time.

## Verification & Testing
- Add an existing prompt to a project → verify it appears in the project's prompt list.
- Generate a prompt from within a project → verify it's linked without a separate "add" call.
- Add a prompt already linked to project A into project B → verify it moves (see US-9.5) rather than duplicating.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
