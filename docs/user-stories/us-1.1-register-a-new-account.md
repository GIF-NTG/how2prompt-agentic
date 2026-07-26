# User Story 1.1: Register a new account (UC-01.01)

## Overview
- **Epic**: Epic 1: User Identity & Access Management
- **Priority**: P1
- **User Persona**: Guest

## Story Description
- **As a** Guest,
- **I want to** register a new account using my email,
- **So that** I can use the platform and have my own personal workspace.

## Acceptance Criteria (BDD Format)
- **Given** I am on the Register page
- **When** I submit valid email, password, display name, and locale
- **Then** the system creates my account and my personal workspace
- **And** the system sends a verification email
- **And** I receive access and refresh tokens and am redirected to the home page

## Technical Implementation Details
- **Frontend Layer**:
  - React Hook Form for email format and password strength validation (>= 8 chars, letters + numbers).
  - JWT token storage: access token in memory, refresh token in httpOnly cookie.
  - Redirect to home page with verification banner after successful registration.
- **Backend Layer**:
  - `POST /api/v1/auth/register` endpoint.
  - BCrypt password hashing (cost >= 12).
  - Auto-create Personal Workspace (`type='personal'`) and appoint user as owner.
  - Send verification email via SendGrid/Resend (token valid 24h).
  - Rate limit: 10 requests/minute/IP.
- **Database Layer**:
  - Insert into `users`, `workspaces`, and `workspace_members` tables.

## Verification & Testing
- Fill registration form with valid data → verify account created, redirected to home with verification banner.
- Check browser httpOnly cookie for refresh token; verify access token is NOT in cookie/localStorage.
- Try registering with duplicate email → expect `409 Conflict`.
- Try weak password (e.g., "123") → expect `422 Unprocessable Entity`.
- Exceed rate limit → expect `429 Too Many Requests`.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
