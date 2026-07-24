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
