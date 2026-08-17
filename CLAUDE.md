# CLAUDE.md — how2prompt-agentic

This repo is shared agentic tooling for the how2prompt team — Spec-Kit SDD workflow
(skills/commands/scripts/templates) **and** a Claude Code harness (agents/rules/skills/
commands under `.claude/`) — submoduled into how2prompt's service repositories via
`scripts/sync.sh`. See `README.md` for the full integration pattern.

**Synced surface** (copied into consuming repos by `sync.sh`): `.claude/agents/`,
`.claude/skills/`, `.claude/rules/`, `.claude/commands/`, `.cursor/skills/`,
`.opencode/commands/`, `.specify/scripts`, `.specify/templates` (top-level only), and
`.specify/workflows`.

**Local-only** (never synced — specific to this repo's own governance, or machine-local):
`.claude/settings*.json`, `.claude/hooks/`, `.specify/agents/`, `.specify/memory/`,
`.specify/specs/`, `.specify/templates/overrides/`, the `.specify/*.json` state files.
A consuming repo builds its own `.specify/memory/constitution.md` and `.specify/specs/`
via `/speckit.constitution` and `/speckit.specify`, run locally in that repo.

## Rules — read just-in-time (not auto-loaded)

`.claude/rules/` is reference material, not something to load wholesale into every
conversation — that burns context budget for nothing. Read a rule file only when the
task at hand actually needs it:

- `common/coding-style.md`, `common/testing.md`, `common/security.md`,
  `common/code-review.md`, `common/git-workflow.md`, `common/agents.md` — apply to any
  stack.
- `java/guidelines.md`, `typescript/guidelines.md` — apply when working in that
  language (`how2prompt-api` = Java/Spring Boot, `how2prompt-ui` = React/TS). Add a
  `python/` folder later only if/when a Python service actually joins the stack.
- `common/agent-first-workflow.md`, `common/security-gate-policy.md`,
  `common/test-coverage-standards.md`, `common/ai-attribution-log.md`,
  `common/prompt-library-standards.md` — L2C ("Agent-First") certification process
  docs; read when doing agent-attribution or coverage-evidence work.

## Agents (`.claude/agents/`)

`planner`, `tdd-guide`, `code-reviewer`, `security-reviewer` — see
`.claude/rules/common/agents.md` for when to invoke each. This is a deliberately small
starting set; add per-stack reviewers as the need actually shows up rather than
front-loading them.

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
This repo can dogfood Spec-Kit for itself once real project work starts here — run
`/speckit.constitution` and `/speckit.specify` locally to create this repo's own
`.specify/memory/constitution.md` and `.specify/specs/`. That content, once created,
applies to this repo's own example/tracking use only — never to projects that
submodule this repo (each of those defines its own constitution locally, per the
"Local-only" list above).
