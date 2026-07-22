# GitHub Copilot Instructions — how2prompt-agentic

You are an AI coding assistant working on the how2prompt project. This repository enforces Spec-Driven Development (SDD) via GitHub's **Spec-Kit**.

## Spec-Driven Development Rules
- **Do not write code before planning:** You must only write code that is mapped to a task in `.specify/specs/how2prompt-mvp/tasks.md` and supported by `.specify/specs/how2prompt-mvp/plan.md`.
- **Core Specification:** The source of truth for the features is `.specify/specs/how2prompt-mvp/spec.md`. Do not introduce functionality not defined in the specification.
- **Project Constitution:** The governing architectural principles are defined in `.specify/memory/constitution.md`. You must verify that every code change conforms to these principles.
- **Workflow Steps:**
  1. Read `.specify/specs/how2prompt-mvp/spec.md` to understand requirements.
  2. Read `.specify/specs/how2prompt-mvp/plan.md` to understand tech stack and constraints.
  3. Consult `.specify/specs/how2prompt-mvp/tasks.md` and implement the tasks sequentially.
  4. Write automated tests for each implemented task.

## Key Platform Constraints (from Constitution)
- **Stateless Python Service:** The Python Prompt Service must remain 100% stateless. Do not add database connections or persistent state. All parameters must come via the request body.
- **FastAPI / Pydantic Contracts:** Request and response schemas must be strictly defined with Pydantic. Do not use raw dictionary inputs.
- **LiteLLM Wrapper:** Use LiteLLM for LLM connections. Do not install LangChain or LangGraph.
- **Retry & Error Standards:** Implement tenacity backoff retries for LLM calls (up to 3 times). Catch failures and format error responses as RFC-7807 problem details (HTTP 502 with `LLM_PROVIDER_ERROR` code).
- **Postgres JSONB:** The database uses JSONB columns to persist active variables and history logs.
