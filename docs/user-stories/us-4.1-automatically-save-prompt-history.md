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
  - History drawer/page with pagination.
  - React Context to track favorite states.
- **Backend Layer**:
  - Asynchronous saving to history via `@Transactional` methods.
- **Database Layer**:
  - PostgreSQL `generated_prompts` and `favorites` tables.

## Verification & Testing
- Generate a prompt and check if it appears in the history list.
- Click 'Re-run' to ensure old variables are loaded.
- Click favorite icon and verify state persists.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [epics-and-stories.md](../epics-and-stories.md) for full system specifications.
