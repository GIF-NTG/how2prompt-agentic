# User Story 2.1: Browse the template library (UC-02.01)

## Overview
- **Epic**: Epic 2: Template Discovery & Browsing
- **Priority**: P1
- **User Persona**: User or Guest

## Story Description
- **As a** User or Guest,
- **I want to** browse the template library,
- **So that** I can discover available templates.

## Acceptance Criteria (BDD Format)
- **Given** I navigate to the '/explore' page
- **When** the page loads
- **Then** I see a paginated grid of public templates sorted by popularity

## Technical Implementation Details
- **Frontend Layer**:
  - React Query for data fetching and caching.
  - Grid layout with infinite scroll or load-more button.
  - Template cards showing: title, cover image, category, `upvote_count`, `usage_count`, author.
- **Backend Layer**:
  - `GET /api/v1/templates?sort=popular&limit=20` endpoint.
  - Filter: `status='published' AND is_public=true` (for guests); include user's workspace templates if logged in.
  - Templates with `is_official=true` prioritized at the top under default sort.
- **Database Layer**:
  - Query `templates` table with cursor-based pagination.
  - Exclude records where `deleted_at IS NOT NULL`.

## Verification & Testing
- Visit `/explore` → verify template grid renders with cards showing correct metadata.
- Verify official templates (`is_official=true`) appear at the top.
- Verify soft-deleted templates are not displayed.
- Test infinite scroll / load-more pagination.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
