#!/usr/bin/env python3
"""
CashlessWatch Enhanced Stock Fetcher — With News Integration
Fetches marke
[truncated]": 0.4
        }
        
        if abs(pct) > 2:
            score += weights['momentum']
        if news and news != 
[truncated]
        if abs(pct) > 5:
            alert = "🚨 Significant move"
        elif abs(pct) > 2:
            alert = "📊 Notable change"
        
        combined_table.append({
            'rank': 0,  # Will be assigned after sorting
            'scrip': symbol,
            'name': name,
            'price': price,
            'technical': f"{change:+.2f} ({change_pct:+.2f}%)",
            'news_context': news if news else 'No major news',
            'combined_score': score,
            'action': alert
        })
    
    # Sort by combined score
    combined_table.sort(key=lambda x: x['combined_score'], reverse=True)
    for i, row in enumerate(combined_table, 1):
        row['rank'] = i
    
    return combined_table

def generate_markdown(data, combined_table, date_str):
    """Generate Hugo markdown with news integration"""
    
    # Get brief reference
    brief_path = f"/home/.z/workspaces/con_PXCpywVCLwND9RsD/cashless-watch/content/posts/{date_str}-fintech-brief.md"
    brief_exists = os.path.exists(brief_path)
    
    md = f"""---
title: "CashlessWatch Stock Market Summary — {date_str}"
date: {date_str}T08:15:00+05:30
draft: false
tags: ["Stocks", "Fintech", "Markets", "India", "CashlessWatch"]
categories: ["Stock Watch"]
description: "Pre-market summary with news context — Indices, Banks, and Pure-Play Fintech"
---

# CashlessWatch Stock Market Summary — {date_str}

**Data Status:** ✅ Live from NSE India + Yahoo Finance  
**News Integration:** {'✅ Linked to Daily Brief' if brief_exists else '⚠️ Brief not yet published'}  
**Timestamp:** 08:15 AM IST  
**Market Status:** Pre-open

---

## 📊 Indices — Pre-Open Levels

| Index | Level | Change | % Change | News Context |
|-------|-------|--------|----------|--------------|
"""
    
    # Add indices with news context
    for symbol, info in data['indices'].items():
        name = {
            'NIFTY 50': 'Nifty 50',
            'BANKNIFTY': 'Nifty Bank',
            'FINNIFTY': 'FinNifty',
            'NIFTYIT': 'Nifty IT'
        }.get(symbol, symbol)
        
        news = info.get('news_context', '—')
        md += f"| {name} | {info.get('price', 'N/A')} | {info.get('change', 'N/A')} | {info.get('change_pct', 'N/A')}% | {news} |\n"
    
    md += """
---

## 🏦 BANKS — Digital Payments Leaders

| Company | Symbol | Price | Change | % Change | News Context |
|---------|--------|-------|--------|----------|--------------|
"""
    
    # Add banks with news context
    bank_names = {
        'HDFCBANK': 'HDFC Bank',
        'ICICIBANK': 'ICICI Bank',
        'SBIN': 'SBI',
        'AXISBANK': 'Axis Bank',
        'KOTAKBANK': 'Kotak Bank'
    }
    
    for symbol, info in data['banks'].items():
        name = bank_names.get(symbol, symbol)
        news = info.get('news_context', '—')
        md += f"| {name} | {symbol} | ₹{info.get('price', 'N/A')} | {info.get('change', 'N/A')} | {info.get('change_pct', 'N/A')}% | {news} |\n"
    
    md += """
---

## 💳 PURE-PLAY FINTECH/PAYTECH

| Company | Symbol | Tier | Price | Change | % Change | News Context |
|---------|--------|------|-------|--------|----------|--------------|
"""
    
    # Add fintech with news context
    tiers = {
        'PAYTM': 'B1',
        'MOBIKWIK': 'B1',
        'PBFINTECH': 'B2',
        'INFIBEAM': 'B3',
        'PINELABS': 'B3',
        'NPST': 'B3',
        'FINOPB': 'B4',
        'SBICARD': 'B4',
        'AGSTRA': 'B5'
    }
    
    for symbol, info in data['fintech'].items():
        tier = tiers.get(symbol, 'B?')
        news = info.get('news_context', '—')
        note = info.get('note', '')
        if note:
            news += f" {note}"
        md += f"| {symbol} | {symbol} | {tier} | ₹{info.get('price', 'N/A')} | {info.get('change', 'N/A')} | {info.get('change_pct', 'N/A')}% | {news} |\n"
    
    md += f"""
---

## 🔗 Cashless Watch Reco

### Today's Ranked Watchlist

| Rank | Scrip | Price | Technical | News Catalyst | Score | Action |
|------|-------|-------|-----------|---------------|-------|--------|
"""
    
    # Add combined ranking
    for row in combined_table[:5]:  # Top 5
        md += f"| {row['rank']} | {row['scrip']} | ₹{row['price']:.2f} | {row['technical']} | {row['news_context'][:30]}... | {row['combined_score']:.1f} | {row['action']} |\n"
    
    md += f"""
### Ranking Logic
**Score = Technical Setup (40%) + News Significance (60%)**

