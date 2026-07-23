#!/bin/bash
# setup.sh
# Run this from the root directory of your target service repository (e.g. backend/ or frontend/)
# where 'how2prompt-agentic' is placed either parallel or inside the root folder.
# Usage:
#   bash ../how2prompt-agentic/setup.sh    (if parallel)
#   bash how2prompt-agentic/setup.sh       (if inside)

SUBMODULE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$(pwd)"

echo "Initializing Spec-Kit workspace integration..."
echo "  Source Submodule: ${SUBMODULE_DIR}"
echo "  Target Workspace: ${TARGET_DIR}"

if [ "${SUBMODULE_DIR}" = "${TARGET_DIR}" ]; then
  echo "Warning: Running setup.sh inside the submodule directory itself. Typically you should run this script from the root of your service repository (e.g. backend/ or frontend/)."
  read -p "Do you want to proceed with linking inside the submodule directory? (y/N) " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    exit 0
  fi
fi

# 1. Link .specify folder
if [ ! -d "${TARGET_DIR}/.specify" ] && [ ! -L "${TARGET_DIR}/.specify" ]; then
  ln -s "${SUBMODULE_DIR}/.specify" "${TARGET_DIR}/.specify"
  echo "✓ Linked .specify -> ${SUBMODULE_DIR}/.specify"
else
  echo "⚠ .specify folder/symlink already exists at target"
fi

# 2. Link Claude skills
mkdir -p "${TARGET_DIR}/.claude/skills"
for skill in "${SUBMODULE_DIR}/.claude/skills"/speckit-*; do
  if [ -d "$skill" ]; then
    name=$(basename "$skill")
    rm -rf "${TARGET_DIR}/.claude/skills/${name}"
    ln -s "$skill" "${TARGET_DIR}/.claude/skills/${name}"
    echo "✓ Linked Claude skill: ${name}"
  fi
done

# 3. Link Cursor skills
mkdir -p "${TARGET_DIR}/.cursor/skills"
for skill in "${SUBMODULE_DIR}/.cursor/skills"/speckit-*; do
  if [ -d "$skill" ]; then
    name=$(basename "$skill")
    rm -rf "${TARGET_DIR}/.cursor/skills/${name}"
    ln -s "$skill" "${TARGET_DIR}/.cursor/skills/${name}"
    echo "✓ Linked Cursor skill: ${name}"
  fi
done

# 4. Link OpenCode commands
mkdir -p "${TARGET_DIR}/.opencode/commands"
for cmd in "${SUBMODULE_DIR}/.opencode/commands"/speckit.*; do
  if [ -f "$cmd" ]; then
    name=$(basename "$cmd")
    rm -f "${TARGET_DIR}/.opencode/commands/${name}"
    ln -s "$cmd" "${TARGET_DIR}/.opencode/commands/${name}"
    echo "✓ Linked OpenCode command: ${name}"
  fi
done

echo "Spec-Kit integration completed successfully!"
