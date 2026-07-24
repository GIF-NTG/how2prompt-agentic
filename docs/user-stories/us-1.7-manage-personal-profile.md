# User Story 1.7: Manage personal profile (UC-01.07)

## Overview
- **Epic**: Epic 1: User Identity & Access Management
- **Priority**: P2
- **User Persona**: Logged-in User

## Story Description
- **As a** Logged-in User,
- **I want to** update my profile information,
- **So that** my personal details and locale preferences are accurate.

## Acceptance Criteria (BDD Format)
- **Given** I am on the Profile Settings page
- **When** I update my full name, avatar, bio, username, locale, or timezone
- **Then** the system validates and saves the changes
- **And** the UI immediately reflects my locale preference

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
