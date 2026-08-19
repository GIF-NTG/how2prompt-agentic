# User Story 9.1: Create a Project (UC-09.01)

## Overview
- **Epic**: Epic 9: Prompt Projects
- **Priority**: High
- **User Persona**: Logged-in User

## Story Description
- **As a** logged-in User,
- **I want to** create a Project with a name and an optional description/icon,
- **So that** I can group related generated prompts together.

## Acceptance Criteria (BDD Format)
- **Given** I am on the Projects page
- **When** I click `[+ New Project]` and submit a name (and optional description/icon)
- **Then** the frontend calls `POST /api/v1/projects`
- **And** the backend creates a `projects` record with `owner_id` = me
- **And** I am redirected to the new project's page.

## Exception Scenarios
- Duplicate name within my own projects → `409 Conflict`, "You already have a project with this name".

## Technical Implementation Details
- **Frontend Layer**:
  - `[+ New Project]` action on `/projects`, opening a name/description/icon form.
  - Redirects to `/projects/{id}` on success.
- **Backend Layer**:
  - `POST /api/v1/projects` — validates the name is unique per owner, creates the `projects` row.
- **Database Layer**:
  - New `projects` row: `id`, `owner_id`, `name`, `description`, `icon`, `custom_instructions` (nullable), `created_at`, `updated_at`, `deleted_at`.

## Business Rules
- A user can create an unlimited number of personal projects.
- The project name must be unique within the user's own projects (not globally).

## Verification & Testing
- Create a project with just a name → verify it appears on `/projects` and is empty.
- Create a project with description/icon → verify both are persisted and rendered.
- Attempt to create a second project with the same name → verify `409 Conflict`.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
