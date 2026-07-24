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
  - React Hook Form for validation.
  - JWT token storage (access in memory, refresh in httpOnly cookie).
- **Backend Layer**:
  - Spring Boot Gateway for auth endpoints.
  - BCrypt password hashing.
- **Database Layer**:
  - PostgreSQL `users` and `workspaces` tables.

## Verification & Testing
- Navigate to the relevant auth page.
- Submit valid and invalid data to observe success redirects and error states.
- Check browser cookies for refresh token.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [epics-and-stories.md](../epics-and-stories.md) for full system specifications.
