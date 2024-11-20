from giorgio import get_random_article_text
from lea import get_passage
from game_logic import run_question
from giorgio import get_random_article_text
from zanges import get_fake_passage


def main():
    score = 0
    i = 0
    while i < 3:
        article_dict = get_random_article_text()
        article_text = article_dict["summary"]
        # passage = get_passage(article_text)
        fake_passage = get_fake_passage(article_text)
        print("-"*50)
        score += run_question(fake_passage, article_text)
        i += 1

if __name__ == "__main__":
    main()
