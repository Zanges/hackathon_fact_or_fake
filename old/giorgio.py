# import requests
import wikipedia

def get_random_article_text():
    article = ""
    while True:
        try:
            random_article_title = wikipedia.random()
            article = getattr(wikipedia, 'page')(random_article_title)
            summary = article.summary
            if len(summary) < 100:
                continue
            break
        except Exception as e:
            print(f"Error, trying again. {e}")
    return {
     'summary': article.summary,
     'title': article.title,
     'content': article.content
    }

# random_article = get_random_article_text()
# print('----------------------------------------')
# print('title: ', random_article["title"])
# print('----------------------------------------')
# print('summary: ', random_article["summary"])
# print('----------------------------------------')
# print('content: ', random_article["content"])
