# Development Workflow & Environments — how2prompt

Follow this guide to spin up the local development workspace, build containers, run test commands, and manage environment variables.

## 1. Prerequisites
Ensure you have the following installed locally:
- Docker and Docker Compose
- Python 3.11+
- Poetry ^1.8
- Java JDK 17 (if running Spring Boot locally outside Docker)

---

## 2. Local Environment Setup

### Environment Variables (.env)
Copy the example environment settings to initialize your configuration:
```bash
cp .env.example .env
```
Open `.env` and fill in the required API keys (e.g. `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`).

### Poetry Shell (Python Service)
Navigate to `how2prompt-agentic` and run Poetry commands:
```bash
# Install packages
poetry install

# Spin up virtualenv
poetry shell
```

---

## 3. Running the Stack

The simplest way to run the entire stack (React, Spring Boot, Postgres, Python Service) is via Docker Compose at the root of the workspace.

### Running with Docker Compose
To build and start all containers:
```bash
docker-compose up --build
```

To run only the Python Agentic service locally in hot-reload mode:
```bash
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 4. Verification & Testing

### Running Linters and formatters
Always format and check type annotations before submitting a Pull Request:
```bash
# Code Formatting
poetry run black .

# Linting
poetry run ruff check .

# Static Type Checking
poetry run mypy app/
```

### Running Automated Tests
Tests are located in the `tests/` directory and use `pytest`.

```bash
# Run all tests
poetry run pytest

# Run tests with code coverage report
poetry run pytest --cov=app tests/
```

### Pull Request & CI Checks
The continuous integration pipelines enforce that:
1. `black` returns exit code 0 (no formatting changes needed).
2. `ruff` returns 0 warnings/errors.
3. `mypy` static analyzer validates type safety.
4. `pytest` unit/integration tests run successfully with at least 80% coverage on core files.
5. All endpoint inputs/outputs match strict Pydantic definitions.
