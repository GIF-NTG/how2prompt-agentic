# Implementation Plan: how2prompt-mvp

**Branch**: `how2prompt-mvp` | **Date**: 2026-07-22 | **Spec**: [specs/how2prompt-mvp/spec.md](spec.md)

**Input**: Feature specification from `specs/how2prompt-mvp/spec.md`

---

## Summary
Build the How2Prompt platform MVP using a decoupled layered design. A React SPA frontend provides the keyboard-first interface, a Java Spring Boot backend controls relational storage and JWT validation, a PostgreSQL database stores relational models and JSONB variables, and a stateless Python FastAPI service executes LLM-driven prompt optimizations using LiteLLM.

---

## Technical Context

- **Language/Version:** Java 17 (Spring Boot), JavaScript/TypeScript (React), Python 3.11+ (Agent Service).
- **Primary Dependencies:** Spring Security, React, Tailwind CSS, FastAPI, Pydantic, LiteLLM, Tenacity.
- **Storage:** PostgreSQL 15+ (relational schema and JSONB column index).
- **Testing:** JUnit & Mockito (Spring Boot), Pytest (Python service), Jest & React Testing Library (React).
- **Target Platform:** Docker / Docker Compose containerized environment.
- **Project Type:** Web Service Application (decoupled Frontend, Backend Gateway, and Agent Backend).
- **Performance Goals:** First Contentful Paint (FCP) < 200ms, Time To Interactive (TTI) < 500ms, Command Palette fuzzy search latency < 50ms.
- **Constraints:** Python prompt service must remain 100% stateless; user parameters must be supplied in request bodies. LLM integrations must carry transient error retries (exponential backoff, 3 retries max).

---

## Constitution Check

| Rule ID | Constitution Guideline | Status | Verification Path |
|---|---|---|---|
| C-1 | Keyboard-First Design | Passed | Frontend UI test verifying all canvas actions run using `Tab`, `Shift+Tab`, and `Ctrl+Enter`. |
| C-2 | Decoupled Service Architecture | Passed | Verify separate ports and containers for React SPA, Spring Boot, and FastAPI. |
| C-3 | Dynamic Variables (JSONB) | Passed | DB migration script uses JSONB type for `user_variables.variables` and `history.variable_snapshot`. |
| C-4 | Strict Python Statelessness | Passed | Review Python config; verify no DB drivers (e.g. psycopg2) or disk write operations are imported. |
| C-5 | Resilient LLM Execution | Passed | Wrap LiteLLM requests in Python service using a Tenacity retry decorator with exponential backoff. |

---

## Project Structure

### Documentation (this feature)
```text
specs/how2prompt-mvp/
├── spec.md              # Requirements and prioritized user stories
├── plan.md              # Technical implementation plan (this file)
└── tasks.md             # Actionable task list breaking down the MVP build
```

### Source Code
The codebase is structured as a decoupled multi-service project:

```text
how2prompt/
├── docker-compose.yml         # Container orchestration for all services
├── docs/                      # General specifications and PDFs
├── frontend/                  # React Single Page Application (UI Canvas)
│   ├── package.json
│   ├── src/
│   │   ├── components/        # VariableCanvas, CommandPalette, HistoryDrawer
│   │   ├── context/           # Context API state managers
│   │   └── services/          # REST Client invoking Spring Boot API
│   └── tests/
├── backend/                   # Java Spring Boot API Gateway
│   ├── pom.xml
│   ├── src/main/java/com/
│   │   ├── controllers/       # Templates, Authentication, Variables endpoints
│   │   ├── services/          # Core gateway business logic and REST Client to Python
│   │   └── models/            # Entity models (Users, Teams, History, Templates)
│   └── src/main/resources/    # Database migration scripts (Flyway/Liquibase)
└── agent-service/             # Stateless Python Prompt Optimizer Backend
    ├── pyproject.toml         # Poetry settings
    ├── app/
    │   ├── main.py            # FastAPI entry point
    │   ├── core/              # Config, Logging, Schemas
    │   ├── routers/           # /api/v1/agent/optimize endpoint
    │   ├── services/          # Prompts optimizer logic
    │   └── clients/           # LiteLLM resilience caller
    └── tests/
```

**Structure Decision:** Option 2 (Web application) is selected. It splits UI, security/persistence gateway, and prompt processing into standalone isolated components that communicate via REST APIs.

---

## Complexity Tracking

*No constitution violations were detected. Architecture constraints are strictly respected.*
