# User Story 5.5: Review User-Submitted Templates (UC-05.04)

## Overview
- **Epic**: Epic 5: Admin & Content Management
- **Priority**: High
- **User Persona**: Admin

## Story Description
- **As an** Admin,
- **I want to** review templates submitted by users for community publication,
- **So that** only quality, policy-compliant templates become publicly visible.

## Acceptance Criteria (BDD Format)
- **Given** a template has `status='pending'` (submitted by its author via US-7.5)
- **When** I open `/admin/moderation` → 'Pending Templates' tab
- **Then** I see the template listed with author information
- **And** I can view its details and test-render the prompt with sample input.
- **Given** I am reviewing a pending template
- **When** I click Approve
- **Then** the template moves to `status='published'`, `is_public=true`
- **And** the author is notified.
- **Given** I am reviewing a pending template
- **When** I click Reject and provide a `rejection_reason`
- **Then** the template's status is updated to rejected
- **And** the author receives a notification with the reason.
- **Given** a pending template needs minor fixes rather than outright rejection
- **When** I request changes with a comment
- **Then** the template's status reverts to `draft` with my comment attached for the author to address.

## Technical Implementation Details
- **Frontend Layer**:
  - `/admin/moderation` page with a 'Pending Templates' tab, listing templates filtered by `status='pending'`.
  - Detail view with a live test-render panel (reuses the dynamic form + preview renderer from US-3.2/US-3.3).
  - Approve / Reject / Request changes actions, with a required reason field for Reject and Request changes.
- **Backend Layer**:
  - `GET /api/v1/admin/templates?status=pending` — list pending templates with author info.
  - `POST /api/v1/admin/templates/{id}/approve` — sets `status='published'`, `is_public=true`, `published_at=NOW()`; triggers author notification.
  - `POST /api/v1/admin/templates/{id}/reject` — sets `status='rejected'`, stores `rejection_reason`; triggers author notification.
  - `POST /api/v1/admin/templates/{id}/request-changes` — sets `status='draft'`, stores the review comment; triggers author notification.
- **Database Layer**:
  - `templates.status` transitions: `pending` → `published` | `rejected` | `draft`.
  - Store `rejection_reason` / review comment on the template or a related moderation-log record.

## Business Rules
- Review SLA of 48 hours.
- Content that trips automated spam/keyword filters is auto-rejected before reaching the admin queue (see US-7.5 exception flow).

## Verification & Testing
- Submit a template as a user (US-7.5) → verify it appears in `/admin/moderation` pending queue.
- Approve a pending template → verify `status='published'`, `is_public=true`, and it now appears in `/explore` (US-2.1).
- Reject a pending template with a reason → verify `status='rejected'` and the author receives the reason.
- Request changes → verify `status='draft'` and the comment is visible to the author in their template editor.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
