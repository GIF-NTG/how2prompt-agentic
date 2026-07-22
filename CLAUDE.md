# CLAUDE.md — how2prompt-agentic

## Build and Environment Administration
This service is built using Python 3.11+ and uses Poetry for package and environment management.

### Environment Setup
- Install dependencies: `poetry install`
- Activate virtual environment: `poetry shell`
- Create local settings file: `cp .env.example .env` (fill in required API keys)

### Running the Application
- Run development server (with hot reload): `poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload`
- Run production server: `poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4`

### Testing
- Run all tests: `poetry run pytest`
- Run a specific test: `poetry run pytest tests/test_routers/test_agent.py`
- Run tests with coverage: `poetry run pytest --cov=app tests/`

### Linting and Formatting
- Format code: `poetry run black .`
- Lint and fix code: `poetry run ruff check . --fix`
- Type checking: `poetry run mypy app/`

## Coding Style & Architecture Conventions

### Architectural Guidelines (Router-Service-Client)
- The architecture must follow strict downward dependencies: Routers -> Services -> Clients -> Core.
- Upward dependencies are prohibited (e.g. Services must never import Routers, Clients must never import Services).
- Core represents configurations, exceptions, utilities, and logging. It is importable by all layers.

### Code Style
- Follow PEP 8 guidelines.
- Use explicit type annotations for all function signatures and variables.
- Write docstrings for all modules, classes, and public functions.
- Class names must use PascalCase (e.g., `LLMClient`).
- Module, function, and variable names must use snake_case (e.g., `optimize_prompt`).
- Constants must be UPPERCASE (e.g., `MAX_RETRY_ATTEMPTS`).

### System Invariants
- **Statelessness:** The service must be completely stateless. Do not use local storage, databases, or local memory state. All state must be passed by the client (Spring Boot backend) as request payload parameters.
- **Strict Data Contracts:** All request and response payloads must use Pydantic models. Do not use dynamic dictionaries or JSON-any parsing for main routes.
- **Agent Framework Restrictions:** Use LiteLLM and Pydantic. Do not import heavyweight wrappers (LangChain, LangGraph).
- **Error Handling:** External calls must use exponential backoff retry. Terminal errors must be returned as HTTP 502 containing RFC-7807 compliant JSON body.
- **Secrets Management:** Use `pydantic-settings` to load configuration from environment variables. Do not commit keys to VCS.
