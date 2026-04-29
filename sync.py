"""
sync.py — Fetches new articles from bmak.substack.com RSS feed,
converts them to markdown, saves to articles/, and updates README.md.
Run locally or via GitHub Actions.
"""

import feedparser
import requests
from bs4 import BeautifulSoup
import markdownify
import os
import re
import glob

FEED_URL = "https://bmak.substack.com/feed"
ARTICLES_DIR = "articles"
README_PATH = "README.md"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; substack-archiver/1.0)"
}


def slugify(title):
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug.strip())
    slug = re.sub(r'-+', '-', slug)
    return slug[:80]


def clean_markdown(md):
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = re.sub(r'!\[.*?\]\(.*?\)', '', md)
    return md.strip()


def fetch_article_content(url):
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')

    title_el = soup.find('h1', class_=re.compile('post-title|title')) or soup.find('h1')
    title = title_el.get_text(strip=True) if title_el else "Untitled"

    subtitle_el = soup.find('h3', class_=re.compile('subtitle')) or soup.find('div', class_=re.compile('subtitle'))
    subtitle = subtitle_el.get_text(strip=True) if subtitle_el else None

    body = (
        soup.find('div', class_=re.compile(r'body\b')) or
        soup.find('div', class_='available-content') or
        soup.find('div', class_=re.compile('post-content')) or
        soup.find('article')
    )

    if not body:
        return None, title, subtitle

    content_md = markdownify.markdownify(str(body), heading_style="ATX", bullets="-")
    content_md = clean_markdown(content_md)
    return content_md, title, subtitle


def build_markdown(title, subtitle, date, url, content_md):
    parts = [f"# {title}"]
    if subtitle:
        parts.append(f"*{subtitle}*")
    parts.append(f"\n**Published:** {date}  \n**Source:** [{url}]({url})")
    parts.append("---")
    parts.append(content_md)
    return "\n\n".join(parts)


def get_existing_slugs():
    files = glob.glob(os.path.join(ARTICLES_DIR, "*.md"))
    slugs = set()
    for f in files:
        basename = os.path.basename(f)
        # Strip date prefix: YYYY-MM-DD-slug.md -> slug
        match = re.match(r'^\d{4}-\d{2}-\d{2}-(.+)\.md$', basename)
        if match:
            slugs.add(match.group(1))
    return slugs


def update_readme(articles):
    """Rebuild README table from all articles in the articles/ dir."""
    rows = []
    for date, title, filename in sorted(articles, reverse=True):
        rows.append(f"| {date} | [{title}](articles/{filename}) |")

    table = "| Date | Title |\n|------|-------|\n" + "\n".join(rows)

    with open(README_PATH, 'r') as f:
        readme = f.read()

    # Replace the table between the ## Articles header and ## Auto-sync header
    readme = re.sub(
        r'(## Articles\n\n).*?(\n\n## Auto-sync)',
        rf'\g<1>{table}\g<2>',
        readme,
        flags=re.DOTALL
    )

    with open(README_PATH, 'w') as f:
        f.write(readme)


def collect_existing_articles():
    """Return list of (date, title, filename) from existing markdown files."""
    articles = []
    for filepath in glob.glob(os.path.join(ARTICLES_DIR, "*.md")):
        filename = os.path.basename(filepath)
        match = re.match(r'^(\d{4}-\d{2}-\d{2})-(.+)\.md$', filename)
        if not match:
            continue
        date = match.group(1)
        with open(filepath, 'r') as f:
            first_line = f.readline().strip()
        title = first_line.lstrip('#').strip()
        articles.append((date, title, filename))
    return articles


def main():
    os.makedirs(ARTICLES_DIR, exist_ok=True)
    existing_slugs = get_existing_slugs()

    feed = feedparser.parse(FEED_URL)
    new_articles = []

    for entry in feed.entries:
        url = entry.link
        slug = slugify(entry.title)

        if slug in existing_slugs:
            print(f"  Already exists: {slug}")
            continue

        try:
            published = entry.published_parsed
            date = f"{published.tm_year}-{published.tm_mon:02d}-{published.tm_mday:02d}"
        except Exception:
            date = "unknown-date"

        print(f"  Fetching new article: {entry.title}")
        content_md, title, subtitle = fetch_article_content(url)

        if not content_md:
            print(f"  WARNING: No content found for {url}")
            continue

        md = build_markdown(title, subtitle, date, url, content_md)
        filename = f"{date}-{slug}.md"
        filepath = os.path.join(ARTICLES_DIR, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md)

        print(f"  Saved: {filename}")
        new_articles.append((date, title, filename))

    if new_articles:
        all_articles = collect_existing_articles()
        update_readme(all_articles)
        print(f"\nAdded {len(new_articles)} new article(s) and updated README.")
    else:
        print("\nNo new articles found.")


if __name__ == "__main__":
    main()
