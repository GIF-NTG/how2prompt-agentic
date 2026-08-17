# GitHub Copilot Instructions — how2prompt-agentic

You are an AI coding assistant working on a how2prompt service repository. This
repository enforces Spec-Driven Development (SDD) via GitHub's **Spec-Kit**, plus a
shared Claude Code harness (`.claude/agents/`, `.claude/rules/`) for coding, testing,
and security standards.

## Spec-Driven Development Rules

- **Do not write code before planning.** Only write code mapped to a task in this
  project's own `.specify/specs/<feature>/tasks.md`, supported by that feature's
  `plan.md`. If neither exists yet, run `/speckit.specify` and `/speckit.plan` first.
- **Core specification is the source of truth.** Don't introduce functionality not
  defined in `.specify/specs/<feature>/spec.md`.
- **Project constitution governs every change.** Once this project has run
  `/speckit.constitution`, verify changes conform to `.specify/memory/constitution.md`.
- **Workflow:** read `spec.md` → read `plan.md` → implement `tasks.md` sequentially →
  write automated tests for each task (see `.claude/rules/common/testing.md`).

## Coding standards

Read the relevant rule file from `.claude/rules/` just-in-time (not all at once):
`common/coding-style.md`, `common/testing.md`, `common/security.md`,
`common/code-review.md`, plus the stack-specific guide (`python/`, `java/`, or
`typescript/guidelines.md`) for whichever service you're editing.
