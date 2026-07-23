# User Story 3.3: History Deletion

## Overview
- **Epic**: Epic 3: Stateless Optimization & History Management
- **Priority**: P2
- **User Persona**: Member (Authenticated)

## Story Description
- **As a** Member,
- **I want to** delete specific logs from my history,
- **So that** I can keep my history feed clean.

## Acceptance Criteria (BDD Format)
- **Given** a Member is viewing history rows in the Quick-History Drawer.
- **When** they click the "Delete" icon on a row.
- **Then** the React SPA sends a `DELETE /api/v1/history/{id}` request.
- **And** the Spring Boot service deletes the record from the `history` table.
- **And** the UI immediately filters out the deleted card from the list.

## Technical Implementation Details
- **Frontend Layer**:
  - Delete UI button element on each history row/card inside the drawer.
  - Dispatch a `DELETE /api/v1/history/{id}` API request asynchronously on click.
  - Optimistic UI or immediate state filtering: Clean the history list in the frontend state using a filter function (e.g. `setHistory(prev => prev.filter(item => item.id !== id))`), avoiding full drawer re-fetch and ensuring immediate visual update.
- **Backend API Layer (Spring Boot)**:
  - REST endpoint: `DELETE /api/v1/history/{id}`.
  - Requires active user JWT session verification, checking that the requested resource ID belongs to the authenticated user (prevents unauthorized deletions).
  - Uses `@Transactional` configuration on the service level.
- **Database Layer**:
  - Executes database deletion statement on the `history` (or `prompt_histories`) table for the given UUID key.

## Verification & Testing
- Open the Quick-History Drawer, locate an entry, and click the delete button.
- Verify that the card is removed from the UI instantly.
- Verify that a `DELETE /api/v1/history/{id}` request is sent with `HTTP 200 OK` or `HTTP 204 No Content` status.
- Reload the drawer (or the page) to confirm that the deleted record is no longer present.
- Refer to [how2prompt-agentic/agent/BA.md](how2prompt-agentic/agent/BA.md), [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md), and [how2prompt-agentic/docs/epics.md](how2prompt-agentic/docs/epics.md) for full system specifications.
