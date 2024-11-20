import random

from colorama import Fore, Style, init

from ai_api import get_fake_passage
from crashes import wants_crash, choose_crash
from player import Player
from pretty_print import header, display_player_scores_horizontally, print_two_paragraphs_side_by_side, closing_screen, final, get_player_answer
from request_wiki_categories import get_random_valid_title, get_article_content
from validation import get_player_number, get_rounds_number, get_player_name

init(autoreset=True)

MAX_RETRIES = 3


def run_question(fake_passage, passage, round_str, players):
    """Runs a single question round where players identify the fake passage."""
    header()
    print(round_str)
    display_player_scores_horizontally(players)
    print()

    passages = [passage, fake_passage]
    random.shuffle(passages)

    shortened_passages = []
    for passage in passages:
        sentences = passage.split(". ")
        shortened_passages.append(". ".join(sentences[:6]) + ".")

    print_two_paragraphs_side_by_side(
        "Paragraph 1", shortened_passages[0], "Paragraph 2", shortened_passages[1]
    )
    print()

    while True:
        try:
            question = Fore.LIGHTGREEN_EX + "Which paragraph is fake?:"
            options = ["Paragraph", "Paragraph"]
            user_input = get_player_answer(question, options)
            print(user_input)
            if (user_input == 0 and passages[0] == fake_passage) or (
                user_input == 1 and passages[1] == fake_passage
            ):
                print(Fore.GREEN + Style.BRIGHT + "Correct! You earn 10 points")
                return 10
            elif user_input in [0, 1]:
                print(Fore.RED + Style.BRIGHT + "Incorrect! Better luck next time ...")
                return 0
            else:
                print(Fore.RED + "Invalid input. Please choose only 1 or 2")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number (1 or 2)")


def run_round(difficulty, category, round_str, players, crash=False) -> int:
    """Executes a single round of the game, fetching article content and running questions."""
    success = False
    tries = 0
    while not success and tries < MAX_RETRIES:
        try:
            title = get_random_valid_title(category)
            title, article_content = get_article_content(title)
            fake_passage = get_fake_passage(article_content, difficulty)
            success = True
        except ValueError:  # when the article is empty
            pass
        except Exception as e:
            print(e)
        tries += 1
    if not success:
        raise Exception("Failed to fetch article content")

    if crash:
        crash_function = choose_crash()
        crashed_fake_passage = crash_function(fake_passage)
        crashed_article_text = crash_function(article_content)
        return run_question(
            crashed_fake_passage, crashed_article_text, round_str, players
        )
    return run_question(fake_passage, article_content, round_str, players)


def run_game(difficulty, category) -> None:
    """Manages the entire game, iterating through rounds and updating player scores."""
    total_players = get_player_number()
    total_rounds = get_rounds_number()
    crash = False

    # create player objects
    players = {}
    for i in range(1, total_players + 1):
        player_name = get_player_name(i, players)
        players[f"player{i}"] = Player(player_name)

    for game_round in range(1, total_rounds + 1):
        for player in players.values():
            current_player = player

            round_str = Fore.BLUE + f"   Round: {game_round}/{total_rounds}"
            round_str += (
                current_player.color + f"  ──── This is {current_player.name}'s turn ────  "
            )
            round_str += Fore.BLUE + f"Score: {current_player.score}"
            round_str_len = len(round_str.replace(Fore.BLUE, "").replace(Fore.RED, ""))
            seperator =  "─" * (round_str_len + 3)
            round_str += "\n" + seperator

            if crash:
                score = run_round(difficulty, category, round_str, players, crash=True)
                crash = False
            else:
                score = run_round(difficulty, category, round_str, players)

            if total_rounds > 1:
                if (
                    total_players > 1
                    and current_player.has_crash
                    and game_round < total_rounds
                    and wants_crash()
                ) or (
                    game_round == total_rounds - 1
                    and current_player.has_crash
                    and total_players > 1
                ):
                    crash = True
                    current_player.has_crash = False

            current_player.update_score(score)

    
    final(players)
    input("Press Enter to continue!")
    closing_screen()
