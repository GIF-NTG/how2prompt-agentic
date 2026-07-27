# User Story 3.5: Generate & copy the complete prompt (UC-03.05)

## Overview
- **Epic**: Epic 3: Prompt Generation Engine
- **Priority**: P1
- **User Persona**: User

## Story Description
- **As a** User,
- **I want to** generate and copy the final prompt,
- **So that** I can paste it into my AI tool of choice.

## Acceptance Criteria (BDD Format)
- **Given** I have filled in all required fields
- **When** I click 'Generate'
- **Then** the backend renders the final prompt and returns it
- **And** I can click 'Copy' to save it to my clipboard with a confirmation toast

## Technical Implementation Details
- **Frontend Layer**:
  - "Generate" button calls backend API.
  - Results panel displays final prompt with `[Copy]`, `[Save as favorite]` buttons.
  - Clipboard API writes prompt to clipboard; "Copied" toast notification on success.
- **Backend Layer**:
  - `POST /api/v1/templates/{id}/generate` with payload: `{ template_version_id, ai_model_id, input_values, extra_instructions }`.
  - Backend renders the final prompt (US-3.6), saves to `generated_prompts`, increments `templates.usage_count`.
  - Returns `{ generated_prompt_id, final_prompt, tokens_estimate }`.
- **Database Layer**:
  - Insert into `generated_prompts` table; update `templates.usage_count`.

## Verification & Testing
- Fill in all required fields → click "Generate" → verify prompt displayed in results panel.
- Click "Copy" → verify prompt copied to clipboard and "Copied" toast appears.
- Check `generated_prompts` table → verify history record created with correct data.
- Test with backend rendering error (invalid placeholder) → expect `500` with user-friendly fallback message.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
