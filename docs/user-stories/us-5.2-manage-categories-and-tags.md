# User Story 5.2: Manage Categories & Tags (UC-05.02)

## Overview
- **Epic**: Epic 5: Admin & Content Management
- **Priority**: P1
- **User Persona**: Admin

## Story Description
- **As a** Admin,
- **I want to** manage categories and tags,
- **So that** templates are properly organized and searchable.

## Acceptance Criteria (BDD Format)
- **Given** I am on the '/admin/taxonomy' page
- **When** I create, edit, or merge categories and tags
- **Then** the taxonomy tree is updated and template associations are maintained

## Technical Implementation Details
- **Frontend Layer**:
  - Protected admin routes using Higher Order Components (HOC).
  - Data tables for CRUD operations.
- **Backend Layer**:
  - Role-based authorization (`hasRole('ADMIN')`).
- **Database Layer**:
  - CRUD operations on taxonomy and model tables.

## Verification & Testing
- Log in as an Admin and navigate to the admin dashboard.
- Create or edit an entity and verify changes reflect in the database.
- Attempt to access admin routes as a normal user and verify 403 Forbidden.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [epics-and-stories.md](../epics-and-stories.md) for full system specifications.
