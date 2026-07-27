# User Story 1.2: Log in with email + password (UC-01.02)

## Overview
- **Epic**: Epic 1: User Identity & Access Management
- **Priority**: P1
- **User Persona**: Registered User

## Story Description
- **As a** Registered User,
- **I want to** log in with my email and password,
- **So that** I can access my workspace and saved prompts.

## Acceptance Criteria (BDD Format)
- **Given** I have a registered account
- **When** I submit the correct email and password
- **Then** I am authenticated and redirected to the dashboard
- **And** the system issues access and refresh tokens

## Technical Implementation Details
- **Frontend Layer**:
  - React Hook Form for email/password validation.
  - JWT token storage: access token in memory, refresh token in httpOnly cookie.
  - Redirect to dashboard on success.
- **Backend Layer**:
  - `POST /api/v1/auth/login` endpoint.
  - BCrypt credential verification against `password_hash`.
  - Update `users.last_login_at`, create `refresh_tokens` record (30-day validity).
  - Access token signed with RS256 (asymmetric), 15-minute validity.
  - Refresh tokens rotate on each use.
  - Brute force protection: 5 failed attempts in 15 min → CAPTCHA required.
- **Database Layer**:
  - Read from `users` table; insert into `refresh_tokens` table.

## Verification & Testing
- Login with valid credentials → redirected to dashboard; verify httpOnly cookie set.
- Login with wrong email/password → expect `401 Unauthorized` (must not reveal which field is wrong).
- Attempt 5 failed logins within 15 min → verify CAPTCHA lock triggers.
- Verify access token expires after 15 min and auto-refreshes if refresh token is valid.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
