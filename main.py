from giorgio import get_random_article_text
from phil_amir import run_question
from player import Player
import crashes
from colorama import Fore
from request_wiki_categories import get_article_content, get_random_valid_title
from zanges_lea import get_fake_passage
from header import header
from pretty_print import get_player_answer
from podium import display_podium

from validation import get_player_number, get_rounds_number, get_player_name


def main() -> None:
    header()
    category = select_category()
    difficulty = select_difficulty()
    run_game(difficulty, category)
        

def select_difficulty():
    question = "Choose difficulty level:"
    options = ["Easy", "Medium", "Hard"]
    choice = get_player_answer(question, options)
    return options[choice].lower()

def select_category() -> str:
    question = "Choose category:"
    categories = [
        "List_of_highest-grossing_films",
        "List of video games considered the best",
        "List of Primetime Emmy Award winners",
        "List of countries by population (United Nations)",
    ]
    choice = get_player_answer(question, categories)
    return categories[choice]

def run_round(difficulty, category, crash=False) -> int:
    # article_dict = get_random_article_text()
    # article_text = article_dict["summary"]
    title = get_random_valid_title(category)
    title, article_content = get_article_content(title)
    fake_passage = get_fake_passage(article_content, difficulty)
    if crash:
        crash_function = crashes.choose_crash()
        crashed_fake_passage = crash_function(fake_passage)
        crashed_article_text = crash_function(article_content)
        return run_question(crashed_fake_passage, crashed_article_text)
    return run_question(fake_passage, article_content)


def run_game(difficulty, category) -> None:
    total_players = get_player_number()
    total_rounds = get_rounds_number()
    crash = False

    players = {}
    for i in range(1, total_players + 1):
        player_name = get_player_name(
            i, players
        )
        players[f"player{i}"] = Player(player_name)

    for game_round in range(1, total_rounds + 1):
        for player in players.values():
            current_player = player

            print(Fore.BLUE + f"Round: {game_round} Player: {current_player.name}")

            if crash:
                score = run_round(difficulty, category, crash=True)
                crash = False
            else:
                score = run_round(difficulty, category)

            if (
                total_players > 1
                and current_player.has_crash
                and game_round < total_rounds
                and crashes.wants_crash()
            ):
                crash = True
                current_player.has_crash = False

            current_player.update_score(score)

    display_podium(players)



if __name__ == "__main__":
    main()
