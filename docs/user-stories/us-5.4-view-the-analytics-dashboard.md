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
  - Protected admin route at `/admin/dashboard` (requires `is_admin = true`).
  - Charts (line, bar, pie) and data tables for metrics visualization.
  - Date range filter for custom time periods.
- **Backend Layer**:
  - Aggregated queries returning: DAU/WAU/MAU, prompts generated per day, most popular templates, most-used AI models, signup → first-generate conversion funnel.
  - Results cached for 5 minutes to reduce database load.
  - Role-based authorization: `hasRole('ADMIN')`.
- **Database Layer**:
  - Aggregate queries across `users`, `generated_prompts`, `templates`, `ai_models` tables.

## Verification & Testing
- Navigate to `/admin/dashboard` → verify metrics and charts render correctly.
- Apply a date range filter → verify data updates to match the selected period.
- Verify cache behavior: data stays consistent for 5 minutes.
- Access `/admin/dashboard` as a normal user → expect `403 Forbidden`.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
