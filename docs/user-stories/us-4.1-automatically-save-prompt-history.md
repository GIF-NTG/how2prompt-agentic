# User Story 4.1: Automatically save prompt history (UC-04.01)

## Overview
- **Epic**: Epic 4: Prompt History & Favorites
- **Priority**: P1
- **User Persona**: System

## Story Description
- **As a** System,
- **I want to** automatically save generated prompts,
- **So that** users don't lose their work.

## Acceptance Criteria (BDD Format)
- **Given** a prompt is successfully generated via the backend
- **When** the generation transaction completes
- **Then** a record containing the input values and final prompt is asynchronously saved to the user's history

## Technical Implementation Details
- **Frontend Layer**:
  - N/A — this is a system-level operation triggered automatically after prompt generation.
- **Backend Layer**:
  - Within the same `@Transactional` block as UC-03.06 (backend render), creates a `generated_prompts` record.
  - Saves: `user_id`, `workspace_id`, `template_id`, `template_version_id`, `ai_model_id`, `input_values` (JSONB), `extra_instructions`, `final_prompt`.
  - Does not block the generation response — runs within the same transaction for consistency.
- **Database Layer**:
  - Insert into `generated_prompts` table.
  - Soft-delete via `deleted_at` column (records are never hard-deleted).

## Verification & Testing
- Generate a prompt → verify a `generated_prompts` record is created with all correct fields.
- Verify `input_values` JSONB matches what was submitted in the form.
- Verify soft-delete: deleted records retain `deleted_at` timestamp, not physically removed.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
