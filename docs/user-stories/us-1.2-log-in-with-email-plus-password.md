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
