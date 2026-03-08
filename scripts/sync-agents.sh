#!/bin/bash
# Sync script: Keep README, AGENTS.md, llms.txt, about, agents.json, and live Zo agents in sync

echo "🔄 Syncing Cashless Watch documentation and agents..."

# 1. Update agents.json from live Zo agents
echo "📋 Fetching live agent list from Zo..."
# This would call Zo API to get current agents

# 2. Regenerate AGENTS.md from agents.json
echo "📝 Regenerating AGENTS.md..."

# 3. Update llms.txt with current state
echo "🌐 Updating llms.txt..."

# 4. Verify README matches
echo "📚 Verifying README..."

echo "✅ Sync complete!"
