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
