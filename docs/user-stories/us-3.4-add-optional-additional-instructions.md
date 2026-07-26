# User Story 3.4: Add optional Additional Instructions (UC-03.04)

## Overview
- **Epic**: Epic 3: Prompt Generation Engine
- **Priority**: P2
- **User Persona**: User

## Story Description
- **As a** User,
- **I want to** add additional free-form instructions,
- **So that** I can customize the prompt beyond the template's structured fields.

## Acceptance Criteria (BDD Format)
- **Given** I am on the Generate form
- **When** I type text into the 'Additional instructions' textarea
- **Then** my text is appended to the end of the prompt preview

## Technical Implementation Details
- **Frontend Layer**:
  - "Additional instructions (optional)" textarea rendered at the bottom of the dynamic form.
  - Content appended to real-time preview as user types.
- **Backend Layer**:
  - Appends `extra_instructions` to the end of `prompt_body` after a newline.
  - If the template declares a `{{__extra__}}` placeholder, the content is inserted at that specific location instead.
  - Content is escaped to guard against basic prompt injection.
- **Database Layer**:
  - `extra_instructions` stored as part of `generated_prompts.extra_instructions` column.

## Verification & Testing
- Type additional instructions → verify they appear in the preview appended at the end.
- Test with a template that uses `{{__extra__}}` placeholder → verify instructions are inserted at the correct location.
- Attempt to inject prompt manipulation characters → verify content is escaped.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
