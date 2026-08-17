# User Story 7.1: Fork a Template into a Personal Workspace (UC-07.01)

## Overview
- **Epic**: Epic 7: Template Customization & Versioning
- **Priority**: High
- **User Persona**: Logged-in User

## Story Description
- **As a** logged-in User,
- **I want to** fork a public or official template into my personal workspace,
- **So that** I can customize it without affecting the original.

## Acceptance Criteria (BDD Format)
- **Given** a template is public or official
- **When** I click `[Fork]` on its detail page
- **Then** the frontend calls `POST /api/v1/templates/{id}/fork`
- **And** the backend clones the `templates` row, its current `template_versions`, `template_variables`, and `template_variants`
- **And** the new copy has `workspace_id` = my personal workspace, `author_id` = me, `author_type='forked'`, `is_official=false`, `is_public=false`, `status='draft'`, and `forked_from_template_id`/`forked_from_version_id` pointing to the source
- **And** the original template's `fork_count` is incremented
- **And** I am redirected to the template editor with my fork.

## Technical Implementation Details
- **Frontend Layer**:
  - `[Fork]` button on the template detail page (US-2.4), disabled for templates the user already owns.
  - Redirects to the template editor (US-7.2) on success.
- **Backend Layer**:
  - `POST /api/v1/templates/{id}/fork` — clones `templates` + current `template_versions` + `template_variables` + `template_variants`; sets `forked_from_template_id`, `forked_from_version_id`.
  - Increments `templates.fork_count` on the source template.
- **Database Layer**:
  - New `templates` row + associated `template_versions`/`template_variables`/`template_variants` rows, all scoped to the user's personal `workspace_id`.

## Business Rules
- A fork does not automatically receive updates when the original template gets a new version.
- A user can fork the same template multiple times; each fork is an independent copy.

## Verification & Testing
- Fork a public template → verify a new draft template exists in my personal workspace with the same variables/variants as the source.
- Verify the source template's `fork_count` increments.
- Publish a new version of the source template after forking → verify the existing fork is unaffected.
- Fork the same template twice → verify two independent copies exist.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
