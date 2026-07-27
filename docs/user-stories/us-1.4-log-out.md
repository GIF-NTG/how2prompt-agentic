# User Story 1.4: Log out (UC-01.04)

## Overview
- **Epic**: Epic 1: User Identity & Access Management
- **Priority**: P1
- **User Persona**: Logged-in User

## Story Description
- **As a** Logged-in User,
- **I want to** log out of my account,
- **So that** my session is securely terminated on this device.

## Acceptance Criteria (BDD Format)
- **Given** I am logged in
- **When** I click 'Log out' from the profile menu
- **Then** my refresh token is revoked and the client session is cleared
- **And** I am redirected to the public home page

## Technical Implementation Details
- **Frontend Layer**:
  - Clear access token from Zustand store (in-memory).
  - Redirect to the public home page after logout.
- **Backend Layer**:
  - `POST /api/v1/auth/logout` endpoint.
  - Set `revoked_at = NOW()` on the current `refresh_tokens` record.
  - Clear the httpOnly cookie containing the refresh token.
- **Database Layer**:
  - Update `refresh_tokens` table (`revoked_at` column).

## Verification & Testing
- Click "Log out" from profile menu → verify redirected to public home page.
- Verify httpOnly cookie is cleared (no refresh token in browser).
- Verify access token is no longer in memory (Zustand store reset).
- Attempt to access a protected route after logout → verify redirect to login page.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
