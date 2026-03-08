#!/usr/bin/env bun
/**
 * Create a new blog post for Hugo
 * 
 * Usage: bun run scripts/new-post.ts --title="Title" --content="..." [--date=2026-03-09] [--tags="RBI,UPI"]
 */

function showHelp() {
  console.log(`
Create a new blog post for the Indian Fintech News Hugo blog.

Usage:
  bun run scripts/new-post.ts --title="March 9, 2026 Fintech Update" \\
    --content="Post content with [links](https://...)" \\
    [--date=2026-03-09] \\
    [--tags="RBI,UPI,Banking"]

Options:
  --title     Post title (required)
  --content   Post content in markdown (required)
  --date      Date in YYYY-MM-DD format (defaults to today)
  --tags      Comma-separated tags (optional)
  --excerpt   Custom excerpt (optional, auto-generated from content)
  --help      Show this help message
`);
  process.exit(0);
}

function parseArgs() {
  const args: Record<string, string> = {};
  for (let i = 2; i < process.argv.length; i++) {
    const arg = process.argv[i];
    if (arg === '--help') showHelp();
    if (arg.startsWith('--')) {
      const key = arg.slice(2);
      const value = process.argv[i + 1] || '';
      if (!value.startsWith('--') && value) {
        args[key] = value;
        i++;
      }
    }
  }
  return args;
}

function generateExcerpt(content: string): string {
  // Remove markdown and get first sentence or 150 chars
  const plain = content
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')  // Remove markdown links
    .replace(/[#*_`]/g, '')                   // Remove formatting
    .replace(/\n+/g, ' ')                    // Replace newlines with spaces
    .trim();
  
  const firstSentence = plain.split(/[.!?]\s+/)[0];
  return firstSentence.length > 150 
    ? firstSentence.slice(0, 150) + '...'
    : firstSentence + '.';
}

function suggestTags(content: string): string[] {
  const tags: string[] = [];
  const content_lower = content.toLowerCase();
  
  if (content.includes('RBI') || content_lower.includes('reserve bank'))
    tags.push('RBI');
  if (content.includes('UPI'))
    tags.push('UPI');
  if (content.includes('IPO') || content_lower.includes('public offering'))
    tags.push('IPO');
  if (content_lower.includes('fintech') || content_lower.includes('funding'))
    tags.push('Fintech');
  if (content_lower.includes('bank') || content_lower.includes('lending'))
    tags.push('Banking');
  if (content.includes('Aadhaar'))
    tags.push('Aadhaar');
  if (content.includes('AI') || content_lower.includes('data center'))
    tags.push('Technology');
  
  if (tags.length === 0) tags.push('Fintech', 'Banking');
  return tags;
}

function main() {
  const args = parseArgs();
  
  // Validate required args
  if (!args.title || !args.content) {
    console.error('Error: --title and --content are required\n');
    showHelp();
  }
  
  const title = args.title;
  const content = args.content;
  const date = args.date || new Date().toISOString().split('T')[0];
  const excerpt = args.excerpt || generateExcerpt(content);
  const tags = args.tags 
    ? args.tags.split(',').map(t => t.trim())
    : suggestTags(content);
  
  // Create slug from title
  const slug = title
    .toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .replace(/\s+/g, '-')
    .slice(0, 50);
  
  const filename = `${date}-${slug}.md`;
  const filepath = `content/posts/${filename}`;
  
  // Create frontmatter and content
  const postContent = `---
title: "${title}"
date: ${date}T08:00:00+05:30
draft: false
tags: [${tags.map(t => `"${t}"`).join(', ')}]
categories: ["Daily News"]
description: "${excerpt}"
---

${content}
`;
  
  // Write file
  const fs = require('fs');
  fs.mkdirSync('content/posts', { recursive: true });
  fs.writeFileSync(filepath, postContent, 'utf-8');
  
  console.log(`✅ Created post: ${filepath}`);
  console.log(`\nTitle: ${title}`);
  console.log(`Date: ${date}`);
  console.log(`Tags: ${tags.join(', ')}`);
  console.log(`\nNext steps:`);
  console.log(`  1. Review the post: ${filepath}`);
  console.log(`  2. git add ${filepath}`);
  console.log(`  3. git commit -m "Add post: ${title}"`);
  console.log(`  4. git push origin main`);
  console.log(`\nThe post will be live at: https://cashlessconsumer.github.io/fintech-news/posts/${date}-${slug}/`);
}

main();
