# User Story 4.4: Favorite or unfavorite a template (UC-04.04)

## Overview
- **Epic**: Epic 4: Prompt History & Favorites
- **Priority**: P2
- **User Persona**: Logged-in User

## Story Description
- **As a** Logged-in User,
- **I want to** favorite and unfavorite templates,
- **So that** I can easily access templates I use frequently.

## Acceptance Criteria (BDD Format)
- **Given** I click the heart icon on a template
- **When** the request completes
- **Then** the template is added to or removed from my favorites list
- **And** the template's favorite count is updated

## Technical Implementation Details
- **Frontend Layer**:
  - Heart icon toggle on template cards and detail pages.
  - Zustand store tracks favorite states for optimistic UI updates.
  - Toast notification on favorite/unfavorite action.
- **Backend Layer**:
  - `POST /api/v1/templates/{id}/favorite` to add favorite.
  - `DELETE /api/v1/templates/{id}/favorite` to remove favorite.
  - Increments/decrements `templates.favorite_count` on toggle.
- **Database Layer**:
  - Insert/delete in `favorites` table (`user_id`, `template_id`).
  - Update `templates.favorite_count` counter.

## Verification & Testing
- Click heart icon on a template → verify icon toggles filled/unfilled and toast appears.
- Verify `favorites` table record created/deleted.
- Verify `templates.favorite_count` increments/decrements correctly.
- Navigate to `/favorites` → verify favorited templates are listed.
- Unfavorite a template → verify it disappears from the favorites list.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
