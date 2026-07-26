# User Story 3.1: Select the target AI Model for a prompt (UC-03.01)

## Overview
- **Epic**: Epic 3: Prompt Generation Engine
- **Priority**: P1
- **User Persona**: User

## Story Description
- **As a** User,
- **I want to** select a target AI model for my template,
- **So that** the generated prompt uses the optimal format for that specific AI.

## Acceptance Criteria (BDD Format)
- **Given** I am on the template usage page
- **When** I select an AI model from the supported models dropdown
- **Then** the system prepares to use the specific template variant for that model if it exists

## Technical Implementation Details
- **Frontend Layer**:
  - Model selection dropdown populated from `template_models` (via `ai_models` table).
  - Auto-select and hide dropdown if template supports only one model (marked `is_primary`).
  - On model change: load corresponding `template_variants.prompt_body_override` if exists; otherwise use original `prompt_body`.
- **Backend Layer**:
  - Model data served via `GET /api/v1/templates/{id}` (includes variants per model).
- **Database Layer**:
  - `template_models`, `template_variants`, `ai_models` tables.

## Verification & Testing
- Select a template with multiple models → verify dropdown shows all supported models.
- Switch model → verify variant loads correctly (different prompt body if variant exists).
- Template with single model → verify dropdown is hidden and model is auto-selected.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
