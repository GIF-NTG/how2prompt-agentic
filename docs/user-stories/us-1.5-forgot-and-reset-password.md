# User Story 1.5: Forgot & reset password (UC-01.05)

## Overview
- **Epic**: Epic 1: User Identity & Access Management
- **Priority**: P1
- **User Persona**: Guest

## Story Description
- **As a** Guest,
- **I want to** reset my password via email,
- **So that** I can recover access to my account if I forget my password.

## Acceptance Criteria (BDD Format)
- **Given** I submit my registered email in the 'Forgot password' form
- **When** I click the reset link in the email and enter a new password
- **Then** my password is updated and all old refresh tokens are revoked

## Technical Implementation Details
- **Frontend Layer**:
  - Forgot password form (email input) and reset password page (new password + confirm).
  - React Hook Form for password strength validation.
- **Backend Layer**:
  - `POST /api/v1/auth/forgot-password`: generate reset token (1h validity), send email via SendGrid/Resend.
  - `POST /api/v1/auth/reset-password`: verify token, update `password_hash` (BCrypt, cost >= 12), revoke all old refresh tokens, send confirmation email.
  - Anti-enumeration: returns `200 OK` even if email doesn't exist.
- **Database Layer**:
  - Update `users.password_hash`; bulk-revoke in `refresh_tokens` table.

## Verification & Testing
- Submit forgot password form → verify email received with reset link.
- Click reset link → set new password → verify redirected to login and can log in with new password.
- Try expired or already-used reset token → expect `410 Gone`.
- Submit non-existent email → verify still returns `200 OK` (no enumeration).
- After reset, verify all previous sessions (refresh tokens) are revoked.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
