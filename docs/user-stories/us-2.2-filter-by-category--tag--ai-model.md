# User Story 2.2: Filter by Category / Tag / AI Model (UC-02.02)

## Overview
- **Epic**: Epic 2: Template Discovery & Browsing
- **Priority**: P1
- **User Persona**: User or Guest

## Story Description
- **As a** User or Guest,
- **I want to** filter templates by categories, tags, or target models,
- **So that** I can find templates specific to my current needs.

## Acceptance Criteria (BDD Format)
- **Given** I am viewing the template library
- **When** I select one or more categories, tags, or a target AI model
- **Then** the list updates to show only templates matching those criteria
- **And** the URL updates so I can share the filtered view

## Technical Implementation Details
- **Frontend Layer**:
  - Category sidebar (multi-select), AI model dropdown, tag multi-select chips.
  - URL query string updated on filter change (deep-linkable).
  - Total count badge reflecting filtered results.
  - React Query to refetch on filter change.
- **Backend Layer**:
  - `GET /api/v1/templates?category=...&model=...&tags=...` endpoint.
  - Joins via N:M tables: `template_categories`, `template_tags`, `template_models`.
  - Returns results with total count for badge display.
- **Database Layer**:
  - Queries across `templates`, `template_categories`, `template_tags`, `template_models`, `categories`, `tags`, `ai_models` tables.

## Verification & Testing
- Select a category → verify list narrows to matching templates.
- Select a model + tags → verify combined filter works correctly.
- Verify URL query string updates and is sharable (deep-linking).
- Click "Clear filters" → verify list resets to full results.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
