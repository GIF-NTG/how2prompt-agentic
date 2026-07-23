# User Story 1.1: Dashboard Layout & Command Palette Search

## Overview
- **Epic**: Epic 1: Keyboard-First Prompt Creation Workspace
- **Priority**: P1 (Critical MVP path)
- **User Persona**: Guest (Unauthenticated) or Member (Authenticated)

## Story Description
- **As a** Guest or Member,
- **I want to** use a command palette to quickly search and load empty prompt templates,
- **So that** I can select my workspace in under 50ms without using a mouse.

## Acceptance Criteria (BDD Format)
- **Given** a user is on the homepage dashboard.
- **When** they press the shortcut key combination `Ctrl+K`.
- **Then** the Command Palette search overlay toggles open with focus set on the search input box.
- **When** the user types a search query (e.g., "debug").
- **Then** the catalog performs fuzzy-search and filters templates matching the query in title, tags, or description.
- **When** the search results render.
- **Then** the latency of filtering and rendering results MUST be under 50ms.
- **When** the user selects a template card using arrow keys and presses `Enter` (or clicks the card).
- **Then** the selected template loads onto the Variable Canvas workspace, and the Command Palette closes.

## Technical Implementation Details
- **Frontend Layer**:
  - React components representing the Dashboard view and the Search Command Palette modal overlay.
  - Global `keydown` keyboard listener to capture `Ctrl+K` key combination to toggle the Command Palette.
  - Support for keyboard navigation within results: arrow keys (`ArrowDown`, `ArrowUp`) to hover and navigate, `Enter` to select and execute, and `Escape` to close.
  - Performance requirement: fuzzy-matching and rendering must perform under 50ms latency locally, ensuring FCP is under 200ms and TTI is under 500ms as per [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md).
- **Backend API Layer**:
  - REST endpoint: `GET /api/v1/templates` (returning the list of public template cards: ID, title, description, raw template string, and tags).
  - Controller-Service-Repository-Entity pattern in Spring Boot.
- **Database Layer**:
  - `templates` table: UUID primary keys, titles, descriptions, raw templates, and tags (represented as `VARCHAR[]` in PostgreSQL).
- **Exception & Edge Cases**:
  - If backend is down or template loading fails, show a clean fallback UI with helpful error message (RFC-7807 error envelopes mapped cleanly).
  - Empty search inputs should restore the list to all default templates instantly.

## Verification & Testing
- Pressing `Ctrl+K` toggles open the palette overlay.
- Searching for a query filters items.
- Navigating results using arrow keys highlights active element; pressing `Enter` loads the template onto the Canvas.
- Refer to [how2prompt-agentic/agent/BA.md](how2prompt-agentic/agent/BA.md), [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md), and [how2prompt-agentic/docs/epics.md](how2prompt-agentic/docs/epics.md) for full system specifications.
