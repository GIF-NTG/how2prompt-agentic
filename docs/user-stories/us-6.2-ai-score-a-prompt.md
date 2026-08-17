# User Story 6.2: AI Score a Prompt (UC-06.02)

## Overview
- **Epic**: Epic 6: AI Enhancement
- **Priority**: Medium
- **User Persona**: Logged-in User

## Story Description
- **As a** logged-in User,
- **I want to** have AI score my generated prompt against quality criteria,
- **So that** I understand its strengths and weaknesses before using it.

## Acceptance Criteria (BDD Format)
- **Given** I have already generated a prompt
- **When** I click `[Score this prompt]`
- **Then** the backend calls the LLM with a meta-prompt requesting a score across 4 criteria: clarity, specificity, context, format (scale 0-10)
- **And** the LLM returns JSON `{ clarity, specificity, context, format, overall, suggestions[] }`
- **And** the backend saves it to `generated_prompts.ai_score`
- **And** the frontend renders a radar chart plus a list of improvement suggestions.

## Technical Implementation Details
- **Frontend Layer**:
  - `[Score this prompt]` action on the generated-prompt result view.
  - Radar chart component (4 axes: clarity, specificity, context, format) + suggestions list.
  - Visible disclaimer: "AI assessment for reference only".
- **Backend Layer**:
  - `POST /api/v1/generated-prompts/{id}/score` — calls the LLM Adapter with a scoring meta-prompt, parses the JSON response.
- **Database Layer**:
  - Persist the score payload to `generated_prompts.ai_score` (JSONB).

## Business Rules
- Results may be inaccurate — a disclaimer 'AI assessment for reference only' must always be displayed alongside the score.

## Verification & Testing
- Generate a prompt, click Score → verify radar chart renders with 4 criteria and an overall score.
- Verify the disclaimer is always visible next to the score.
- Verify `ai_score` is persisted and re-displayed when revisiting the prompt from history.
- Simulate a malformed LLM JSON response → verify graceful error handling, not a raw parse crash.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
