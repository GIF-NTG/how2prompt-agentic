# how2prompt-agentic

Shared Spec-Kit configuration for the how2prompt team — the **Spec-Driven Development
(SDD)** tooling (Claude Code / Cursor / OpenCode skills & commands, CLI scripts,
templates, workflows) that every service repository (React `frontend/`, Spring Boot
`backend/`, Python `agent/`, ...) starts from. Kept in one repo so updates propagate to
every service instead of being copy-pasted and drifting out of sync.

This repo itself also dogfoods Spec-Kit for its own governance (see
`.specify/specs/how2prompt-mvp/`, `.specify/memory/constitution.md`, `docs/`) — that
content is this repo's own example/tracking data, **not** part of the shared surface
synced into other services (see below).

---

## Quick Start

For a service repo (`frontend/`, `backend/`, `agent/`, ...) that doesn't have this
tooling yet:

```bash
# 1. Install the Spec-Kit CLI (once per machine)
uv tool install specify-cli   # or: pipx install specify-cli
specify version               # sanity check

# 2. From the root of your service repo, add this repo as a submodule
git submodule add <repository-url> how2prompt-agentic

# 3. Copy the shared skills/commands/templates into your service repo
bash how2prompt-agentic/scripts/sync.sh

# 4. Create your service's own constitution and first feature spec
#    (run inside your AI assistant, e.g. Claude Code / Cursor / OpenCode)
/speckit.constitution
/speckit.specify "describe the feature"
```

If you're cloning a service repo that **already** has this submodule:

```bash
git submodule update --init --recursive   # pull the submodule's content
bash how2prompt-agentic/scripts/sync.sh   # re-sync into your local .claude/.cursor/.opencode/.specify
```

To pick up updates published to this repo later:

```bash
git submodule update --remote --merge how2prompt-agentic
bash how2prompt-agentic/scripts/sync.sh
git add .claude .cursor .opencode .specify how2prompt-agentic
git commit -m "chore: update how2prompt-agentic shared tooling"
```

See section 1 below for the full rationale (why copy instead of symlink), section 3 for
the full slash-command reference, and section 4 for what's synced vs. local-only.

The submodule + sync mechanism is identical for every service, regardless of stack —
only the constitution/spec content you write in step 4 differs, since it should reflect
that service's own architecture (React vs. Spring Boot vs. Python, etc.).

### Example: integrating into `how2prompt-ui` (frontend)

```bash
# From the root of how2prompt-ui (where package.json lives):

# 1. Install the Spec-Kit CLI (once per machine)
uv tool install specify-cli   # or: pipx install specify-cli
specify version

# 2. Add this repo as a submodule
git submodule add https://github.com/GIF-NTG/how2prompt-agentic.git how2prompt-agentic

# 3. Sync the shared skills/commands/templates into how2prompt-ui
bash how2prompt-agentic/scripts/sync.sh

# 4. Inside your AI assistant, create how2prompt-ui's OWN constitution and spec
#    (this writes to how2prompt-ui's .specify/memory and .specify/specs, never
#    into the how2prompt-agentic submodule itself)
#    /speckit.constitution
#    /speckit.specify "describe the frontend feature"

# 5. Commit the submodule pointer and the synced (generated, non-symlinked) files
git add .gitmodules how2prompt-agentic .claude .cursor .opencode .specify
git commit -m "chore: integrate how2prompt-agentic shared Spec-Kit tooling"
```

### Example: integrating into `how2prompt-api` (backend)

```bash
# From the root of how2prompt-api (where pom.xml lives):

# 1. Install the Spec-Kit CLI (once per machine)
uv tool install specify-cli   # or: pipx install specify-cli
specify version

# 2. Add this repo as a submodule
git submodule add https://github.com/GIF-NTG/how2prompt-agentic.git how2prompt-agentic

# 3. Sync the shared skills/commands/templates into how2prompt-api
bash how2prompt-agentic/scripts/sync.sh

# 4. Inside your AI assistant, create how2prompt-api's OWN constitution and spec
#    (writes to how2prompt-api's .specify/memory and .specify/specs, reflecting its
#    own Java/Spring Boot architecture — never into the how2prompt-agentic submodule)
#    /speckit.constitution
#    /speckit.specify "describe the backend feature"

# 5. Commit the submodule pointer and the synced (generated, non-symlinked) files
git add .gitmodules how2prompt-agentic .claude .cursor .opencode .specify
git commit -m "chore: integrate how2prompt-agentic shared Spec-Kit tooling"
```

Later, to pick up updates published to `how2prompt-agentic` (same for either repo):
```bash
git submodule update --remote --merge how2prompt-agentic
bash how2prompt-agentic/scripts/sync.sh
git add how2prompt-agentic .claude .cursor .opencode .specify
git commit -m "chore: update how2prompt-agentic shared tooling"
```

---

## 1. Git Submodule Integration

This repository is designed to be integrated as a Git submodule inside the **root
directory of a specific service/component repository** (such as your React `frontend/`
repository or Spring Boot `backend/` repository).

Integrating it this way enables your AI coding assistant (Claude Code, Cursor, OpenCode)
to access Spec-Kit specifications and commands directly from the workspace root of that
specific service.

### Add this Submodule to your Service Repository
To add this project inside your frontend/backend repository root:
```bash
# From the root of your frontend or backend repository:
git submodule add <repository-url> how2prompt-agentic
```

### Initialize and Update Submodules
If the repository was already cloned without submodules, initialize and update them by running:
```bash
git submodule update --init --recursive
```

### Update the Submodule to the Latest Commit
To pull the latest updates for this subsystem within your project:
```bash
git submodule update --remote --merge
```

