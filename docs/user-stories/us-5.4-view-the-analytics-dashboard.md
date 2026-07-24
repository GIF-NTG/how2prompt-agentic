# User Story 5.4: View the analytics dashboard (UC-05.05)

## Overview
- **Epic**: Epic 5: Admin & Content Management
- **Priority**: P2
- **User Persona**: Admin

## Story Description
- **As a** Admin,
- **I want to** view system analytics,
- **So that** I can monitor active users, generated prompts, and popular templates.

## Acceptance Criteria (BDD Format)
- **Given** I navigate to the '/admin/dashboard'
- **When** the dashboard loads
- **Then** I see aggregated metrics and charts cached from the database

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
