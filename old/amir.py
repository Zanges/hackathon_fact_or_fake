# from colorama import Fore
# from giorgio import get_random_article_text
# from lea import get_passage
# from phil_amir import run_question
# from player import Player
# from utils import clear_terminal
# from zanges_lea import get_fake_passage
# #from validation import get_player_number, get_rounds_number
#
# article_text = get_passage()
# fake_passage = get_fake_passage()
#
# def main() -> None:
#     game_mode = input("Single-Player(sp) or Multi-Player(mp)")
#     multiplayer = True if game_mode == "mp" else False
#
#     difficulty = select_difficulty()
#
#     if multiplayer:
#         run_multiplayer(difficulty)
#     else:
#         run_game(difficulty)
#     clear_terminal()
#     clear_terminal()
#     print('after clear')
#
#     # process winner(players)
#
# def select_difficulty():
#     print("Choose difficulty level:")
#     print("1. Easy")
#     print("2. Medium")
#     print("3. Hard")
#     while True:
#         choice = input("Enter the number of your choice (1/2/3): ").strip()
#         if choice == "1":
#             return "easy"
#         elif choice == "2":
#             return "medium"
#         elif choice == "3":
#             return "hard"
#         else:
#             print("Invalid choice. Please choose 1, 2, or 3.")
#
#
# def run_game(difficulty):
#     print(f"Multiplayer mode started on {difficulty.capitalize()} difficulty!")
#     return run_question(fake_passage, article_text)
#
#
# def run_multiplayer(difficulty):
#     print(f"Single-player mode started on {difficulty.capitalize()} difficulty!")
#     total_players = int(input("how many players?: "))
#     total_rounds = int(input("how many rounds?: "))
#
#     players = {}
#     for i in range(1, total_players + 1):
#         player_name = input("What is your username?: ")
#         players[f"player{i}"] = Player(player_name)
#
#     for game_round in range(1, total_rounds + 1):
#         for player in players.values():
#             current_player = player
#
#             print(f"Round: {game_round} Player: {current_player.name}")
#
#             score = run_game(difficulty)
#
#
#             current_player.update_score(score)
#
#     for player in players.values():
#         print(player.name, player.score)
#
#
# if __name__ == "__main__":
#     main()
import textwrap
from colorama import Fore, Style


article_1 = """Nisi incididunt reprehenderit cillum enim ad tempor et reprehenderit sit eiusmod veniam occaecat mollit cillum eu velit elit cupidatat qui duis cupidatat eu. Aute et est labore. Labore anim aliquip culpa incididunt velit amet."""
article_2 = """Commodo laborum laboris laborum cillum consequat sit nostrud laboris. Amet dolor eiusmod magna ad nulla. Magna anim ex dolor laborum non sint laborum qui. Mollit amet nostrud amet Lorem esse. Labore anim aliquip culpa incididunt velit amet."""


column_width = 50
article_1_wrapped = textwrap.wrap(article_1, width=column_width)
article_2_wrapped = textwrap.wrap(article_2, width=column_width)


max_lines = max(len(article_1_wrapped), len(article_2_wrapped))
article_1_wrapped += [""] * (max_lines - len(article_1_wrapped))
article_2_wrapped += [""] * (max_lines - len(article_2_wrapped))


print("Article 1".ljust(column_width) + " | " + "Article 2")
print(Fore.RED + "-" * column_width + "-+-" + "-" * column_width + Style.RESET_ALL)


for line1, line2 in zip(article_1_wrapped, article_2_wrapped):
    print(line1.ljust(column_width) + " | " + line2)
