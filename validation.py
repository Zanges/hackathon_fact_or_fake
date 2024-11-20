from colorama import Style
from colors import INPUT_COLOR, ERROR_COLOR




def get_rounds_number(max_round: int = 10) -> int:
    """define the round of numbers"""
    if max_round < 1:
        raise ValueError("max_round must be at least 1")

    while True:
        num_rounds = input(
            INPUT_COLOR
            + f"How many rounds you want to play? {max_round} is today's limit: "
            + Style.RESET_ALL
        )
        if num_rounds.isdigit():
            num_rounds = int(num_rounds)
            if num_rounds == 0:
                print(
                    ERROR_COLOR + "It's fun. Try one round at least" + Style.RESET_ALL
                )
            elif num_rounds > max_round:
                print(
                    ERROR_COLOR
                    + f"Sorry, the maximum number of checks are: {max_round}"
                    + Style.RESET_ALL
                )
            else:
                break
        else:
            print(
                ERROR_COLOR + "Nice try :) Try again & use a number" + Style.RESET_ALL
            )
    return num_rounds


def get_player_number(max_players: int = 8) -> int:
    """define the number of players"""
    if max_players < 1:
        raise ValueError("max_players must be at least 1")

    while True:
        num_players = input(
            INPUT_COLOR
            + f"How many players are hunting the truth? Only {max_players} fact checkers are allowed: "
            + Style.RESET_ALL
        )
        if num_players.isdigit():
            num_players = int(num_players)
            if num_players == 0:
                print(ERROR_COLOR + "No one? Seriously?" + Style.RESET_ALL)
                continue
            if num_players > max_players:
                print(
                    ERROR_COLOR
                    + f"Sorry but only {max_players} fact checkers care allowed to uncover the truth"
                    + Style.RESET_ALL
                )
                continue
            return num_players
        else:
            print(
                ERROR_COLOR
                + "Nice try :) Try again by using a number"
                + Style.RESET_ALL
            )


def get_player_name(player_number, players) -> str:
    """enter the player names"""
    while True:
        player_name = input(
            INPUT_COLOR
            + f"Enter the name of Player {player_number}: "
            + Style.RESET_ALL
        ).strip()
        if len(player_name) < 1:
            print(
                ERROR_COLOR
                + "This is a bit short for a name, isn't it?"
                + Style.RESET_ALL
            )
            continue
        if len(player_name) > 20:
            print(
                ERROR_COLOR
                + "This is a bit long for a name, isn't it?"
                + Style.RESET_ALL
            )
            continue

        player_names = [player.name for player in players.values()]
        if player_name in player_names:
            print(
                ERROR_COLOR
                + "Someone was faster. That name is already taken"
                + Style.RESET_ALL
            )
            continue
        return player_name
