# How2Prompt Project Constitution

## Core Principles

### I. Keyboard-First Workspace
Every feature, interface panel, and command workflow must be optimized for keybind-only execution. Mouse actions are secondary. Loading templates and copying compiled prompts to the clipboard must be achievable in less than 3 seconds.

### II. Decoupled Service Architecture
The codebase must enforce strict component isolation:
- **React Frontend SPA:** Pure UI layout and interaction states.
- **Java Spring Boot Gateway:** JWT session verification, PostgreSQL transactions, template CRUD, and history logging.
- **Python FastAPI Service:** A completely stateless assistant dedicated solely to executing LiteLLM prompts and returning structured JSON.

### III. PostgreSQL JSONB Dynamic Variables
To avoid Entity-Attribute-Value (EAV) database complexity, all dynamic user variables mapping and prompt copy history snapshots must be persisted in PostgreSQL `JSONB` database columns.

### IV. Stateless prompt optimizer
The Python service MUST NOT establish database connections or write local file caches. All variable scopes and guidelines must be supplied dynamically in the HTTP POST request payload.

### V. Resilient LLM Calls
External LLM calls must be wrapped with exponential backoff retries (maximum 3 attempts). Terminal failures must map to RFC-7807 Bad Gateway error details containing `LLM_PROVIDER_ERROR` codes.

## System Constraints & Technology Stack
- **Frontend:** React 18+, Tailwind CSS 3+, Context API.
- **Backend:** Java 17+, Spring Boot 3+, Spring Security (JWT).
- **Database:** PostgreSQL 15+.
- **Agent Service:** Python 3.11+, FastAPI 0.110+, LiteLLM 1.30+, Pydantic 2.6+.

## Governance
- This constitution governs all code additions.
- AI agents must run conformance checks against these guidelines before writing or editing.
