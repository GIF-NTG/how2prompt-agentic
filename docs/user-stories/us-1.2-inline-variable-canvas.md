# User Story 1.2: Inline Variable Canvas Editor

## Overview
- **Epic**: Epic 1: Keyboard-First Prompt Creation Workspace
- **Priority**: P1 (Critical MVP path)
- **User Persona**: Guest (Unauthenticated) or Member (Authenticated)

## Story Description
- **As a** Guest or Member,
- **I want to** navigate and fill placeholder fields directly inside the template sentence flow,
- **So that** I can write my prompt parameters seamlessly.

## Acceptance Criteria (BDD Format)
- **Given** a prompt template is loaded onto the Variable Canvas.
- **When** the workspace renders the template text.
- **Then** placeholder fields (e.g., `{code_to_review}`, `{environment}`) render as inline text input pills styled distinctively.
- **When** the user presses the `Tab` key.
- **Then** the input focus cycles forward to the next inline input pill.
- **When** they press `Shift+Tab`.
- **Then** the focus cycles backward to the previous inline input pill.
- **When** the user types text into an inline input pill.
- **Then** the input pill auto-adjusts its width dynamically based on the character length typed, keeping the surrounding sentence layout natural and preventing wrap-breaking.

## Technical Implementation Details
- **Frontend Layer**:
  - React components representing the Variable Canvas workspace.
  - Template parsing: Parsed raw template text (e.g., matching `{placeholder_name}`) and dynamically injected editable inline text input elements.
  - **Auto-resize Input Width calculation**: To calculate the dynamic width of an input pill without sentence wrapping glitches, the React application uses an off-screen hidden `span` element that mirrors the typed text and inherits the input's font family, weight, and size. The dynamic width is measured from this `span` client width plus a padding buffer (e.g., `16px`) and applied to the input style `width` in real-time as per [how2prompt-agentic/agent/BA.md](how2prompt-agentic/agent/BA.md) and [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md).
  - Navigation support: The tab index of these inline input elements is managed in order to allow standard `Tab` and `Shift+Tab` keyboard focus cycles.
- **Styles**:
  - Distinctive styling for inline input pills (e.g. rounded borders, custom backgrounds, focus rings, placeholder color).
  - Ensuring no wrap-breaking when text resizing takes place (using flex wrapping layouts or whitespace handling CSS attributes).

## Verification & Testing
- Select a template and verify that placeholders render as inline pills inline inside sentences.
- Test `Tab` and `Shift+Tab` navigation to ensure focus cycle works seamlessly.
- Type in each pill and observe that the width changes dynamically under 50ms without overlapping other characters or wrapping mid-word.
- Refer to [how2prompt-agentic/agent/BA.md](how2prompt-agentic/agent/BA.md), [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md), and [how2prompt-agentic/docs/epics.md](how2prompt-agentic/docs/epics.md) for full system specifications.
