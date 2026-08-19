# User Story 9.5: Move or Remove a Prompt from a Project (UC-09.05)

## Overview
- **Epic**: Epic 9: Prompt Projects
- **Priority**: Medium
- **User Persona**: Logged-in User

## Story Description
- **As a** logged-in User who owns a prompt and the project(s) involved,
- **I want to** move a prompt to a different project or remove it from its project,
- **So that** I can reorganize my prompts without losing them.

## Acceptance Criteria (BDD Format)
- **Given** a prompt is currently assigned to project A
- **When** I select `[Move to project]` and pick project B
- **Then** the frontend calls `POST /api/v1/projects/{B}/prompts` with the `generated_prompt_id`
- **And** the backend updates the existing `project_prompts` row to `project_id = B` (per the unique constraint from US-9.2).
- **Given** a prompt is currently assigned to a project
- **When** I select `[Remove from project]`
- **Then** the frontend calls `DELETE /api/v1/projects/{id}/prompts/{promptId}`
- **And** the backend deletes the `project_prompts` row
- **And** the underlying `generated_prompts` row is untouched and becomes unassigned.

## Technical Implementation Details
- **Frontend Layer**:
  - `[Move to project]` and `[Remove from project]` actions on a prompt within a project view.
- **Backend Layer**:
  - `POST /api/v1/projects/{id}/prompts` — upserts the `project_prompts` row for the given `generated_prompt_id`, moving it if already linked elsewhere.
  - `DELETE /api/v1/projects/{id}/prompts/{promptId}` — deletes the `project_prompts` row only; never touches `generated_prompts`.
- **Database Layer**:
  - No schema change beyond `project_prompts` (see US-9.2).

## Verification & Testing
- Move a prompt from project A to project B → verify it disappears from A's list and appears in B's list.
- Remove a prompt from a project → verify it disappears from the project's list but still appears in personal history (US-4.2).
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
