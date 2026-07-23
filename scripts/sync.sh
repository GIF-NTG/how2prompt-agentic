#!/bin/bash
# scripts/sync.sh
#
# Run from the root of your service repository (e.g. backend/ or frontend/),
# after adding this repo as a submodule:
#   git submodule add <repository-url> how2prompt-agentic
#
# Copies the generic, cross-project Spec-Kit tooling (skills, commands,
# scripts, templates) from the submodule into the consuming project's own
# .claude/, .cursor/, .opencode/ and .specify/ trees.
#
# Deliberately COPIES instead of symlinking, and deliberately does NOT touch
# .specify/agents, .specify/memory, .specify/specs, .specify/templates/overrides,
# or the *.json integration-state files: those hold this-project-specific spec/
# constitution content. Symlinking (or copying) them would make every project
# that submodules this repo read and write into the SAME shared directory,
# clobbering each other's specs. Each consuming project gets its own
# `.specify/memory/constitution.md` and `.specify/specs/` via `specify init` /
# `/speckit.constitution` / `/speckit.specify`, run locally in that project.
#
# These copies are generated — don't hand-edit them. Edit the source under
# how2prompt-agentic/ and re-run this script.
set -euo pipefail

SRC="how2prompt-agentic"
DEST="."

if [ ! -d "$SRC" ]; then
  echo "error: $SRC not found — add the submodule first: git submodule add <repository-url> $SRC" >&2
  exit 1
fi

echo "Syncing shared Spec-Kit tooling from $SRC/..."

# Claude Code skills
mkdir -p "$DEST/.claude/skills"
for skill in "$SRC"/.claude/skills/speckit-*; do
  [ -d "$skill" ] || continue
  name=$(basename "$skill")
  rm -rf "$DEST/.claude/skills/$name"
  cp -R "$skill" "$DEST/.claude/skills/$name"
  echo "✓ Synced Claude skill: $name"
done

# Cursor skills
mkdir -p "$DEST/.cursor/skills"
for skill in "$SRC"/.cursor/skills/speckit-*; do
  [ -d "$skill" ] || continue
  name=$(basename "$skill")
  rm -rf "$DEST/.cursor/skills/$name"
  cp -R "$skill" "$DEST/.cursor/skills/$name"
  echo "✓ Synced Cursor skill: $name"
done

# OpenCode commands
mkdir -p "$DEST/.opencode/commands"
for cmd in "$SRC"/.opencode/commands/speckit.*; do
  [ -f "$cmd" ] || continue
  name=$(basename "$cmd")
  cp "$cmd" "$DEST/.opencode/commands/$name"
  echo "✓ Synced OpenCode command: $name"
done

# Generic Spec-Kit CLI scripts, base templates (not overrides/), and workflows
mkdir -p "$DEST/.specify/scripts" "$DEST/.specify/templates" "$DEST/.specify/workflows"
cp -R "$SRC/.specify/scripts/." "$DEST/.specify/scripts/"
find "$SRC/.specify/templates" -maxdepth 1 -name '*.md' -exec cp {} "$DEST/.specify/templates/" \;
cp -R "$SRC/.specify/workflows/." "$DEST/.specify/workflows/"
echo "✓ Synced .specify/scripts, .specify/templates (base), .specify/workflows"

echo "Sync complete. Run 'specify init' / '/speckit.constitution' in this project to create your own .specify/memory and .specify/specs."
