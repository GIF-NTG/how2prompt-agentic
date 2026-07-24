# User Story 3.6: Backend renders the prompt (UC-03.06)

## Overview
- **Epic**: Epic 3: Prompt Generation Engine
- **Priority**: P1
- **User Persona**: System

## Story Description
- **As a** System,
- **I want to** securely render the final prompt,
- **So that** validation is enforced and exact data is saved for history.

## Acceptance Criteria (BDD Format)
- **Given** the frontend submits the generate request
- **When** the backend receives it
- **Then** it validates the input, safely replaces placeholders, sanitizes the text, and returns the final string

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
