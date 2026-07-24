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
