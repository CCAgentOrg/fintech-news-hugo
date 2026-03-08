# 🚀 Deployment Guide

## GitHub Pages Setup

### Step 1: Create GitHub Repository

```bash
cd /home/workspace/Blog/fintech-news-hugo
git remote add origin https://github.com/cashlessconsumer/fintech-news.git
git branch -m main
git add .
git commit -m "Initial commit: Hugo blog with PaperMod theme"
git push -u origin main
```

### Step 2: Enable GitHub Pages

1. Go to https://github.com/cashlessconsumer/fintech-news/settings/pages
2. **Source**: Select "GitHub Actions"
3. Wait for the first deployment (check Actions tab)

### Step 3: Custom Domain (Optional)

1. Edit `static/CNAME`:
   ```
   fintech.cashlessconsumer.in
   ```

2. Go to your DNS provider and add a CNAME record:
   ```
   fintech.cashlessconsumer.in → cashlessconsumer.github.io
   ```

3. Enable HTTPS in GitHub Pages settings (auto-issued by Let's Encrypt)

4. Update `hugo.toml`:
   ```toml
   baseURL = 'https://fintech.cashlessconsumer.in'
   ```

### Step 4: Verify Deployment

- Site will be live at: `https://cashlessconsumer.github.io/fintech-news`
- Or your custom domain: `https://fintech.cashlessconsumer.in`

## 📝 Daily Publishing Workflow

The scheduled agent will automatically:
1. Research latest fintech news
2. Create a new post using the helper script
3. Commit and push to trigger deployment

### Manual Publishing

```bash
cd /home/workspace/Blog/fintech-news-hugo

# Create new post
bun run scripts/new-post.ts \
  --title="March 9, 2026 Indian Fintech & Banking Pulse" \
  --content="Your markdown content here..." \
  --tags="RBI,UPI,Banking"

# Preview locally
hugo server -D

# Deploy
git add content/posts/
git commit -m "Add: March 9, 2026 fintech update"
git push origin main
```

## 🔧 Troubleshooting

**Build fails?**
- Check Hugo version: `hugo version` (needs 0.146.0+)
- Verify theme submodule: `git submodule update --init --recursive`

**Theme issues?**
- PaperMod requires Hugo 0.146.0+
- Update theme: `cd themes/PaperMod && git pull`

**Links not working?**
- Ensure all URLs in posts start with `https://`
- Check markdown format: `[Text](https://url.com)`

## 📊 GitHub Actions

The `.github/workflows/deploy.yml` handles:
- Building on every push to `main`
- Deploying to GitHub Pages
- Works with both github.io and custom domains

Check deployment status in the Actions tab of your repository.
