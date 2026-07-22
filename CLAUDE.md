# CLAUDE.md — how2prompt-agentic

## Spec-Driven Development (SDD) Workflow
This project uses GitHub's **Spec-Kit** to manage software requirements, technical planning, and task execution. All development must follow the Spec-Driven Development cycle.

### Core Commands (Spec-Kit CLI)
- Check CLI status: `specify self check`
- Upgrade CLI: `specify self upgrade`
- Execute SDD commands via your coding agent:
  - Create constitution: `/speckit.constitution [prompt]`
  - Define feature spec: `/speckit.specify [prompt]`
  - Create tech plan: `/speckit.plan [prompt]`
  - Generate tasks: `/speckit.tasks`
  - Implement task: `/speckit.implement`
  - Sync with issues: `/speckit.taskstoissues`
  - Verify gaps: `/speckit.converge`

## Project Structure & Invariants
All architecture decisions must respect the Project Constitution (`.specify/memory/constitution.md`):
- **Statelessness:** The Python optimizer service must have no databases, local caches, or disk state.
- **Data Contracts:** All interfaces must use rigid Pydantic models. Dynamic dictionary parsing on main routes is prohibited.
- **Storage:** PostgreSQL is used for persistence. Active variables and execution snapshots must be stored in PostgreSQL `JSONB` columns to prevent EAV bloat.
- **LLM Engine:** Use LiteLLM and Pydantic. Do not use LangChain or LangGraph. Enforce exponential backoff retries (maximum 3) and map terminal exceptions to RFC-7807 Bad Gateway error details.
