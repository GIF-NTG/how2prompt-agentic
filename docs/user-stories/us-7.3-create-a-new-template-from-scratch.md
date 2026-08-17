# User Story 7.3: Create a New Template from Scratch (UC-07.03)

## Overview
- **Epic**: Epic 7: Template Customization & Versioning
- **Priority**: Medium
- **User Persona**: Logged-in User

## Story Description
- **As a** logged-in User with remaining template-creation quota,
- **I want to** create a brand-new template from an empty editor,
- **So that** I can build a prompt template for a use case not already covered by the library.

## Acceptance Criteria (BDD Format)
- **Given** I am logged in and have `template_create` quota remaining
- **When** I click `[+ New Template]` from `/my-templates`
- **Then** the frontend opens an empty editor
- **And** I fill in the title, description, categories, tags, models, `prompt_body`, and variables
- **And** I click `[Save Draft]` to persist it as a draft, or `[Publish (submit for review)]` to send it into the moderation queue (US-5.5).

## Technical Implementation Details
- **Frontend Layer**:
  - `[+ New Template]` action on `/my-templates`, opening the same editor shell used for editing forks (US-7.2), pre-populated empty.
- **Backend Layer**:
  - `POST /api/v1/templates` — creates a new `templates` row with `workspace_id` = personal workspace, `author_id` = me, `author_type='created'`, `status='draft'`.
  - Enforces the `template_create` quota before allowing creation.
- **Database Layer**:
  - New `templates` + `template_versions` + `template_variables` rows.

## Business Rules
- Free plan: limited to 10 templates per user. Pro: unlimited.

## Verification & Testing
- Create a new template as a Free-plan user under the limit → verify it's created as a draft.
- Attempt to create an 11th template on the Free plan → verify creation is blocked with an upgrade prompt.
- Save as draft → verify it's visible only to me in `/my-templates`, not in `/explore`.
- Save via `[Publish]` → verify it enters `status='pending'` and appears in the admin moderation queue (US-5.5).
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
