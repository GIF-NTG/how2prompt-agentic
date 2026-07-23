# User Story 1.4: Prompt Compiler, Verification, & Copy Action

## Overview
- **Epic**: Epic 1: Keyboard-First Prompt Creation Workspace
- **Priority**: P1 (Critical MVP path)
- **User Persona**: Guest (Unauthenticated) or Member (Authenticated)

## Story Description
- **As a** Guest or Member,
- **I want to** the compiler to validate my inputs and copy the compiled prompt,
- **So that** I can immediately use it in external AI chats.

## Acceptance Criteria (BDD Format)
- **Given** a user is editing placeholders on the Variable Canvas.
- **When** they press `Ctrl+Enter` (or click "Hoàn thành" / "Complete").
- **And** at least one mandatory placeholder pill is left empty.
- **Then** the copy execution blocks, highlights the empty fields red, and automatically shifts focus to the first empty pill.
- **Given** all mandatory placeholder pills are filled.
- **When** they trigger the compilation.
- **Then** the Prompt Compiler resolves variables by replacing placeholders, stripping empty optional variables, removing extra whitespaces, and copying the clean compiled prompt string to the system clipboard.
- **And** the UI triggers a non-blocking toast notification reading "Copied!" (or "Đã sao chép!") which disappears after exactly 2 seconds.

## Technical Implementation Details
- **Frontend Layer**:
  - Hotkey listener: Captures `Ctrl+Enter` to trigger compilation.
  - Validation algorithm:
    - Locate variables in the current template and identify required vs. optional fields.
    - Check if any required fields are empty/whitespace-only.
    - If validation fails, apply `.has-error` CSS class (renders a red border) to all empty inputs and programmatically focus the first empty input.
  - Compiler utility:
    - Replace placeholders (e.g. `{variable}`) with their typed values.
    - Clean up optional fields if empty (or replace/strip optional syntax).
    - Sanitize multiple spaces, format paragraph spacing, and produce a clean prompt string.
  - Clipboard write: Uses browser `navigator.clipboard.writeText` API to copy the final compiled text.
  - Notification Feedback: Displays a non-blocking toast message reading "Copied!" (or "Đã sao chép!"). The component handles self-cleanup using a `setTimeout` with a duration of exactly 2000ms.

## Verification & Testing
- Load a template with placeholders, fill in half of them, and press `Ctrl+Enter`. Verify that validation blocks, highlights empty fields in red, and focuses the first empty input.
- Fill all required variables, trigger compilation, and paste clipboard contents into an editor to confirm variable replacement, spacing cleanup, and optional fields formatting.
- Verify the toast notification appears instantly and disappears after exactly 2 seconds.
- Refer to [how2prompt-agentic/agent/BA.md](how2prompt-agentic/agent/BA.md), [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md), and [how2prompt-agentic/docs/epics.md](how2prompt-agentic/docs/epics.md) for full system specifications.
