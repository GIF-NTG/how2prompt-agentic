# User Story 5.1: Manage AI Models (UC-05.01)

## Overview
- **Epic**: Epic 5: Admin & Content Management
- **Priority**: P1
- **User Persona**: Admin

## Story Description
- **As a** Admin,
- **I want to** manage the catalog of supported AI models,
- **So that** the system stays up to date with the latest AI capabilities.

## Acceptance Criteria (BDD Format)
- **Given** I am on the '/admin/ai-models' page
- **When** I create or edit a model
- **Then** the changes are saved and reflected in the model selection dropdowns

## Technical Implementation Details
- **Frontend Layer**:
  - Protected admin route at `/admin/ai-models` (requires `is_admin = true`).
  - Data table with CRUD forms for model management.
  - Fields: `code`, `name`, `provider`, `model_type`, `capabilities` (JSONB), `default_config`, `icon`, `is_active`, `sort_order`.
- **Backend Layer**:
  - `GET /api/v1/admin/ai-models` — list all models (including inactive).
  - `POST /api/v1/admin/ai-models` — create new model.
  - `PATCH /api/v1/admin/ai-models/{id}` — update model.
  - Role-based authorization: `hasRole('ADMIN')`.
- **Database Layer**:
  - CRUD operations on `ai_models` table.
  - Cannot delete a model if templates reference it — must deactivate (`is_active=false`) instead.

## Verification & Testing
- Log in as Admin → navigate to `/admin/ai-models` → CRUD a model.
- Verify model changes reflected in model selection dropdowns across the app.
- Try deleting a model with attached templates → verify blocked; must deactivate instead.
- Access `/admin/ai-models` as a normal user → expect `403 Forbidden`.
- Refer to [BA.md](../../.agent/BA.md), [srs.md](../srs.md), and [use-cases.md](../use-cases.md) for full system specifications.
