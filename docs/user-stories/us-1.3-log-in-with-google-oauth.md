# User Story 1.3: Log in with Google OAuth (UC-01.03)

## Overview
- **Epic**: Epic 1: User Identity & Access Management
- **Priority**: P1
- **User Persona**: Guest

## Story Description
- **As a** Guest,
- **I want to** log in using my Google account,
- **So that** I can access the platform quickly without creating a new password.

## Acceptance Criteria (BDD Format)
- **Given** I click 'Sign in with Google'
- **When** I approve the consent on Google's authorization page
- **Then** the system logs me in
- **And** if I don't have an account, the system automatically creates one along with a personal workspace

## Technical Implementation Details
- **Frontend Layer**:
  - "Sign in with Google" button redirects to Google OAuth Authorization endpoint with `openid email profile` scope.
  - JWT token storage: access token in memory, refresh token in httpOnly cookie.
- **Backend Layer**:
  - `GET/POST /api/v1/auth/oauth/google/callback` endpoint.
  - Exchange authorization code for ID token; verify ID token signature.
  - Check `user_identities` for `(provider='google', provider_uid)`.
  - If not found: create new `users` record + Personal Workspace + `user_identities` record.
  - If Google email matches existing email/password account → identity merge flow with confirmation.
  - Return access + refresh tokens.
- **Database Layer**:
  - `users`, `user_identities`, `workspaces`, `refresh_tokens` tables.

## Verification & Testing
- Click "Sign in with Google" → approve consent → verify logged in and redirected.
- Decline consent on Google page → verify redirected back to login with error message.
- Login with Google email that matches an existing email/password account → verify merge flow triggers.
- Google timeout/error → verify `502 Bad Gateway` with "Please try again" message.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
