from colorama import Fore
from giorgio import get_random_article_text
from lea import get_passage
from phil_amir import run_question
from player import Player
from utils import clear_terminal
from zanges_lea import get_fake_passage
#from validation import get_player_number, get_rounds_number

article_text = get_passage()
fake_passage = get_fake_passage()

def main() -> None:
    game_mode = input("Single-Player(sp) or Multi-Player(mp)")
    multiplayer = True if game_mode == "mp" else False

    difficulty = select_difficulty()

    if multiplayer:
        run_multiplayer(difficulty)
    else:
        run_game(difficulty)
    clear_terminal()
    clear_terminal()
    print('after clear')

    # process winner(players)

def select_difficulty():
    print("Choose difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        choice = input("Enter the number of your choice (1/2/3): ").strip()
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def run_game(difficulty):
    print(f"Multiplayer mode started on {difficulty.capitalize()} difficulty!")
    return run_question(fake_passage, article_text)


def run_multiplayer(difficulty):
    print(f"Single-player mode started on {difficulty.capitalize()} difficulty!")
    total_players = int(input("how many players?: "))
    total_rounds = int(input("how many rounds?: "))

    players = {}
    for i in range(1, total_players + 1):
        player_name = input("What is your username?: ")
        players[f"player{i}"] = Player(player_name)

    for game_round in range(1, total_rounds + 1):
        for player in players.values():
            current_player = player

            print(f"Round: {game_round} Player: {current_player.name}")

            score = run_game(difficulty)


            current_player.update_score(score)

    for player in players.values():
        print(player.name, player.score)


if __name__ == "__main__":
    main()
