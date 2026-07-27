# User Story 3.6: Backend renders the prompt (UC-03.06)

## Overview
- **Epic**: Epic 3: Prompt Generation Engine
- **Priority**: P1
- **User Persona**: System

## Story Description
- **As a** System,
- **I want to** securely render the final prompt,
- **So that** validation is enforced and exact data is saved for history.

## Acceptance Criteria (BDD Format)
- **Given** the frontend submits the generate request
- **When** the backend receives it
- **Then** it validates the input, safely replaces placeholders, sanitizes the text, and returns the final string

## Technical Implementation Details
- **Frontend Layer**:
  - N/A — this is a system-level backend operation.
- **Backend Layer**:
  - Render engine (Mustache/Handlebars-style): `{{var_key}}` → `input_values[var_key]`.
  - Load `template_versions` and `template_variants`; select `prompt_body_override` if variant exists, otherwise use `version.prompt_body`.
  - Handle `default_value`: if input is empty and default exists → use default; if optional and empty → remove placeholder + trim whitespace.
  - Append `extra_instructions` per UC-03.04 rules.
  - Sanitize output (remove unusual control characters).
  - Re-validate all inputs server-side (required, regex) — frontend is never trusted.
  - Renderer is a separate service with >= 90% unit test coverage.
- **Database Layer**:
  - Read: `template_versions`, `template_variants`. Write: `generated_prompts` with `final_prompt`, `input_values` (JSONB), `workspace_id`, `ai_model_id`, `template_version_id`.

## Verification & Testing
- Verify backend render matches frontend preview for identical inputs.
- Test with all variable types (text, select, multiselect, boolean, etc.).
- Test default values: leave a field with a default empty → verify default is used.
- Test empty optional variables → verify placeholder is removed and whitespace is trimmed.
- Verify renderer unit test coverage >= 90%.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
