# User Story 7.2: Edit a Personal Template (UC-07.02)

## Overview
- **Epic**: Epic 7: Template Customization & Versioning
- **Priority**: High
- **User Persona**: Logged-in User (template owner)

## Story Description
- **As a** User who owns a template (a fork or one I created),
- **I want to** edit its title, description, prompt body, and variables,
- **So that** I can tailor it to my exact needs.

## Acceptance Criteria (BDD Format)
- **Given** I am in the template editor for a template I own
- **When** I edit the title, description, or `prompt_body`, and perform CRUD on `template_variables` (add a field with a chosen `input_type` and options/validation, remove a field, or reorder fields), and edit `template_variants` for other models
- **And** I click `[Save]`
- **Then** the backend creates a new `template_versions` record if `prompt_body` or variables changed, preserving old history pointing at the old version.
- **Given** I try to delete a variable still referenced in `prompt_body`
- **When** I attempt to save
- **Then** I see a warning requiring me to remove the placeholder from `prompt_body` first.

## Technical Implementation Details
- **Frontend Layer**:
  - Template editor: title/description fields, prompt-body editor, variable CRUD panel (input type, options, validation, `var_key`), variant editor per model.
  - Client-side check blocking removal of a variable still referenced by an active `{{placeholder}}`.
- **Backend Layer**:
  - `PATCH /api/v1/templates/{id}` — validates `var_key` uniqueness/format, validates every `{{placeholder}}` in `prompt_body` has a matching variable, and creates a new `template_versions` row when content changed.
- **Database Layer**:
  - New `template_versions` row on meaningful change; old `generated_prompts` continue referencing the prior `template_version_id` (no retroactive rewrite).

## Business Rules
- Maximum 30 fields per template (Free plan), 100 fields (Pro).
- `var_key` must be unique within a `template_version`, snake_case, no diacritics.

## Verification & Testing
- Edit `prompt_body` and save → verify a new `template_versions` row is created and old `generated_prompts` still reference the prior version.
- Add a variable exceeding the Free-plan field limit → verify the save is blocked with a clear message.
- Attempt to delete a variable still referenced in `prompt_body` → verify the warning blocks the save.
- Use a duplicate or invalid `var_key` (uppercase, diacritics) → verify validation rejects it.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
