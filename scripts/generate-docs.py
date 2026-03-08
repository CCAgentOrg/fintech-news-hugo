#!/usr/bin/env python3
"""
Sync script to keep README, AGENTS.md, llms.txt, about page, agents.json, and live Zo agents in sync.
Run this whenever agent configuration changes.
"""

import json
import os
from datetime import datetime

# Read agents.json as source of truth
with open('agents.json', 'r') as f:
    agents_data = json.load(f)

# Generate AGENTS.md
agents_md = """# 🤖 AI Agents — Cashless Watch

> **Source of Truth**: This file is auto-generated from `agents.json`. Do not edit manually.

## Active Agents ({count})

| Agent | Schedule | Focus | Status |
|-------|----------|-------|--------|
""".format(count=len(agents_data['agents']))

for agent in agents_data['agents']:
    status = "✅ Active" if agent.get('active', True) else "⏸ Paused"
    agents_md += f"| {agent['name']} | {agent['schedule']} | {agent['focus']} | {status} |\n"

agents_md += """
## Agent Details

See `content/agents/` for full instruction files.

## Contributing

1. Edit `agents.json` to add/modify agents
2. Run `python scripts/generate-docs.py` to regenerate docs
3. Commit all changes

## Last Sync
"""

with open('AGENTS.md', 'w') as f:
    f.write(agents_md)

# Generate llms.txt sections
llms_txt = f"""# Cashless Watch - llms.txt
# AI-agent-optimized documentation

## Site Overview
**Name**: Cashless Watch
**URL**: https://watch.cashlessconsumer.in
**Description**: {agents_data['description']}
**Content Types**: {', '.join(agents_data['content_types'])}

## Active Agents ({count})
""".format(count=len(agents_data['agents']))

for agent in agents_data['agents']:
    llms_txt += f"- **{agent['name']}**: {agent['focus']} ({agent['schedule']})\n"

with open('static/llms.txt', 'w') as f:
    f.write(llms_txt)

print(f"✅ Generated docs for {len(agents_data['agents'])} agents")
