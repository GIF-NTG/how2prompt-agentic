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
  - Debounced search input (300ms delay before sending request).
  - Keyword highlighting in search results.
  - React Query for caching search results.
- **Backend Layer**:
  - `GET /api/v1/templates?q=...` endpoint.
  - Primary search: `search_vector` column (`tsvector`) with `to_tsquery`.
  - Fallback: `pg_trgm` for fuzzy matching when exact match returns few results.
  - Ranking: `ts_rank + usage_count` for relevance ordering.
- **Database Layer**:
  - GIN index on `search_vector` (tsvector) column.
  - `pg_trgm` extension for trigram-based fuzzy search.
  - Supports both English and Vietnamese (using 'simple' dictionary).

## Verification & Testing
- Type a keyword (e.g., "email marketing") → verify results appear after debounce.
- Verify search latency p95 < 200ms with 10K templates.
- Test fuzzy search with typos → verify pg_trgm returns relevant results.
- Test search in both English and Vietnamese.
- Verify keyword highlighting in result titles/descriptions.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
