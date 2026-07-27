# User Story 2.5: View Featured / Trending templates (UC-02.05)

## Overview
- **Epic**: Epic 2: Template Discovery & Browsing
- **Priority**: P2
- **User Persona**: User or Guest

## Story Description
- **As a** User or Guest,
- **I want to** see featured and trending templates on the homepage,
- **So that** I can discover popular or highly recommended content.

## Acceptance Criteria (BDD Format)
- **Given** I visit the homepage
- **When** the page loads
- **Then** I see a carousel of Featured templates
- **And** a carousel of Trending templates based on 7-day usage

## Technical Implementation Details
- **Frontend Layer**:
  - Two separate carousels on the homepage: Featured and Trending.
  - React Query for fetching with stale-while-revalidate pattern.
- **Backend Layer**:
  - `GET /api/v1/templates/featured` — returns templates where `featured_at IS NOT NULL`, sorted by `featured_at DESC`.
  - `GET /api/v1/templates/trending?window=7d` — returns templates ranked by `usage_count` over the last 7 days.
  - Both endpoints cached in Redis for 10 minutes to reduce database load.
- **Database Layer**:
  - `templates.featured_at` column for admin-curated featured templates.
  - Aggregate `usage_count` over 7-day window for trending calculation.

## Verification & Testing
- Visit homepage → verify Featured and Trending carousels render separately.
- Mark a template as featured (admin) → verify it appears in the Featured carousel.
- Verify cache: data stays consistent for 10 minutes even after new template activity.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
