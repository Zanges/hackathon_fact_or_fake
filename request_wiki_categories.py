import random
import re

import requests


def fetch_articles(category: str) -> list[str]:
    """Fetch article titles form wikipedia corresponding to chosen category"""
    # Step 1: Fetch article content
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": category,
        "prop": "revisions",
        "rvprop": "content",
        "format": "json",
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Step 2: Extract content
    pages = data.get("query", {}).get("pages", {})
    page = next(iter(pages.values()))
    content = page.get("revisions", [{}])[0].get("*", "")

    if category == "List of countries by population (United Nations)":
        articles = re.findall(r"\[\[([^\]]+)\]\]", content)
    else:
        articles = re.findall(r"''\[\[([^\]]+)\]\]''", content)

    # Filter out non-movie links (e.g., sections or unrelated links)
    filtered_titles = [
        title.split("|")[0] for title in articles if not title.startswith("File:")
    ]

    return filtered_titles


def get_random_valid_title(category: str) -> str:
    """Pick one random title from fetched article list"""
    titles = fetch_articles(category)

    while True:
        article = random.choice(titles)
        if article.startswith("List of"):
            continue
        if re.match(r"\S*#\S*", article):
            continue
        return article


def get_article_content(title: str) -> tuple[str, str]:
    """Get article content from given title"""
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "format": "json",
    }
    response = requests.get(url, params=params)
    data = response.json()

    pages = data.get("query", {}).get("pages", {})
    for page_id, page_data in pages.items():
        title = page_data.get("title", None)
        summary = page_data.get("extract", None)
        return title, summary
