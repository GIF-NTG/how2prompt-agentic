# CLAUDE.md — how2prompt-agentic

This repo is shared Spec-Kit tooling (skills/commands/scripts/templates), submoduled
into how2prompt's service repositories via `scripts/sync.sh` — see `README.md` for the
integration pattern. Only `.claude/skills`, `.cursor/skills`, `.opencode/commands`,
`.specify/scripts`, `.specify/templates` (top-level), and `.specify/workflows` are the
shared surface synced into other repos; everything else under `.specify/` (`agents/`,
`memory/`, `specs/`, `templates/overrides/`, the `*.json` state files) plus `docs/` is
this repo's own local example/governance content and must not be assumed present in a
consuming project.

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

## This Repo's Own Governance (local-only, not synced)
This repo dogfoods Spec-Kit for itself. Its own architecture decisions must respect
`.specify/memory/constitution.md` (Python/Postgres/LiteLLM stack invariants for the
how2prompt-mvp example service) — that constitution applies to this repo's own example
content only, not to projects that submodule this repo.
