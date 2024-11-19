# bunt!

def get_rounds_number() -> int:
    """ """
    MAX_ROUND = 10
    while True:
        num_rounds = input(
            f"How many rounds you want to play? {MAX_ROUND} rounds max: "
        )
        if num_rounds.isdigit():
            num_rounds = int(num_rounds)
            if num_rounds == 0:
                print("It's fun. Try one round at least")
            elif num_rounds > MAX_ROUND:
                print(f"Sorry, the maximum number of rounds is {MAX_ROUND}")
            else:
                break
        else:
            print("Please enter a valid number")
    return num_rounds


def get_player_number() -> int:
    """ """
    MAX_PLAYERS = 8
    while True:
        num_players = input(
            f"How many players are joining the game? {MAX_PLAYERS} players max: "
        )
        if num_players.isdigit():
            num_players = int(num_players)
            if num_players == 0:
                print("At least one person should play this game")
                continue
            if num_players > MAX_PLAYERS:
                print(f"Sorry, the maximum number of players is {MAX_PLAYERS}")
                continue
            return num_players
        else:
            print("Please enter a valid number")


def get_player_name(player_number, players) -> str:
    while True:
        player_name = input(
            f"Enter the name of Player{player_number}: "
        ).strip()
        if (
            len(player_name) < 1
        ):  # I didn't catch nums & 1-letters for a reason. can be changed
            print("This is a bit short for a name, isn't it?")
            continue
        if len(player_name) > 20:
            print("This is a bit long for a name, isn't it?")
            continue

        player_names = [player.name for player in players.values()]
        if player_name in player_names:
            print("That name is already taken")
            continue
        return player_name
