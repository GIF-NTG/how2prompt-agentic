# User Story 5.2: Manage Categories & Tags (UC-05.02)

## Overview
- **Epic**: Epic 5: Admin & Content Management
- **Priority**: P1
- **User Persona**: Admin

## Story Description
- **As a** Admin,
- **I want to** manage categories and tags,
- **So that** templates are properly organized and searchable.

## Acceptance Criteria (BDD Format)
- **Given** I am on the '/admin/taxonomy' page
- **When** I create, edit, or merge categories and tags
- **Then** the taxonomy tree is updated and template associations are maintained

## Technical Implementation Details
- **Frontend Layer**:
  - Protected admin route at `/admin/taxonomy` (requires `is_admin = true`).
  - Tree view for nested categories; flat list/tag cloud for tags.
  - Tag merge UI: select duplicates and merge into one.
- **Backend Layer**:
  - `GET/POST/PATCH/DELETE /api/v1/admin/taxonomy` endpoints.
  - Category nesting via `parent_id`.
  - Tag merge: combines duplicate tags (e.g., "email" + "emails") and updates `usage_count`.
  - Role-based authorization: `hasRole('ADMIN')`.
- **Database Layer**:
  - `categories` table with `parent_id` for nesting.
  - `tags` table with `usage_count`.

## Verification & Testing
- Create a nested category → verify it appears correctly in the browse sidebar.
- Merge duplicate tags → verify `usage_count` is summed and old tag is removed.
- Verify taxonomy changes reflected in template filter controls.
- Access `/admin/taxonomy` as a normal user → expect `403 Forbidden`.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
