# Task List: how2prompt-mvp

**Branch**: `how2prompt-mvp` | **Date**: 2026-07-22 | **Spec**: [./spec.md](./spec.md) | **Plan**: [./plan.md](./plan.md)

This task list breaks down the MVP development into modular, testable tasks. It guides AI agents or developers through step-by-step implementation.

---

## Phase 0: Infrastructure & Project Scaffolding

### [ ] TSK-001: Initialize Directory Hierarchy
- **Description:** Scaffold directories for `frontend`, `backend`, and `agent-service` at the workspace root.
- **Verification:** Run `tree` or list directories to verify clean separation.

### [ ] TSK-002: Docker Compose Orchestration Setup
- **Description:** Create the main `docker-compose.yml` to define services for PostgreSQL, Spring Boot gateway, React client, and Python prompt service.
- **Verification:** Run `docker-compose config` to ensure YAML validation passes.

### [ ] TSK-003: PostgreSQL Database Initialization
- **Description:** Setup base SQL migrations to create `teams`, `users`, `templates`, `user_variables` (containing JSONB variables), and `history` (containing JSONB variable_snapshot) tables.
- **Verification:** Start DB container, run test queries, and verify JSONB columns are correctly initialized.

---

## Phase 1: Spring Boot API Gateway

### [ ] TSK-004: JWT Security & Authentication
- **Description:** Enforce Spring Security with stateless JWT validation. Create login route returning signature token.
- **Verification:** POST to `/api/v1/auth/login` and verify signature and contents of returned JWT token.

### [ ] TSK-005: Templates CRUD API
- **Description:** Implement GET and POST routes for prompt templates. Ensure sharing templates is bounded to the user's `team_id`.
- **Verification:** Authenticate user, GET `/api/v1/templates`, and assert templates from the same team are returned.

### [ ] TSK-006: User Variables Endpoint (JSONB mapping)
- **Description:** Implement GET and PUT routes for `/api/v1/users/me/variables` to store dynamic personal global parameters.
- **Verification:** PUT values to endpoint and verify PostgreSQL writes correct JSON object inside JSONB column.

### [ ] TSK-007: History Drawer Persistence
- **Description:** Implement GET and POST routes for `/api/v1/history` to log prompt execution state snapshot and retrieve up to 20 past snapshots.
- **Verification:** POST a snapshot of variable states, check PostgreSQL, and verify history list only returns the last 20 records.

---

## Phase 2: Python Prompt Optimizer Service

### [ ] TSK-008: FastAPI App & Pydantic Config
- **Description:** Initialize FastAPI app, Pydantic settings loading from environment, and global RFC-7807 handler.
- **Verification:** Call GET `/health` and verify `{"status": "healthy"}`. Verify HTTP validation errors return RFC-7807 error envelopes.

### [ ] TSK-009: LiteLLM Client with Exponential Retry
- **Description:** Create `LLMClient` class using LiteLLM for LLM queries. Wrap completion in a Tenacity decorator with exponential backoff up to 3 attempts.
- **Verification:** Mock LLM timeout error on first two calls and verify completion succeeds on the third. Verify terminal failures return RFC-7807 HTTP 502 error detail with `LLM_PROVIDER_ERROR` code.

### [ ] TSK-010: Prompt Optimizer Core Service
- **Description:** Create `PromptOptimizerService` implementing prompt optimization templates formatting and structured output schema checks.
- **Verification:** Call `optimizer.optimize()` and verify it returns an `OptimizeResponse` Pydantic model with correct variables array and template string.

### [ ] TSK-011: API router `/api/v1/agent/optimize`
- **Description:** Create POST controller endpoint mapped to `OptimizeRequest` schema and delegates to optimizer service.
- **Verification:** Run unit tests calling the endpoint using FastAPI `TestClient` verifying correct JSON return output.

---

## Phase 3: React Keyboard-First Frontend

### [ ] TSK-012: Dashboard Layout & Context API State
- **Description:** Create UI workspace. Instantiate Context API state management for active template, active variables, and history logs.
- **Verification:** Verify state modifications trigger re-renders on components correctly.

### [ ] TSK-013: Command Palette Search (Ctrl+K)
- **Description:** Create Command Palette UI triggered by `Ctrl+K`. Implement fuzzy search to select and load templates.
- **Verification:** Press `Ctrl+K`, type text, and verify matches are listed and pressing `Enter` loads the template on canvas in under 50ms.

### [ ] TSK-014: Variable Canvas & Inline Pills
- **Description:** Render template text with inline Variable Pills. Support tabbing navigation through editable pills.
- **Verification:** Load template, press `Tab` repeatedly, and confirm focus moves through all Variable Pills in sequence.

### [ ] TSK-015: Prompt Compile & Clipboard Copy (Ctrl+Enter)
- **Description:** Implement prompt compiler replacing pills with user input, cleaning whitespaces, and copying to clipboard.
- **Verification:** Press `Ctrl+Enter` and verify compiled prompt resides in clipboard and toast message notification displays.

### [ ] TSK-016: Quick-History Drawer
- **Description:** Implement Drawer listing past 20 copied prompts. Clicking a log reloads the snapshot on the canvas.
- **Verification:** Copy prompts, open drawer, check log cards, click one, and verify canvas variable values are restored.

---

## Phase 4: Integration & E2E Testing

### [ ] TSK-017: Full-Flow Gateway Mock Integration
- **Description:** Configure Spring Boot client to invoke Python Service optimize routes on prompt optimization triggers.
- **Verification:** Integration tests verifying successful payload exchange between Spring Boot and Mock Python FastAPI container.

### [ ] TSK-018: End-to-End User Journey Tests
- **Description:** Write integration/E2E test validating login, template search, canvas edit, copy compiled prompt, and history logging.
- **Verification:** Run test scripts and verify all 5 core epics pass successfully.
