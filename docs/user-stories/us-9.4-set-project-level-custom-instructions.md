# User Story 9.4: Set Project-Level Custom Instructions (UC-09.04)

## Overview
- **Epic**: Epic 9: Prompt Projects
- **Priority**: Medium
- **User Persona**: Logged-in User

## Story Description
- **As a** logged-in User who owns a project,
- **I want to** set custom instructions on the project,
- **So that** every prompt I generate inside it automatically follows the same context without retyping it each time.

## Acceptance Criteria (BDD Format)
- **Given** I am in a project's settings
- **When** I edit the custom instructions field and save
- **Then** the frontend calls `PATCH /api/v1/projects/{id}` with `custom_instructions`
- **And** the backend persists it on the `projects` record.
- **Given** a project has custom instructions set
- **When** I generate a prompt from a template inside that project
- **Then** the backend prepends the project's custom instructions before backend rendering (source of truth per US-3.6).

## Technical Implementation Details
- **Frontend Layer**:
  - Project settings page: a free-form text field for `custom_instructions`.
- **Backend Layer**:
  - `PATCH /api/v1/projects/{id}` — updates `projects.custom_instructions`.
  - `POST /api/v1/templates/{id}/generate` — when `project_id` is present, reads `projects.custom_instructions` and prepends it to the rendered prompt before saving `generated_prompts`.
- **Database Layer**:
  - `projects.custom_instructions` (text, nullable).

## Business Rules
- Custom instructions apply only to prompts generated inside the project going forward; prompts already in the project are not retroactively changed.

## Verification & Testing
- Set custom instructions on a project, then generate a prompt inside it → verify the final prompt includes the instructions.
- Add an already-existing prompt to the project (US-9.2) → verify its `final_prompt` is unchanged (not retroactively rewritten).
- Clear the custom instructions field → verify subsequent generations no longer include it.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
