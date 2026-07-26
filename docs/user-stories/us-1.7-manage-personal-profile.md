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
  - Profile settings page at `/settings/profile`.
  - React Hook Form for field validation.
  - Image upload component (accepts png/jpg, max 2MB).
  - Locale change triggers immediate i18n update via i18next.
- **Backend Layer**:
  - `GET /api/v1/users/me` to load current profile data.
  - `PATCH /api/v1/users/me` to save changes.
  - Validates: unique username, image size <= 2MB, image format (png/jpg).
  - Avatar uploaded to S3/MinIO.
- **Database Layer**:
  - Update `users` table (`full_name`, `avatar_url`, `bio`, `username`, `locale`, `timezone`).

## Verification & Testing
- Update profile fields (full name, bio, timezone) → verify saved and displayed correctly.
- Try duplicate username → expect `409 Conflict` with suggestion.
- Upload avatar > 2MB → expect `413 Payload Too Large`.
- Change locale from EN to VI → verify UI language switches immediately.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
