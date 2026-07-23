# User Story 2.3: Team Variables Configuration

## Overview
- **Epic**: Epic 2: Authentication & Context Configurations
- **Priority**: P2
- **User Persona**: Team Lead (Authenticated Admin) / Member (Authenticated)

## Story Description
- **As a** Team Lead,
- **I want to** configure global team variables in the settings,
- **So that** they pre-populate automatically for my team members.

## Acceptance Criteria (BDD Format)
- **Given** a Team Lead is on the settings page.
- **When** they create/update key-value configurations (e.g., `{ "team_coding_standards": "Use Java 17 and Spring Boot MVC pattern" }`) and click save.
- **Then** the React SPA sends a `PUT /api/v1/users/me/variables` request.
- **And** the Spring Boot backend updates the PostgreSQL `user_variables` table, storing the mappings inside the `variables` JSONB column.
- **When** a Member on the same team loads a template referencing `{team_coding_standards}`.
- **Then** the Variable Canvas queries `GET /api/v1/users/me/variables` on load.
- **And** pre-populates the corresponding variable pill with the Team Lead's configuration automatically.

## Technical Implementation Details
- **Frontend Layer**:
  - Settings page workspace for Team Leads containing key-value input forms.
  - Variable Canvas integration: On template load, make a `GET /api/v1/users/me/variables` request. Check if any placeholders match keys in the returned variable mappings, and pre-populate the inputs.
- **Backend API Layer**:
  - Endpoints kebab-cased under `/api/v1`:
    - `GET /api/v1/users/me/variables` - Retrieve user/team variable settings.
    - `PUT /api/v1/users/me/variables` - Store updated variable settings.
  - Uses `@Transactional` annotations on write operation methods.
- **Database Layer**:
  - `user_variables` table schema:
    - `user_id` (UUID, Foreign Key referencing `users.id` and Primary Key)
    - `variables` (JSONB) - Key-value pair configuration mappings (e.g. `{"team_coding_standards": "Use Java 17 and Spring Boot MVC pattern"}`).
  - Uses PostgreSQL JSONB format to avoid Entity-Attribute-Value (EAV) bloat as defined in the project invariants in [how2prompt-agentic/CLAUDE.md](how2prompt-agentic/CLAUDE.md).

## Verification & Testing
- Authenticate as Team Lead, go to settings, write key-value variables, and click save. Verify data is saved correctly in the `user_variables` table under `variables` JSONB column.
- Authenticate as a team member, load a template that uses a matching variable name (e.g. `{team_coding_standards}`). Verify that the field gets populated automatically with the configured value.
- Refer to [how2prompt-agentic/agent/BA.md](how2prompt-agentic/agent/BA.md), [how2prompt-agentic/docs/SRS.md](how2prompt-agentic/docs/SRS.md), and [how2prompt-agentic/docs/epics.md](how2prompt-agentic/docs/epics.md) for full system specifications.
