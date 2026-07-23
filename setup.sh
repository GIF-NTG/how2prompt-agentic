#!/bin/bash
# setup.sh
# Run this from the root of your service repository (e.g. backend/ or frontend/)
# where 'how2prompt-agentic' is integrated as a subdirectory.
# Usage: bash how2prompt-agentic/setup.sh

if [ ! -d "how2prompt-agentic" ]; then
  echo "Error: This script must be executed from the repository root containing 'how2prompt-agentic'."
  echo "Usage: bash how2prompt-agentic/setup.sh"
  exit 1
fi

echo "Initializing Spec-Kit workspace integration..."

# 1. Link .specify folder
if [ ! -d ".specify" ] && [ ! -L ".specify" ]; then
  ln -s how2prompt-agentic/.specify .specify
  echo "✓ Linked .specify to how2prompt-agentic/.specify"
else
  echo "⚠ .specify folder/symlink already exists"
fi

# 2. Link Claude skills (skills are 3 levels deep: .claude/skills/speckit-xxx/)
mkdir -p .claude/skills
for skill in how2prompt-agentic/.claude/skills/speckit-*; do
  if [ -d "$skill" ]; then
    name=$(basename "$skill")
    # Clean up existing directory or symlink to ensure fresh link
    rm -rf ".claude/skills/$name"
    ln -s "../../../$skill" ".claude/skills/$name"
    echo "✓ Linked Claude skill: $name"
  fi
done

# 3. Link Cursor skills (skills are 3 levels deep: .cursor/skills/speckit-xxx/)
mkdir -p .cursor/skills
for skill in how2prompt-agentic/.cursor/skills/speckit-*; do
  if [ -d "$skill" ]; then
    name=$(basename "$skill")
    # Clean up existing directory or symlink to ensure fresh link
    rm -rf ".cursor/skills/$name"
    ln -s "../../../$skill" ".cursor/skills/$name"
    echo "✓ Linked Cursor skill: $name"
  fi
done

# 4. Link OpenCode commands (commands are 2 levels deep: .opencode/commands/speckit.xxx.md)
mkdir -p .opencode/commands
for cmd in how2prompt-agentic/.opencode/commands/speckit.*; do
  if [ -f "$cmd" ]; then
    name=$(basename "$cmd")
    # Clean up existing file or symlink to ensure fresh link
    rm -f ".opencode/commands/$name"
    ln -s "../../$cmd" ".opencode/commands/$name"
    echo "✓ Linked OpenCode command: $name"
  fi
done

echo "Spec-Kit integration completed successfully!"
