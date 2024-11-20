from giorgio import get_random_article_text
from lea import get_passage
from game_logic import run_question
from player import Player
from utils import clear_console
from pretty_print import header

# from zanges import get_fake_passage
#from validation import get_player_number, get_rounds_number
article_text = """Donkey Kong Country[b] is a 1994 platform game developed by Rare and published by Nintendo for the Super Nintendo Entertainment System (SNES). It is a reboot of Nintendo's Donkey Kong franchise and follows the gorilla Donkey Kong and his nephew Diddy Kong as they set out to recover their stolen banana hoard from the crocodile King K. Rool and his army, the Kremlings. The single-player traverses 40 side-scrolling levels as they jump between platforms and avoid obstacles. They collect items, ride minecarts and animals, defeat enemies and bosses, and find secret bonus stages. In multiplayer modes, two players work cooperatively or race."""

fake_passage = """Monkey Madness Jungle Quest is a 1994 tree-swinging adventure developed by Bizarre and published by Nintondo for the Super Fun Console (SFC). It is a reinvention of Nintondo's Monkey Mayhem franchise and follows the orangutan Chunky Kong and his niece, Ditzy Kong, as they embark on a mission to reclaim their stolen coconut stash from the nefarious iguana Lord L. Reptile and his gang, the Slitherlings. The single-player embarks on a journey through 42 jungle-packed levels, swinging between vines and dodging falling coconuts. They gather shiny gems, ride unicycles and exotic birds, defeat strange creatures and colossal bosses, and uncover hidden treasure caves. In multiplayer modes, two players can either join forces or compete in a banana-collecting showdown."""


def main() -> None:
    header()
    game_mode = input("Single-Player(sp) or Multi-Player(mp) \n")
    multiplayer = True if game_mode == "mp" else False

    if multiplayer:
        run_multiplayer()
    else:
        clear_console()
        run_game()

    # process winner(players)

def run_game() -> int:
    return run_question(fake_passage, article_text)


def run_multiplayer() -> None:
    total_players = int(input("how many players?: "))
    total_rounds = int(input("how many rounds?: "))

    players = {}
    for i in range(1, total_players + 1):
        player_name = input("What is your username?: ")
        players[f"player{i}"] = Player(player_name)

    for game_round in range(1, total_rounds + 1):
        for player in players.values():
            current_player = player

            clear_console()
            print(f"Round: {game_round} Player: {current_player.name}")

            score = run_game()


            current_player.update_score(score)

    for player in players.values():
        print(player.name, player.score)


if __name__ == "__main__":
    main()
