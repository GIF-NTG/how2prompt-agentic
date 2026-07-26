# User Story 3.3: View real-time prompt preview (UC-03.03)

## Overview
- **Epic**: Epic 3: Prompt Generation Engine
- **Priority**: P1
- **User Persona**: User

## Story Description
- **As a** User,
- **I want to** see a real-time preview of the prompt as I type,
- **So that** I can see exactly what the final prompt will look like.

## Acceptance Criteria (BDD Format)
- **Given** I am filling in the dynamic form
- **When** I type in a field
- **Then** the prompt preview panel updates instantly to show the replaced values

## Technical Implementation Details
- **Frontend Layer**:
  - Client-side Template Renderer runs on every field `onChange` event.
  - Replaces `{{placeholder}}` with current value; shows placeholder styling for unfilled variables.
  - Monospace display with syntax highlighting for unfilled placeholders.
  - Character count and token estimate (using `tiktoken` library or heuristic).
  - Preview render target: < 50ms.
- **Backend Layer**:
  - N/A — the preview is client-side only. The final prompt is always re-rendered by the backend (US-3.6) at generation time.

## Verification & Testing
- Type in form fields → verify preview updates in real-time on every keystroke.
- Verify unfilled placeholders are visually distinct (highlighted/styled differently).
- Measure preview render time → must be < 50ms.
- Verify character count and token estimate update as text changes.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
