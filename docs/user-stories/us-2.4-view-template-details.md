# User Story 2.4: View template details (UC-02.04)

## Overview
- **Epic**: Epic 2: Template Discovery & Browsing
- **Priority**: P1
- **User Persona**: User or Guest

## Story Description
- **As a** User or Guest,
- **I want to** view the details of a template,
- **So that** I can understand its purpose, see an example, and decide if I want to use it.

## Acceptance Criteria (BDD Format)
- **Given** I click on a template card
- **When** the detail page loads
- **Then** I see the description, guide, example output, variables, and usage count
- **And** the view count of the template is incremented

## Technical Implementation Details
- **Frontend Layer**:
  - Template detail page with sections: description, example output, usage guide, variable list, supported models.
  - Action buttons: `[Use template]`, `[Favorite]`, `[Fork]` (Phase 2).
  - React Query for data fetching with cache.
- **Backend Layer**:
  - `GET /api/v1/templates/{id}` endpoint.
  - Returns: template info, `current_version` (prompt_body, guide), `template_variables`, `template_variants` by model, author info, usage/favorite counts, favorite status (if logged in).
  - Increments `view_count` asynchronously (non-blocking).
- **Database Layer**:
  - Joins: `templates`, `template_versions`, `template_variables`, `template_variants`, `ai_models`.

## Verification & Testing
- Click a template card → verify detail page renders all sections correctly.
- Verify `view_count` increments after page load.
- Access a non-existent template → expect `404 Not Found`.
- Access a private template from another workspace → expect `403 Forbidden`.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
