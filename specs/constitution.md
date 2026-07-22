# How2Prompt Constitution

*Note: This is a copy of the official project constitution. The primary source is managed at `.specify/memory/constitution.md`.*

## Core Principles

### I. Keyboard-First Design
Every user interaction must be optimized for keybind-driven execution. Mouse actions are fallback-only. Canvas modifications, template loading, and copy actions must complete within a 3-second user journey.

### II. Decoupled Service Architecture
The platform is strictly divided into three isolated layers:
- **Frontend (React SPA):** Renders UI and handles user interaction state.
- **Gateway (Spring Boot):** Handles JWT security validation, template persistence, and logs.
- **Prompt Service (FastAPI):** A stateless python service dedicated to executing LLM optimization logic. No service may bypass its direct downstream layer.

### III. Dynamic Variables (JSONB)
To prevent database structure bloat (EAV), user variables and execution snapshots must be stored in PostgreSQL JSONB fields. They must remain flexible, key-value mapped, and indexable.

### IV. Strict Statelessness
The Python Prompt Service must contain no database connections or disk states. All user state and guidelines must be passed dynamically in the HTTP POST request payload.

### V. Resilient LLM Execution
All external AI model requests must execute with exponential backoff retry mechanisms (maximum 3 retries) to manage transient failures. Terminal exceptions must bubble up as standard RFC-7807 payloads with HTTP status 502 and `error_code: LLM_PROVIDER_ERROR`.

## System Constraints & Technology Stack

### Tech Stack Standards
- **Frontend:** React 18+, Tailwind CSS 3+, Context API (no Redux).
- **Backend Gateway:** Java 17+, Spring Boot 3+, Spring Security, JWT tokens.
- **Database:** PostgreSQL 15+, JSONB indexing.
- **Agent Service:** Python 3.11+, Poetry, FastAPI 0.110+, LiteLLM 1.30+, Pydantic 2.6+.

### Design Invariants
- API exchange must follow strict JSON contracts.
- Endpoints must use kebab-case (`/api/v1/agent/optimize`).
- All error details must match the RFC-7807 standard.
- Hardcoding API keys or secret credentials in code is strictly prohibited. All settings must resolve from environment variables.

## Spec-Driven Development Workflow

The project strictly follows the GitHub Spec-Kit Spec-Driven Development process:

1. **Specify (`spec.md`):** Write user stories with acceptance scenarios and functional requirements before design.
2. **Clarify (`clarify.md`):** Resolve unclear parameters or missing scopes.
3. **Plan (`plan.md`):** Establish technical implementation paths, components structure, and constraints.
4. **Tasks (`tasks.md`):** Generate a checklist of modular, testable tasks.
5. **Implement:** Execute code changes step-by-step guided by the task list.
6. **Converge:** Compare code to spec/plan and resolve remaining gaps.

## Governance
- This constitution is the source of truth for the project guidelines.
- Any pull request or AI agent compilation must verify compliance against these rules.
- Changes to the core stack require a formal amendment to this constitution.

**Version**: 1.0.0 | **Ratified**: 2026-07-22 | **Last Amended**: 2026-07-22
