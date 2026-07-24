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
  - React Query for data fetching and caching.
  - Debounced input for full-text search.
- **Backend Layer**:
  - Spring Data JPA with pagination.
  - Redis caching for featured/trending endpoints.
- **Database Layer**:
  - PostgreSQL `tsvector` and `pg_trgm` for search indexing.

## Verification & Testing
- Visit the explore page to ensure templates render.
- Apply filters and verify the URL query string updates.
- Perform a search and verify latency < 200ms.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [epics-and-stories.md](../epics-and-stories.md) for full system specifications.
