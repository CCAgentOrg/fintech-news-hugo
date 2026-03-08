---
title: "Agent: Stakeholder Agent (On-Demand)"
date: 2026-03-08T12:00:00+05:30
draft: false
tags: ["Agents", "AI", "Stakeholders", "On-Demand"]
categories: ["Meta"]
description: "On-demand agent to generate stakeholder directories and relationship maps"
---

# 🤖 Agent: Stakeholder Agent (On-Demand)

## Overview

| Property | Value |
|----------|-------|
| **Name** | Stakeholder Agent |
| **Type** | On-Demand |
| **Trigger** | Manual / Issue-based |
| **Model** | minimax-m2.5 |
| **Output** | Comprehensive stakeholder directory |

## Mission

Generate and maintain stakeholder directories mapping key players, their relationships, and hierarchies in the fintech/DPI ecosystem.

## Trigger

This agent runs when:
1. A new issue requests a stakeholder map
2. Major regulatory/policy change requires stakeholder update
3. Quarterly refresh of existing stakeholder pages

## Stakeholder Categories

For Fintech:
- Regulators: RBI, SEBI, IRDAI, FIU-IND
- Payment Infrastructure: NPCI, Banks, TPAPs
- Fintech Companies: Startups, NBFCs, Lenders
- Industry Bodies: IAMAI, Fintech India, IBA
- Consumer Advocacy: CashlessConsumer, PAIGAM

For DPI:
- Identity: UIDAI, MeitY
- Finance: NPCI, RBI, SIDBI
- Health: NHA, Ayushman Bharat
- Agriculture: AgriStack, Mahindra
- Governance: DARPG, MeitY, States

## Output Format

See existing stakeholders.md for format structure.

## Publishing

```bash
# Update stakeholder directory
TOPIC="[Sector Name]"
cat > content/stakeholders.md << 'EOF'
[generated content]
EOF

git add content/stakeholders.md
git commit -m "Update stakeholders: ${TOPIC}"
git push
```

## Quality Checklist

- [ ] All key stakeholders included
- [ ] Contact/official links verified
- [ ] Hierarchical relationships clear
- [ ] Recent updates reflected
- [ ] Consumer contact points listed
