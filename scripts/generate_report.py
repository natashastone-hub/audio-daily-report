"""
Audio Daily Report Generator Script.
This script takes a JSON input containing papers and news, applies the HTML template,
and writes the daily report HTML file.

Usage:
  python generate_report.py --date 2026-06-27 --input report_data.json --output-dir reports/
"""

import json
import sys
import os
from datetime import datetime

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), '..', 'templates', 'daily-report.html')

def load_template():
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def format_paper(p):
    """Format a single paper entry into HTML."""
    tags_html = ''.join(f'<span class="tag">{t}</span>' for t in p.get('tags', []))
    links_html = ''
    for l in p.get('links', []):
        label = l.get('label', 'Link')
        url = l.get('url', '#')
        links_html += f'<a href="{url}" target="_blank">🔗 {label}</a> '
    highlight = ' ⭐' if p.get('highlight') else ''
    return f'''
    <div class="paper">
      <h4><a href="{p.get("url", "#")}" target="_blank">{p["title"]}</a>{highlight}</h4>
      <div class="meta"><span>📅 {p.get("date", "")}</span><span>👥 {p.get("authors", "")}</span></div>
      <div class="abstract">{p.get("abstract", "")}</div>
      <div class="tags">{tags_html}</div>
      <div class="links">{links_html}</div>
    </div>'''

def format_news(n):
    """Format a single news item into HTML."""
    url_html = f' <a href="{n["url"]}" target="_blank">阅读原文 →</a>' if n.get('url') else ''
    return f'''
    <div class="news-item">
      <h4>{n["title"]}</h4>
      <p>{n.get("summary", "")}{url_html}</p>
    </div>'''

def generate_report(date_str, data):
    """
    Generate a daily report HTML file.
    
    data format:
    {
      "papers": [
        {
          "title": "...",
          "url": "https://arxiv.org/abs/...",
          "date": "2026-06-27",
          "authors": "Author et al.",
          "abstract": "...",
          "tags": ["TTS", "Zero-shot"],
          "highlight": true,
          "links": [{"label": "arXiv", "url": "..."}, {"label": "GitHub", "url": "..."}]
        }
      ],
      "news": [
        {
          "title": "...",
          "url": "https://...",
          "summary": "..."
        }
      ]
    }
    """
    template = load_template()
    
    papers = data.get('papers', [])
    news_items = data.get('news', [])
    highlights = [p for p in papers if p.get('highlight')]
    
    # Format display date
    dt = datetime.strptime(date_str, '%Y-%m-%d')
    weekdays = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    date_display = f"{dt.year}年{dt.month}月{dt.day}日 ({weekdays[dt.weekday()]})"
    
    # Build content
    content_parts = []
    
    if highlights:
        content_parts.append('<div class="section"><h3>⭐ 重点推荐</h3>')
        for p in highlights:
            content_parts.append(format_paper(p))
        content_parts.append('</div>')
    
    if papers:
        regular = [p for p in papers if not p.get('highlight')]
        if regular:
            content_parts.append('<div class="section"><h3>📄 最新论文</h3>')
            for p in regular:
                content_parts.append(format_paper(p))
            content_parts.append('</div>')
    
    if news_items:
        content_parts.append('<div class="section"><h3>📰 前沿新闻</h3>')
        for n in news_items:
            content_parts.append(format_news(n))
        content_parts.append('</div>')
    
    # Replace placeholders
    html = template
    html = html.replace('{{DATE}}', date_str)
    html = html.replace('{{DATE_DISPLAY}}', date_display)
    html = html.replace('{{PAPER_COUNT}}', str(len(papers)))
    html = html.replace('{{NEWS_COUNT}}', str(len(news_items)))
    html = html.replace('{{HIGHLIGHT_COUNT}}', str(len(highlights)))
    html = html.replace('{{CONTENT}}', '\n'.join(content_parts))
    
    return html

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Generate Audio Daily Report HTML')
    parser.add_argument('--date', required=True, help='Date string YYYY-MM-DD')
    parser.add_argument('--input', required=True, help='Path to JSON input file')
    parser.add_argument('--output-dir', default='reports', help='Output directory for HTML')
    args = parser.parse_args()
    
    with open(args.input, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    html = generate_report(args.date, data)
    
    os.makedirs(args.output_dir, exist_ok=True)
    output_path = os.path.join(args.output_dir, f'{args.date}.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f'Report generated: {output_path}')
    print(f'Papers: {len(data.get("papers", []))}, News: {len(data.get("news", []))}, Highlights: {sum(1 for p in data.get("papers", []) if p.get("highlight"))}')

if __name__ == '__main__':
    main()
