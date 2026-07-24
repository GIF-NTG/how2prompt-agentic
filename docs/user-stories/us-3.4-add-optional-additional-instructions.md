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
  - Dynamic form rendering based on `template_variables` JSONB configuration.
  - Real-time client-side prompt preview via React state.
- **Backend Layer**:
  - Rendering engine for final prompt compilation (source of truth).
  - Payload sanitization to prevent injection.

## Verification & Testing
- Select a template and verify dynamic fields appear.
- Type in fields and watch the real-time preview update.
- Click Generate and verify the backend response matches the preview.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [epics-and-stories.md](../epics-and-stories.md) for full system specifications.
