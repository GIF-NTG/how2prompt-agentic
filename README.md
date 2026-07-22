# how2prompt-agentic

Stateless Prompt Optimization Agent Service. This service is a subsystem of the **how2prompt** platform, acting as the agentic prompt analysis and variables parser backend.

## Getting Started

Refer to the following files for instructions:
- **`CLAUDE.md`**: Run, build, lint, type check, format, and test commands, along with architectural coding style guidelines.
- **`.cursorrules`**: Explicit directions for AI agents working in this repository.
- **`docs/`**: System and API documentation.
  - `docs/architecture.md`: In-depth description of the system components and integration flows.
  - `docs/database.md`: Relational and JSONB databases design schemas.
  - `docs/api-specs.md`: Detailed endpoint requests, response schemas, and errors specifications.
  - `docs/development-workflow.md`: Local deployment setup guide.

## Requirements
- Python ^3.11
- Poetry ^1.8

## Git Submodule Integration

This repository is designed to be integrated as a Git submodule inside the main parent repository (e.g. `how2prompt` workspace).

### Adding this repository as a submodule
To add this project to your parent repository:
```bash
git submodule add https://github.com/GIF-NTG/how2prompt-agentic.git how2prompt-agentic
```

### Cloning a repository that already contains this submodule
If you are cloning a parent repository that incorporates this project, run:
```bash
git clone --recursive <parent-repository-url>
```

### Initializing the submodule in an existing clone
If the parent repository was already cloned without submodules, run the following from the parent root:
```bash
git submodule update --init --recursive
```

### Updating the submodule to the latest commit
To pull the latest updates for this subsystem within the parent project:
```bash
git submodule update --remote --merge
```

