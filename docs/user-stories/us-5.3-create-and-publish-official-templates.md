# User Story 5.3: Create & publish official templates (UC-05.03)

## Overview
- **Epic**: Epic 5: Admin & Content Management
- **Priority**: P1
- **User Persona**: Admin

## Story Description
- **As a** Admin,
- **I want to** create and publish official templates,
- **So that** users have high-quality, verified templates available at launch.

## Acceptance Criteria (BDD Format)
- **Given** I am on the '/admin/templates' page
- **When** I define a template and click Publish
- **Then** it is marked as 'is_official=true' and is visible to all users

## Technical Implementation Details
- **Frontend Layer**:
  - Protected admin route at `/admin/templates` (requires `is_admin = true`).
  - Template editor: title/description (i18n EN + VI), cover image upload, category/tag/model selectors.
  - Prompt body editor with `{{placeholder}}` syntax.
  - Variable declaration form: `var_key`, `label` (i18n), `input_type`, `options`, `validation`, `sort_order`.
  - Optional variant creation for specific AI models.
  - Save Draft / Publish buttons.
- **Backend Layer**:
  - `POST /api/v1/admin/templates` — create template.
  - `PATCH /api/v1/admin/templates/{id}` — update template.
  - Pre-publish validation: every `{{placeholder}}` in `prompt_body` must have a corresponding variable.
  - On publish: sets `is_official=true`, `status='published'`, `published_at=NOW()`.
  - Editing after publish creates a new `template_version` (does not overwrite).
- **Database Layer**:
  - Insert/update across: `templates`, `template_versions`, `template_variables`, `template_variants`, `template_categories`, `template_tags`, `template_models`.

## Verification & Testing
- Create a template with variables → publish → verify visible to all users on `/explore`.
- Test placeholder validation: add a `{{placeholder}}` without a matching variable → verify publish is blocked.
- Edit a published template → verify a new version is created, old version preserved.
- Access `/admin/templates` as a normal user → expect `403 Forbidden`.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
