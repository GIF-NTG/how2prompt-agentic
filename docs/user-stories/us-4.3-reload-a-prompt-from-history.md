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
