# User Story 4.3: Reload a prompt from history (UC-04.03)

## Overview
- **Epic**: Epic 4: Prompt History & Favorites
- **Priority**: P2
- **User Persona**: Logged-in User

## Story Description
- **As a** Logged-in User,
- **I want to** reload a prompt from my history,
- **So that** I can tweak the inputs and generate a new version without starting over.

## Acceptance Criteria (BDD Format)
- **Given** I am viewing my history
- **When** I click 'Re-run' on an item
- **Then** the template form opens with my previous input values pre-filled

## Technical Implementation Details
- **Frontend Layer**:
  - "Re-run" button on history items navigates to the Generate page.
  - Pre-fills dynamic form with old `input_values` and model selection from history record.
  - Clicking Generate creates a new record (does not overwrite the old one).
- **Backend Layer**:
  - `GET /api/v1/generated-prompts/{id}` returns full `input_values` (JSONB) for form pre-population.
  - Handles edge cases: deleted template (returns warning), newer template version available (returns version badge).
- **Database Layer**:
  - Read from `generated_prompts` table; join with `templates` and `template_versions` to check availability.

## Verification & Testing
- Click "Re-run" on a history item → verify Generate form pre-filled with original values.
- Edit fields and generate → verify a **new** record is created (old one preserved).
- Test with a deleted template → verify warning message, only "Copy" allowed, no form reload.
- Test with a template that has a newer version → verify badge "This used v1, v2 is now available".
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
