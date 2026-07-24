# User Story 3.2: Fill in the dynamic form per template (UC-03.02)

## Overview
- **Epic**: Epic 3: Prompt Generation Engine
- **Priority**: P1
- **User Persona**: User

## Story Description
- **As a** User,
- **I want to** fill in a dynamic form based on the template's variables,
- **So that** I can easily provide all the required information to build the prompt.

## Acceptance Criteria (BDD Format)
- **Given** I am on the template usage page
- **When** the form renders
- **Then** I see fields corresponding to the template variables with localized labels
- **And** client-side validation enforces rules (e.g., required, regex, limits)

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
