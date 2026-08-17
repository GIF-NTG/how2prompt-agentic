# User Story 7.4: Manage Template Versions (UC-07.04)

## Overview
- **Epic**: Epic 7: Template Customization & Versioning
- **Priority**: Medium
- **User Persona**: Author (template owner)

## Story Description
- **As an** Author who owns a template with multiple versions,
- **I want to** view, compare, and switch which version is current,
- **So that** I can control which version new users receive while preserving history for old ones.

## Acceptance Criteria (BDD Format)
- **Given** my template has multiple `template_versions`
- **When** I open the 'Versions' tab in the editor
- **Then** I see a list of versions with `version_number`, changelog, `created_by`, and `created_at`
- **And** I can compare a diff between any two versions
- **And** I can mark one version as `is_current`, so any new user using the template gets that version.

## Technical Implementation Details
- **Frontend Layer**:
  - 'Versions' tab in the template editor: version list, diff viewer (two-version comparison), 'Set as current' action.
- **Backend Layer**:
  - `GET /api/v1/templates/{id}/versions` — list versions.
  - `GET /api/v1/templates/{id}/versions/diff?from={v1}&to={v2}` — diff two versions.
  - `PATCH /api/v1/templates/{id}/versions/{versionId}/current` — sets `is_current=true` on the target version, `false` on all others for that template.
- **Database Layer**:
  - `template_versions.is_current` boolean, exactly one `true` per template.
  - Versions can be archived (`archived_at` set) but never hard-deleted.

## Business Rules
- Old versions cannot be deleted since existing `generated_prompts` may still reference them (referential integrity).
- Old versions can be archived — archiving removes them from selection when generating new prompts, without deleting them.

## Verification & Testing
- Edit a template twice → verify two versions exist and are listed with correct metadata.
- Diff two versions → verify the changed fields/placeholders are highlighted.
- Set an older version as current → verify new generations use it while existing `generated_prompts` still reference their original version.
- Archive a version → verify it no longer appears in the model/version selector for new generations, but historical records referencing it remain intact.
- Attempt to delete a version referenced by existing `generated_prompts` → verify it's blocked (archive only).
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
