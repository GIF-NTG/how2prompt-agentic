# User Story 1.3: Local Draft Backup & State Clear

## Overview
- **Epic**: Epic 1: Keyboard-First Prompt Creation Workspace
- **Priority**: P1 (Critical MVP path)
- **User Persona**: Guest (Unauthenticated) or Member (Authenticated)

## Story Description
- **As a** Guest or Member,
- **I want to** my progress to be backed up locally and have the ability to reset the canvas,
- **So that** I don't lose typed text on accidental refresh and can start fresh easily.

## Acceptance Criteria (BDD Format)
- **Given** the user is typing values into template variable pills.
- **When** the user types characters (on `change` events).
- **Then** the client application automatically serializes and saves the draft values into browser `localStorage` keyed by template UUID.
- **When** the user performs a hard page refresh (F5) or closes and reopens the browser tab.
- **Then** the Variable Canvas retrieves the draft values from `localStorage` and restores them on load.
- **When** the user presses the "Reset" button (or triggers the `Esc` hotkey).
- **Then** the system clears all input pills on the canvas and removes the draft from `localStorage`.

## Technical Implementation Details
- **Frontend Layer**:
  - React State management synchronized with local storage.
  - Keying scheme: Drafts must be stored in `localStorage` using a key mapped to the template UUID (e.g. `how2prompt_draft_<template_id>`).
  - Serializing variables: On changes, the local state dictionary is serialized (JSON) and committed to `localStorage`.
  - Restore on load: `useEffect` executes on template load, retrieves the key from `localStorage`, parses the JSON object, and populates the canvas variables state.
  - Reset function: Clears the React variable values state, sets input widths back to initial default sizes, and calls `localStorage.removeItem(key)`.
  - Hotkey listener: Captures `Escape` (`Esc`) keydown globally to trigger the canvas reset function.

## Verification & Testing
- Load a template, fill in some text in the variable fields.
- Perform a hard refresh (F5) or close the tab, then reopen the page to confirm text is restored.
- Press `Escape` or click the "Reset" button to confirm all input values are cleared and removed from browser storage.
- Refer to [how2prompt-agentic/agent/BA.md](how2prompt-agentic/agent/BA.md), [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md), and [how2prompt-agentic/docs/epics.md](how2prompt-agentic/docs/epics.md) for full system specifications.
