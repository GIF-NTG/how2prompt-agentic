# User Story 3.1: Select the target AI Model for a prompt (UC-03.01)

## Overview
- **Epic**: Epic 3: Prompt Generation Engine
- **Priority**: P1
- **User Persona**: User

## Story Description
- **As a** User,
- **I want to** select a target AI model for my template,
- **So that** the generated prompt uses the optimal format for that specific AI.

## Acceptance Criteria (BDD Format)
- **Given** I am on the template usage page
- **When** I select an AI model from the supported models dropdown
- **Then** the system prepares to use the specific template variant for that model if it exists

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
