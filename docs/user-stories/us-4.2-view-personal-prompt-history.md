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
  - History page at `/history` with list/card view.
  - Cursor-based pagination (load-more or infinite scroll).
  - Filters: by template, AI model, and date range.
  - React Query for data fetching and caching.
- **Backend Layer**:
  - `GET /api/v1/generated-prompts?limit=20&cursor=...` endpoint.
  - Sorted by `created_at DESC`; filters by `template_id`, `ai_model_id`, date range.
  - Returns list with snippet of `final_prompt` and template thumbnail.
- **Database Layer**:
  - Query `generated_prompts` table filtered by `user_id`, `deleted_at IS NULL`.
  - Composite index on `(user_id, created_at DESC)` for fast retrieval.

## Verification & Testing
- Navigate to `/history` → verify generated prompts listed in reverse chronological order.
- Test filters: filter by template → verify only matching history shown.
- Test cursor-based pagination → verify next page loads correctly.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
