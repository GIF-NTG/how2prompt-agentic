# User Story 4.2: View personal prompt history (UC-04.02)

## Overview
- **Epic**: Epic 4: Prompt History & Favorites
- **Priority**: P1
- **User Persona**: Logged-in User

## Story Description
- **As a** Logged-in User,
- **I want to** view a history of my generated prompts,
- **So that** I can find and reuse prompts I created previously.

## Acceptance Criteria (BDD Format)
- **Given** I navigate to the '/history' page
- **When** the page loads
- **Then** I see a paginated list of my past generated prompts sorted by date

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
