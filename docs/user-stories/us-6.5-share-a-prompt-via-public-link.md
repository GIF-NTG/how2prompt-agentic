# User Story 6.5: Share a Prompt via Public Link (UC-06.05)

## Overview
- **Epic**: Epic 6: AI Enhancement
- **Priority**: Medium
- **User Persona**: Logged-in User

## Story Description
- **As a** logged-in User who owns a generated prompt,
- **I want to** share it via a public link,
- **So that** others can view it without needing an account.

## Acceptance Criteria (BDD Format)
- **Given** I own a `generated_prompt`
- **When** I click `[Share]`
- **Then** the backend generates a `share_slug` (nanoid, 10 characters) and sets `is_public=true`
- **And** the frontend displays a URL in the form `https://how2prompt.app/p/{share_slug}`
- **And** anyone visiting that URL sees the prompt without logging in.
- **Given** a prompt is currently shared
- **When** I revoke sharing
- **Then** `is_public=false` and `share_slug=NULL`, and the public URL no longer resolves.

## Technical Implementation Details
- **Frontend Layer**:
  - `[Share]` action with copy-to-clipboard for the generated URL.
  - Public view page `/p/{share_slug}` — unauthenticated, read-only.
  - `[Hide inputs]` toggle when sharing, controlling whether `input_values` are shown on the public page.
- **Backend Layer**:
  - `POST /api/v1/generated-prompts/{id}/share` — generates `share_slug`, sets `is_public=true`.
  - `DELETE /api/v1/generated-prompts/{id}/share` — revokes sharing (`is_public=false`, `share_slug=NULL`).
  - `GET /api/v1/public/prompts/{share_slug}` — unauthenticated read endpoint.
- **Database Layer**:
  - `generated_prompts.share_slug` (unique, nanoid) and `is_public` columns.

## Business Rules
- The public page only shows `final_prompt`, the original template, and the model used.
- Detailed `input_values` are hidden on the public page if the owner selected 'hide inputs' when sharing.

## Verification & Testing
- Share a prompt → verify the public URL resolves without authentication and shows the expected fields.
- Toggle 'hide inputs' → verify `input_values` are absent from the public view.
- Revoke sharing → verify the public URL returns `404`.
- Attempt to share a prompt you don't own → verify `403 Forbidden`.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
