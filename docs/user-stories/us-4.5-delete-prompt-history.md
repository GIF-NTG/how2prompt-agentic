# User Story 4.5: Delete prompt history (UC-04.05)

## Overview
- **Epic**: Epic 4: Prompt History & Favorites
- **Priority**: P2
- **User Persona**: Logged-in User

## Story Description
- **As a** Logged-in User,
- **I want to** delete items from my prompt history,
- **So that** I can remove failed or unnecessary prompts.

## Acceptance Criteria (BDD Format)
- **Given** I am viewing my history
- **When** I click the delete button on an item and confirm
- **Then** the item is soft-deleted and removed from the list

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
