# User Story 5.6: Admin Mark Template as Featured (UC-05.06)

## Overview
- **Epic**: Epic 5: Admin & Content Management
- **Note**: Supplementary story beyond the base use-case catalog (SRS §3 / use-cases.md only define UC-05.01–UC-05.05); numbered UC-05.06 to stay within the Epic 5 range without colliding with Epic 6 (AI Enhancement, Phase 2).
- **Priority**: P2
- **User Persona**: Admin

## Story Description
- **As an** Admin,
- **I want to** mark specific templates as "Featured" (and unmark them),
- **So that** they appear in the Featured carousel on the homepage and are highly visible to users.

## Acceptance Criteria (BDD Format)
- **Given** I am logged in as an Admin
- **When** I update a template and set it to be "Featured"
- **Then** the template is marked as featured
- **And** it appears in the Featured templates list/carousel on the homepage.
- **Given** a template is already "Featured"
- **When** I update the template to remove the "Featured" status
- **Then** the template is no longer marked as featured
- **And** it disappears from the Featured templates list/carousel.

## Technical Implementation Details
- **Frontend Layer**:
  - Add a "Featured" toggle or checkbox in the admin template edit form/list.
  - Send `isFeatured` boolean in the `PATCH /api/v1/admin/templates/{id}` payload.
- **Backend Layer**:
  - `PATCH /api/v1/admin/templates/{id}` (existing endpoint) will accept an optional `isFeatured` boolean field.
  - If `isFeatured = true`, the backend sets `featured_at = NOW()` (if it was null).
  - If `isFeatured = false`, the backend sets `featured_at = NULL`.
- **Database Layer**:
  - Update `templates.featured_at` column for the given template ID.

## Verification & Testing
- Log in as admin → edit template → check "Featured" → save.
- Verify `GET /api/v1/templates/featured` returns the newly featured template.
- Edit template again → uncheck "Featured" → save.
- Verify `GET /api/v1/templates/featured` no longer returns the template.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
