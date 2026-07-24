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
