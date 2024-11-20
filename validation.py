from colorama import init, Fore, Style
init()
input_color = Fore.CYAN
error_color = Fore.RED
success_color = Fore.BLUE
highlight_color = Fore.MAGENTA

def get_rounds_number() -> int:
    """ define the round of numbers """
    max_round = 10
    while True:
        num_rounds = input(input_color +
            f"How many rounds you want to play? {max_round} is today's limit: "
        + Style.RESET_ALL)
        if num_rounds.isdigit():
            num_rounds = int(num_rounds)
            if num_rounds == 0:
                print(error_color + "It's fun. Try one round at least" + Style.RESET_ALL)
            elif num_rounds > max_round:
                print(error_color + f"Sorry, the maximum number of checks are: {max_round}" + Style.RESET_ALL)
            else:
                break
        else:
            print(error_color + "Nice try :) Try again & use a number" + Style.RESET_ALL)
    return num_rounds


def get_player_number() -> int:
    """ define the number of players """
    max_players = 8
    while True:
        num_players = input(input_color +
        f"How many players are hunting the truth? Only {max_players} fact checkers are allowed: "
        + Style.RESET_ALL)
        if num_players.isdigit():
            num_players = int(num_players)
            if num_players == 0:
                print(error_color + "No one? Seriously?" + Style.RESET_ALL)
                continue
            if num_players > max_players:
                print(error_color +
                f"Sorry but only {max_players} fact checkers care allowed to uncover the truth"
                + Style.RESET_ALL)
                continue
            return num_players
        else:
            print(error_color + "Nice try :) Try again by using a number" + Style.RESET_ALL)


def get_player_name(player_number, players) -> str:
    """ enter the player names """
    while True:
        player_name = input(input_color +
            f"Enter the name of Player {player_number}: "
        + Style.RESET_ALL).strip()
        if (
            len(player_name) < 1
        ):
            print(error_color + "This is a bit short for a name, isn't it?" + Style.RESET_ALL)
            continue
        if len(player_name) > 20:
            print(error_color + "This is a bit long for a name, isn't it?" + Style.RESET_ALL)
            continue

        player_names = [player.name for player in players.values()]
        if player_name in player_names:
            print(error_color + "Someone was faster. That name is already taken" + Style.RESET_ALL)
            continue
        return player_name
