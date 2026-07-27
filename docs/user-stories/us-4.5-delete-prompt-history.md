# User Story 4.5: Delete prompt history (UC-04.05)

## Overview
- **Epic**: Epic 4: Prompt History & Favorites
- **Priority**: P2
- **User Persona**: Logged-in User

## Story Description
- **As a** Logged-in User,
- **I want to** delete items from my prompt history,
- **So that** I can remove failed or unnecessary prompts.

## Acceptance Criteria (BDD Format)
- **Given** I am viewing my history
- **When** I click the delete button on an item and confirm
- **Then** the item is soft-deleted and removed from the list

## Technical Implementation Details
- **Frontend Layer**:
  - Delete button (trash icon) on each history item.
  - Confirmation dialog before deletion.
  - Bulk-select with "Delete selected" option.
  - Optimistic UI: item removed from list immediately.
- **Backend Layer**:
  - `DELETE /api/v1/generated-prompts/{id}` endpoint.
  - Sets `deleted_at = NOW()` (soft-delete, not hard-delete).
- **Database Layer**:
  - Update `generated_prompts.deleted_at` column.
  - Soft-deleted records preserved for audit trail; restorable within 30 days (Phase 2).

## Verification & Testing
- Click delete on a history item → confirm → verify item removed from list.
- Verify `generated_prompts.deleted_at` is set (not physically deleted).
- Test bulk delete: select multiple items → delete → verify all removed.
- Verify deleted items no longer appear in `/history` queries.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
