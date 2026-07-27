# User Story 1.6: Verify email (UC-01.06)

## Overview
- **Epic**: Epic 1: User Identity & Access Management
- **Priority**: P1
- **User Persona**: Newly Registered User

## Story Description
- **As a** Newly Registered User,
- **I want to** verify my email address,
- **So that** my account is fully activated.

## Acceptance Criteria (BDD Format)
- **Given** I have received a verification email
- **When** I click the verification link
- **Then** my email is marked as verified
- **And** the verification reminder banner disappears

## Technical Implementation Details
- **Frontend Layer**:
  - Handle verification link redirect; display success message.
  - Verification reminder banner on home page (dismisses after verification).
  - "Resend verification email" button on the banner.
- **Backend Layer**:
  - `GET /api/v1/auth/verify-email?token=...` endpoint.
  - Update `users.email_verified_at = NOW()` upon valid token.
  - Resend rate limit: once per 5 minutes per user.
- **Database Layer**:
  - Update `users` table (`email_verified_at` column).

## Verification & Testing
- Click verification link in email → verify `email_verified_at` is set, banner disappears.
- Try expired or invalid token → verify error message displayed.
- Click "Resend" within 5 minutes → verify rate limit enforced.
- Verify unverified users can still use the app but with restrictions (no public templates, no AI Refine).
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
