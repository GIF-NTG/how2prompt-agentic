# User Story 3.2: Fill in the dynamic form per template (UC-03.02)

## Overview
- **Epic**: Epic 3: Prompt Generation Engine
- **Priority**: P1
- **User Persona**: User

## Story Description
- **As a** User,
- **I want to** fill in a dynamic form based on the template's variables,
- **So that** I can easily provide all the required information to build the prompt.

## Acceptance Criteria (BDD Format)
- **Given** I am on the template usage page
- **When** the form renders
- **Then** I see fields corresponding to the template variables with localized labels
- **And** client-side validation enforces rules (e.g., required, regex, limits)

## Technical Implementation Details
- **Frontend Layer**:
  - Dynamic form rendering based on `template_variables` JSONB: `input_type` determines field component (text, textarea, select, multiselect, number, boolean, slider, etc.).
  - Labels, placeholders, and help text pulled from JSONB i18n data based on current locale.
  - Client-side validation per variable configuration: `min`, `max`, `regex`, `minLength`, `is_required`.
  - Generate button disabled until all required fields pass validation.
- **Backend Layer**:
  - Re-validates all inputs server-side (frontend is never trusted).
  - `template_variables` configuration served via `GET /api/v1/templates/{id}`.
- **Database Layer**:
  - `template_variables` table with JSONB columns for `options`, `validation`, `label` (i18n).

## Verification & Testing
- Select a template → verify correct field types render (text, textarea, select, etc.).
- Test validation: leave required field empty → Generate button stays disabled.
- Test regex validation → verify inline error message from `validation.message_i18n`.
- Switch locale → verify labels and placeholders update to the selected language.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
