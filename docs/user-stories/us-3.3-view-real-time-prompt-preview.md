# User Story 3.3: View real-time prompt preview (UC-03.03)

## Overview
- **Epic**: Epic 3: Prompt Generation Engine
- **Priority**: P1
- **User Persona**: User

## Story Description
- **As a** User,
- **I want to** see a real-time preview of the prompt as I type,
- **So that** I can see exactly what the final prompt will look like.

## Acceptance Criteria (BDD Format)
- **Given** I am filling in the dynamic form
- **When** I type in a field
- **Then** the prompt preview panel updates instantly to show the replaced values

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