### Sync Spec-Kit Tooling to the Repository Root (Post-Clone Setup)
Once you have cloned the submodule inside your service repository (e.g. `backend/` or
`frontend/`), run the sync script **from the root of your service repository**:

```bash
# Run this from the root of your frontend or backend repository
bash how2prompt-agentic/scripts/sync.sh
```

This script **copies** (never symlinks) the generic, cross-project tooling into your
own service repo:
- Spec-Kit integration skills into `.claude/skills/` (for Claude Code).
- Spec-Kit integration skills into `.cursor/skills/` (for Cursor).
- Spec-Kit integration commands into `.opencode/commands/` (for OpenCode).
- The Spec-Kit CLI scripts, base templates, and workflows into `.specify/`.

It deliberately does **not** touch `.specify/agents`, `.specify/memory`,
`.specify/specs`, or `.specify/templates/overrides` — those hold project-specific
constitution/spec content. Symlinking or copying them would make every service that
submodules this repo share (and clobber) the same spec state. Run `specify init` or
`/speckit.constitution` / `/speckit.specify` **in your own service repo** to create your
own `.specify/memory/constitution.md` and `.specify/specs/`.

The copies under `.claude/skills/`, `.cursor/skills/`, `.opencode/commands/`, and
`.specify/{scripts,templates,workflows}/` are generated — don't hand-edit them. Edit the
source in `how2prompt-agentic/` and re-run `sync.sh`.

---

## 2. Spec-Kit Development Environment Setup

This project is pre-configured with Spec-Kit integrations for popular AI Coding Assistants: **Claude Code**, **Cursor**, and **OpenCode**.

### Install Spec-Kit CLI (`specify`)
To run specifications and development automation workflows, you need to install the `specify-cli`. The recommended installation is via `uv` (a fast Python package manager) or `pipx`:

```bash
# Install using uv (recommended)
uv tool install specify-cli

# Or install using pipx
pipx install specify-cli
```
*After installation, verify it by running `specify version`.*

### Installed Integrations in this Repository
The project integrates and generates commands/skills for 3 AI assistants:
1. **Claude Code:** Integration skills are installed under `.claude/skills/`.
2. **Cursor:** Integration skills are installed under `.cursor/skills/`.
3. **OpenCode:** Markdown integration commands are installed under `.opencode/commands/`.

*Note: The global Spec-Kit state configuration file is located at `.specify/integration.json`.*

---

## 3. SDD Slash Commands Table

When working inside AI coding assistants supporting Spec-Kit (Claude Code, Cursor, OpenCode), you can call these slash commands directly to automate tasks.

*   For **Claude Code** and **Cursor** (use hyphen `-`): e.g., `/speckit-specify`
*   For **OpenCode** (use dot `.`): e.g., `/speckit.specify`

| Slash Command (OpenCode) | Slash Command (Claude/Cursor) | Description |
| :--- | :--- | :--- |
| `/speckit.constitution` | `/speckit-constitution` | Initialize or update the shared project constitution. |
| `/speckit.specify` | `/speckit-specify` | Create or update the feature specification (`spec.md`) from user description. |
| `/speckit.clarify` | `/speckit-clarify` | Ask up to 5 targeted questions to de-risk ambiguous areas in the spec (run before planning). |
| `/speckit.plan` | `/speckit-plan` | Translate `spec.md` into the technical implementation plan (`plan.md`). |
| `/speckit.checklist` | `/speckit-checklist` | Generate quality/NFR checklists based on the technical plan. |
| `/speckit.tasks` | `/speckit-tasks` | Generate dependency-ordered tasks (`tasks.md`) based on the spec and plan. |
| `/speckit.taskstoissues` | `/speckit-taskstoissues` | Sync tasks into actionable, dependency-ordered GitHub issues. |
| `/speckit.implement` | `/speckit-implement` | Automate the sequential implementation of tasks defined in `tasks.md`. |
| `/speckit.analyze` | `/speckit-analyze` | Run cross-artifact consistency and quality analysis across spec, plan, and tasks. |
| `/speckit.converge` | `/speckit-converge` | Compare codebase to spec/plan and generate tasks for any remaining gaps. |

---

## 4. Spec-Kit Directory Structure

Spec-Kit specifications and configuration files are organized inside the hidden `.specify/` folder to keep the workspace root clean:

```text
how2prompt-agentic/
├── .claude/skills/            # [synced] Integration skills for Claude Code
├── .cursor/skills/            # [synced] Integration skills for Cursor
├── .opencode/commands/        # [synced] Markdown integration commands for OpenCode
├── scripts/
│   └── sync.sh                # Copies the [synced] items above into a consuming repo
├── .specify/
│   ├── scripts/                # [synced] Spec-Kit CLI helper scripts
│   ├── templates/               # [synced, top-level only] base spec/plan/tasks templates
│   │   └── overrides/           # [local-only] this repo's own customized templates
│   ├── workflows/                # [synced] workflow definitions
│   ├── integration.json         # [local-only] installed-integrations state for this repo
│   ├── init-options.json        # [local-only] `specify init` parameters used for this repo
│   ├── agents/                   # [local-only] this repo's own agent role docs
│   ├── memory/
│   │   └── constitution.md      # [local-only] this repo's own governing constitution
│   └── specs/
│       └── how2prompt-mvp/      # [local-only] this repo's own example feature spec
```

`[synced]` = copied into other repos by `scripts/sync.sh`. `[local-only]` = specific to
this repo's own use of Spec-Kit; never copied elsewhere.

---
*Developed by Spec Kit & How2Prompt Team.*
