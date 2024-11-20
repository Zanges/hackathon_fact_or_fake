from ai_api import DIFFICULTIES
from game_logic import run_game
from pretty_print import (
    get_player_answer,
    header,
    opening_screen,
)


def main() -> None:
    opening_screen()
    header()
    category = select_category()
    difficulty = select_difficulty()
    run_game(difficulty, category)


def select_difficulty() -> str:
    """Ask User to choose between three difficulties"""
    question = "Choose difficulty level:"
    options = list(DIFFICULTIES.keys())
    choice = get_player_answer(question, options)
    return options[choice].lower()


def select_category() -> str:
    """Ask User to choose between predefined categories"""
    question = "Choose category:"
    categories = {
        "Movies": "List_of_highest-grossing_films",
        "Video Games": "List of video games considered the best",
        "TV-Shows": "List of Primetime Emmy Award winners",
        "Countries": "List of countries by population (United Nations)",
    }
    categories_options = list(categories.keys())
    choice = get_player_answer(question, categories_options)
    choice_name = categories_options[choice]
    return categories[choice_name]


if __name__ == "__main__":
    main()
