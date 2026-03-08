# 🇮🇳 Indian Fintech News Blog

A Hugo-powered blog for daily Indian fintech and banking news. Deployed to GitHub Pages.

**Live Site**: https://cashlessconsumer.github.io/fintech-news

## 🚀 Quick Start

### Prerequisites
- [Hugo](https://gohugo.io/installation/) (extended version)
- Git

### Local Development

```bash
# Clone the repository
git clone https://github.com/cashlessconsumer/fintech-news.git
cd fintech-news

# Initialize submodules (for the theme)
git submodule update --init --recursive

# Start development server
hugo server -D

# Open http://localhost:1313 in your browser
```

### Adding New Posts

```bash
# Create a new post
hugo new content posts/YYYY-MM-DD-post-title.md

# Or use the helper script
bun run new-post.ts --title="March 9, 2026 Fintech Update" --content="..."
```

## 📁 Structure

```
.
├── .github/workflows/    # GitHub Actions for deployment
├── archetypes/           # Content templates
├── assets/              # Processed assets (SCSS, JS)
├── content/
│   └── posts/           # Blog posts (Markdown)
├── static/              # Static files (images, etc.)
├── themes/PaperMod      # Hugo theme (submodule)
├── hugo.toml           # Site configuration
└── README.md
```

## 🎨 Theme

Using [PaperMod](https://github.com/adityatelange/hugo-PaperMod) - a clean, fast, and responsive Hugo theme.

## 📝 Content Guidelines

### Blog Post Format

```markdown
---
title: "March 8, 2026 Indian Fintech & Banking Pulse"
date: 2026-03-08T08:00:00+05:30
draft: false
tags: ["RBI", "UPI", "Banking"]
categories: ["Daily News"]
description: "Brief excerpt..."
---

## Daily Indian Fintech & Banking Brief – 8 March 2026

1. **RBI Proposes New Digital Banking Rules**: The Reserve Bank...

Read more: [Money Control](https://www.moneycontrol.com/...)
```

### Link Format
- Use inline markdown links: `[Publication Name](https://complete.url.here)`
- Place "Read more:" lines at the end of each news item
- Never use `[^1]` citations or footnotes
- Never create a "References" section at the bottom

## 🚀 Deployment

The blog automatically deploys to GitHub Pages when you push to `main` branch.

### Manual Setup (First Time)

1. **Create GitHub Repository**
   ```bash
   # Create repo on GitHub named "fintech-news"
   # Then:
   git remote add origin https://github.com/cashlessconsumer/fintech-news.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Source: GitHub Actions

3. **Custom Domain (Optional)**
   - Add your domain in Settings → Pages → Custom domain
   - Create a `CNAME` file with your domain
   - Update `baseURL` in `hugo.toml`

## 🤖 Automated Publishing

The blog can be updated automatically via a scheduled agent. See `scripts/new-post.ts` for the publishing helper.

## 🏷️ Tags

Common tags used:
- `RBI` - Reserve Bank of India updates
- `UPI` - Unified Payments Interface news
- `IPO` - Initial Public Offerings
- `Fintech` - General fintech news
- `Banking` - Banking sector updates
- `Aadhaar` - Digital identity news
- `Technology` - AI, data centers, etc.

## 📄 License

Content: CC BY-SA 4.0
Code: MIT