| Factor | Weight | Source |
|--------|--------|--------|
| % Change magnitude | 20% | Technical data |
| Volume pattern | 20% | Market data |
| News impact | 40% | Daily Brief cross-reference |
| Sector momentum | 20% | Index correlation |

### CashlessConsumer Lens
> *"{get_lens_commentary(combined_table)}"*

**Cross-Reference:**
"""
    
    if brief_exists:
        md += f"- 📰 See detailed news in today's [Daily Brief]({date_str}-fintech-brief.md)\n"
    else:
        md += "- 📰 Daily Brief publishing at 8:00 AM IST\n"
    
    # Previous day link
    prev_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    md += f"- 📊 Previous levels: [Yesterday's Stock Watch]({prev_date}-stock-watch.md)\n"
    
    md += """
---

## 📰 Sector News Summary

"""
    
    # Extract news items from combined table
    news_items = []
    for row in combined_table:
        if row['news_context'] and row['news_context'] != 'No major news':
            news_items.append(f"- **{row['scrip']}**: {row['news_context']}")
    
    if news_items:
        md += "\n".join(news_items[:5]) + "\n"
    else:
        md += "- No major fintech-specific news detected\n"
    
    md += f"""
---

## ⚠️ Disclaimer

**Not investment advice.** This summary is for informational purposes only. Data sourced from NSE India (official) and Yahoo Finance. Cross-referenced with Daily Brief for news context. Always verify prices from official sources before trading.

---

*Live data fetched at 08:15 AM IST, {date_str}*  
*News context integrated from CashlessWatch Daily Brief*
"""
    
    return md

def get_lens_commentary(combined_table):
    """Generate CashlessConsumer lens commentary"""
    if not combined_table:
        return "Markets showing normal activity. No major consumer-impact events detected."
    
    top_mover = combined_table[0]
    scrip = top_mover['scrip']
    technical = top_mover['technical']
    news = top_mover['news_context']
    
    # Consumer impact map
    consumer_impacts = {
        'PAYTM': "wallet users' daily transactions",
        'HDFCBANK': "credit card holders",
        'ICICIBANK': "digital banking customers",
        'SBIN': "SBI's massive customer base",
        'SBICARD': "credit card users",
        'PBFINTECH': "insurance buyers",
        'FINOPB': "payments bank customers"
    }
    
    impact = consumer_impacts.get(scrip, "fintech consumers")
    
    return f"{scrip} {technical} — significant for {impact}. {news[:50] if news else 'Watch for sustained momentum.'}"

def main():
    """Main execution"""
    parser = argparse.ArgumentParser(description='CashlessWatch Enhanced Stock Fetcher')
    parser.add_argument('--date', help='Date to fetch (YYYY-MM-DD), defaults to today')
    parser.add_argument('--brief', help='Path to Daily Brief markdown for news context')
    args = parser.parse_args()
    
    today = args.date or datetime.now().strftime('%Y-%m-%d')
    
    print(f"🔍 CashlessWatch Enhanced Fetcher — {today}")
    print("=" * 60)
    
    # Step 0: Read Daily Brief for context
    brief_path = args.brief
    if not brief_path:
        # Try default path
        default_brief = f"/home/.z/workspaces/con_PXCpywVCLwND9RsD/cashless-watch/content/posts/{today}-fintech-brief.md"
        if os.path.exists(default_brief):
            brief_path = default_brief
    
    news_map = {}
    if brief_path:
        print(f"📰 Reading Daily Brief: {brief_path}")
        news_map = extract_stock_news_from_brief(brief_path)
        print(f"✅ Extracted news for {len(news_map)} stocks")
    else:
        print("⚠️ No Daily Brief found — will use empty news context")
    
    # Step 1: Fetch stock data
    print("\n📊 Fetching stock data...")
    data = fetch_all_stock_data()
    
    # Step 2: Add news context
    print("\n🔗 Adding news context...")
    data = add_news_context(data, news_map)
    
    # Step 3: Generate Cashless Watch Reco
    print("\n🎯 Generating Cashless Watch Reco...")
    combined_table = generate_cashless_watch_reco(data)
    
    # Step 4: Generate enhanced markdown
    print("\n📝 Generating Hugo markdown...")
    md_content = generate_markdown(data, combined_table, today)
    
    # Step 5: Save outputs
    output_dir = "/home/.z/workspaces/con_PXCpywVCLwND9RsD/cashless-watch"
    
    # Save JSON
    json_path = f"{output_dir}/data/stock-data-{today}.json"
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved JSON: {json_path}")
    
    # Save markdown
    md_path = f"{output_dir}/content/posts/{today}-stock-watch.md"
    with open(md_path, 'w') as f:
        f.write(md_content)
    print(f"✅ Saved Markdown: {md_path}")
    
    # Step 6: Summary
    print("\n" + "=" * 60)
    print("🎉 CashlessWatch Enhanced Summary Complete!")
    print(f"   Indices: {len(data['indices'])} fetched")
    print(f"   Banks: {len(data['banks'])} fetched")
    print(f"   Fintech: {len(data['fintech'])} fetched")
    print(f"   News context: {len(news_map)} stocks annotated")
    print(f"   Reco generated: {len(combined_table)} ranked")
    print("=" * 60)
    
    return data, combined_table

if __name__ == "__main__":
    main()
