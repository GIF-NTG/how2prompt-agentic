# how2prompt-agentic

This is the Stateless Prompt Optimization Agent Service, acting as the prompt analysis and variables parser backend for the **how2prompt** platform. This project applies the **Spec-Driven Development (SDD)** workflow managed via GitHub's **Spec-Kit**.

---

## 1. Git Submodule Integration

This repository is designed to be integrated as a Git submodule or subdirectory inside the **root directory of a specific service/component repository** (such as your React `frontend/` repository or Spring Boot `backend/` repository). 

Integrating it this way enables your AI coding assistant (Claude Code, Cursor, OpenCode) to access Spec-Kit specifications and commands directly from the workspace root of that specific service.

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

### Link Spec-Kit to the Repository Root (Post-Clone Setup)
Once you have cloned the submodule parallel to or inside your service repository (e.g. `how2prompt-api/` or `how2prompt-ui/`), you must open your terminal **at the root of your service repository** and run the setup script using its relative path to enable the Spec-Kit commands/skills in your editor instantly:

```bash
# Open terminal at your service repository root (e.g. how2prompt-api/ or how2prompt-ui/)
cd /path/to/your/service-repo

# If how2prompt-agentic is parallel to your service repository:
bash ../how2prompt-agentic/setup.sh

# If how2prompt-agentic is inside your service repository:
bash how2prompt-agentic/setup.sh
```

This script dynamically resolves the absolute path of the submodule and will automatically:
- Symlink the `.specify/` configuration and feature specs directory to the repository root.
- Symlink all Spec-Kit integration skills to `.claude/skills/` (for Claude Code).
- Symlink all Spec-Kit integration skills to `.cursor/skills/` (for Cursor).
- Symlink all Spec-Kit integration commands to `.opencode/commands/` (for OpenCode).

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
├── .claude/skills/            # Integration skills for Claude Code
├── .cursor/skills/            # Integration skills for Cursor
├── .opencode/commands/        # Markdown integration commands for OpenCode
├── .specify/
│   ├── integration.json       # Configured/installed integrations metadata
│   ├── init-options.json      # Initialization CLI parameters log
│   ├── memory/
│   │   └── constitution.md    # Project Constitution (architectural source of truth)
│   ├── templates/
│   │   └── overrides/         # Customized plan and tasks templates
│   └── specs/
│       └── how2prompt-mvp/    # Business spec, plan, and tasks for the MVP feature
│           ├── spec.md        # Feature requirements & acceptance criteria (Given-When-Then)
│           ├── plan.md        # Technical execution and architecture plan
│           └── tasks.md       # Checklist of modular implementation tasks
```

---

## 5. Multi-Root Workspace Configuration (Code Workspace)

To facilitate developing the parent project **how2prompt** and the **how2prompt-agentic** submodule concurrently, open the workspace file at the parent repository root:

*   **File Path:** `how2prompt.code-workspace`
*   This workspace groups both directories and configures file exclusions to hide hidden metadata folders.

---

## 6. Requirements (Local execution)
* Python ^3.11
* Poetry ^1.8

---
*Developed by Spec Kit & How2Prompt Team.*
