# User Story 6.3: Translate a Prompt Between Models (UC-06.04)

## Overview
- **Epic**: Epic 6: AI Enhancement
- **Priority**: Medium
- **User Persona**: Logged-in User

## Story Description
- **As a** logged-in User,
- **I want to** convert a prompt written for one AI model into the equivalent for another model,
- **So that** I can reuse my prompt on a different tool without rewriting it by hand.

## Acceptance Criteria (BDD Format)
- **Given** I have a generated prompt optimized for one model
- **When** I click `[Translate to another model]` and select the target model
- **Then** the backend calls the LLM with a meta-prompt instructing it to convert the prompt's syntax/style to the target model while preserving the original intent
- **And** the new prompt is returned and saved to history as a separate record (the original is not overwritten).

## Technical Implementation Details
- **Frontend Layer**:
  - `[Translate to another model]` action with a target-model selector (reuses the model dropdown from US-3.1).
  - Displays the translated result as a new, distinct prompt (not a diff against the original).
- **Backend Layer**:
  - `POST /api/v1/generated-prompts/{id}/translate` — calls the LLM Adapter with a translation meta-prompt (e.g., "Convert the following prompt from ChatGPT to a style suited for Claude, preserving the original intent").
  - Creates a new `generated_prompts` record referencing the source prompt.
- **Database Layer**:
  - New `generated_prompts` row with a pointer back to the source prompt (e.g., `translated_from_prompt_id`).

## Business Rules
- Especially relevant when converting from a text prompt to an image-generation prompt (Midjourney/DALL·E) — this requires a significant structural rewrite, not just wording changes.

## Verification & Testing
- Translate a text-model prompt to another text model → verify a new history record is created and the original is untouched.
- Translate a text prompt to an image-model prompt (e.g., Midjourney) → verify the structural rewrite (aspect ratio, style tags, etc.) is present.
- Verify the translated record links back to its source prompt.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
