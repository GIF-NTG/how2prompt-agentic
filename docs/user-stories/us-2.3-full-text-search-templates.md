# User Story 2.3: Full-text search templates (UC-02.03)

## Overview
- **Epic**: Epic 2: Template Discovery & Browsing
- **Priority**: P1
- **User Persona**: User or Guest

## Story Description
- **As a** User or Guest,
- **I want to** search templates by keyword,
- **So that** I can quickly find templates related to a specific topic.

## Acceptance Criteria (BDD Format)
- **Given** I type a keyword in the search box
- **When** I stop typing (debounce)
- **Then** the system returns relevant templates using full-text and fuzzy search

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
