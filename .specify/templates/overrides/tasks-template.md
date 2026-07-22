# Task List: [FEATURE NAME]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [specs/how2prompt-mvp/spec.md](spec.md) | **Plan**: [specs/how2prompt-mvp/plan.md](plan.md)

---

## Development Phases

### Phase 1: Database & Backend Gateway (Spring Boot)
- **[ ] TSK-001: DB Migration**: Setup SQL script to modify schema (using JSONB for dynamic attributes).
- **[ ] TSK-002: Spring Boot REST Endpoint**: Create REST API endpoints with Spring Security and JWT validation.
- **[ ] TSK-003: Integration Test**: Create JUnit integration tests mock-calling endpoints.

### Phase 2: Agentic Prompt Service (Python FastAPI)
- **[ ] TSK-004: FastAPI Schemas**: Create Pydantic input and output request/response models.
- **[ ] TSK-005: LiteLLM Client**: Implement LiteLLM wrapper with Tenacity exponential retry logic.
- **[ ] TSK-006: Service Router**: Create FastAPI router delegating endpoints and raising RFC-7807 exceptions.
- **[ ] TSK-007: Pytest Unit Tests**: Create unit tests mocking LLM response states.

### Phase 3: Keyboard-First Interface (React Frontend)
- **[ ] TSK-008: React View Components**: Create canvas, inline variable pills, or drawer components.
- **[ ] TSK-009: Keyboard Navigation**: Implement Tab and keyboard listeners for quick navigation.
- **[ ] TSK-010: Integration API Client**: Setup Context API actions to invoke backend endpoints.

### Phase 4: Verification & E2E Validation
- **[ ] TSK-011: Docker Integration**: Spin up local containers and check log outputs.
- **[ ] TSK-012: E2E Playwright Tests**: Run E2E scripts to verify core UJ journeys.
