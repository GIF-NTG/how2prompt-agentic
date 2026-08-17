# User Story 7.5: Submit a Template for Community Review (UC-07.05)

## Overview
- **Epic**: Epic 7: Template Customization & Versioning
- **Priority**: Medium
- **User Persona**: Author (template owner)

## Story Description
- **As an** Author with a draft template that has valid variables and a `prompt_body`,
- **I want to** submit it for community review,
- **So that** it can become a publicly available template after admin approval.

## Acceptance Criteria (BDD Format)
- **Given** my template is in draft status with sufficient content
- **When** I click `[Submit for review]`
- **Then** the frontend shows a checklist (cover image, i18n description, example output, guide, at least 1 category)
- **And** if the checklist passes, it calls `POST /api/v1/templates/{id}/submit`
- **And** the backend sets `status='pending'` and notifies the admin moderation queue
- **And** I receive a confirmation email.

## Exception Scenarios
- Content violation (e.g., keyword spam) → the submission is auto-rejected with an explanatory message, without entering the admin queue.

## Technical Implementation Details
- **Frontend Layer**:
  - `[Submit for review]` action in the template editor, with a pre-flight checklist gating the call.
- **Backend Layer**:
  - `POST /api/v1/templates/{id}/submit` — validates required fields, runs an automated content/spam filter, sets `status='pending'` on pass, sends author confirmation email and admin queue notification.
- **Database Layer**:
  - `templates.status` transitions `draft` → `pending` (or stays `draft` with an auto-rejection reason on spam-filter failure).

## Business Rules
- The pending template then follows the moderation flow in US-5.5 (Review User-Submitted Templates).

## Verification & Testing
- Submit an incomplete template (missing cover image/category) → verify the checklist blocks submission client-side.
- Submit a complete, compliant template → verify `status='pending'`, admin queue notified, author receives confirmation email.
- Submit content that trips the spam/keyword filter → verify auto-rejection with a message, and that it never reaches `status='pending'`.
- After admin approval (US-5.5) → verify the template becomes visible in `/explore`.
- Refer to [BA.md](../../agent/BA.md), [SRS.md](../SRS.md), and [use-cases.md](../use-cases.md) for full system specifications.
