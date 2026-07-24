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
