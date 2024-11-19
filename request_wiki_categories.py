import random

import requests
import re

from unicodedata import category



def fetch_articles(category):
    # Step 1: Fetch article content
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": category,
        "prop": "revisions",
        "rvprop": "content",
        "format": "json"
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
    filtered_titles = [title.split('|')[0] for title in articles if not title.startswith("File:")]

    return filtered_titles



def get_random_valid_title(category):
    movie_titles = fetch_articles(category)

    while True:
        article :str = random.choice(movie_titles)
        if article.startswith("List of"):
            print(article, "Wrong")
            continue
        if re.match(r"\S*#\S*", article):
            print(article, "Wrong")
            continue
        return article

def get_article_content(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()

    pages = data.get("query", {}).get("pages", {})
    for page_id, page_data in pages.items():
        title = page_data.get("title", None)
        summary = page_data.get("extract", None)
        return title, summary


# for category in CATEGORIES:
#     article_title = get_random_valid_title(category)
#     article = get_article_content(article_title)
