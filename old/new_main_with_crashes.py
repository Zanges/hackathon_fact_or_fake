from giorgio import get_random_article_text
# from lea import get_passage
from phil_amir import run_question
from player import Player
# from utils import clear_terminal
import crashes
# from zanges import get_fake_passage

from validation import get_player_number, get_rounds_number, get_player_name

article_text = """Donkey Kong Country[b] is a 1994 platform game developed by Rare and published by Nintendo for the Super Nintendo Entertainment System (SNES). It is a reboot of Nintendo's Donkey Kong franchise and follows the gorilla Donkey Kong and his nephew Diddy Kong as they set out to recover their stolen banana hoard from the crocodile King K. Rool and his army, the Kremlings. The single-player traverses 40 side-scrolling levels as they jump between platforms and avoid obstacles. They collect items, ride minecarts and animals, defeat enemies and bosses, and find secret bonus stages. In multiplayer modes, two players work cooperatively or race."""

fake_passage = """Monkey Madness Jungle Quest is a 1994 tree-swinging adventure developed by Bizarre and published by Nintondo for the Super Fun Console (SFC). It is a reinvention of Nintondo's Monkey Mayhem franchise and follows the orangutan Chunky Kong and his niece, Ditzy Kong, as they embark on a mission to reclaim their stolen coconut stash from the nefarious iguana Lord L. Reptile and his gang, the Slitherlings. The single-player embarks on a journey through 42 jungle-packed levels, swinging between vines and dodging falling coconuts. They gather shiny gems, ride unicycles and exotic birds, defeat strange creatures and colossal bosses, and uncover hidden treasure caves. In multiplayer modes, two players can either join forces or compete in a banana-collecting showdown."""


def main() -> None:
    game_mode = input("Single-Player(sp) or Multi-Player(mp)")
    multiplayer = True if game_mode == "mp" else False

    if multiplayer:
        run_multiplayer()
    else:
        run_game()


def run_game(crash=False) -> int:
    if crash:
        crash_function = crashes.choose_crash()
        crashed_fake_passage = crash_function(fake_passage)
        crashed_article_text = crash_function(article_text)
    else:
        crashed_article_text = article_text
        crashed_fake_passage = fake_passage

    return run_question(crashed_fake_passage, crashed_article_text)


def run_multiplayer() -> None:
    total_players = get_player_number()  # int(input("how many players?: "))
    total_rounds = get_rounds_number()  # int(input("how many rounds?: "))
    crash = False

    players = {}
    for i in range(1, total_players + 1):
        player_name = get_player_name(
            i, players
        )  # input("What is your username?: ")
        players[f"player{i}"] = Player(player_name)

    for game_round in range(1, total_rounds + 1):
        for player in players.values():
            current_player = player

            print(f"Round: {game_round} Player: {current_player.name}")

            if crash:
                score = run_game(crash=True)
                crash = False
            else:
                score = run_game()

            if (
                total_players > 1
                and current_player.has_crash
                and game_round < total_rounds
                and crashes.wants_crash()
            ):
                crash = True
                current_player.has_crash = False

            current_player.update_score(score)

    winners = process_winners(players)

    for player in winners:
        print(player.name, player.score)


def process_winners(players):
    sorted_players = sorted(players.values(), key=lambda x: x.score, reverse=True)
    return sorted_players[:3]


if __name__ == "__main__":
    main()
