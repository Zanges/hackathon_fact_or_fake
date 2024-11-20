from colorama import init, Fore, Style
from player import Player
init()
podium_color = Fore.YELLOW



def display_podium(players: dict[str, Player]):
    """Displays a podium for the happy winners using a grid structure."""
    sorted_scores = sorted(players.values(), key=lambda x: x.score, reverse=True)


    scale_factor = 10
    podium_info = [(player.name, player.score // scale_factor, player.score, player.color) for player in sorted_scores]
    max_height = max(height for _, height, _, _ in podium_info)

    rank_colors = [Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX, Fore.YELLOW]
    default_color = Fore.LIGHTGREEN_EX

    grid = []
    for level in range(max_height + 1):
        row = []
        for i, (_, height, _, _) in enumerate(podium_info):
            color = rank_colors[i] if i < len(rank_colors) else default_color
            if max_height - level < height:
                row.append(color + "|      |" + Style.RESET_ALL)
            elif max_height - level == height:
                row.append(color + "@******@" + Style.RESET_ALL)
            else:
                row.append("        ")  #
        grid.append(row)


    for row in grid:
        print("  ".join(row))

    score_row = [
        f"{color}{str(score).center(8)}{Style.RESET_ALL}"
        for _, _, score, color in podium_info
    ]
    print("  ".join(score_row))

    name_row = [
        f"{color}{str(name).center(8)}{Style.RESET_ALL}"
        for name, _, _, color in podium_info
    ]
    print("  ".join(name_row))





def display_player_scores_vertically(players):
    """
    Displays each player's name, score, and stars in a vertivcal format
    """
    for player in players.values():
        stars = '*' * (player.score // 10)
        print(f"{player.color}{player.name:<10}{Style.RESET_ALL} {player.score:<3} {stars}")


# display_player_scores_vertically(players)
#
# print("\n")


def display_player_scores_horizontally(players):
    """
    Displays each player's name, score, and stars in a horizontal format
    """

    column_width = 15

    name_row = "  ".join(
        f"{player.color}{player.name:<{column_width}}{Style.RESET_ALL}" for player in players.values()
    )
    score_row = "  ".join(
        f"{player.color}{str(player.score):<{column_width}}{Style.RESET_ALL}" for player in players.values()
    )
    stars_row = "  ".join(
        f"{'*' * (player.score // 10):<{column_width}}" for player in players.values()
    )

    print(name_row)
    print(score_row)
    # print(stars_row)


# display_player_scores_horizontally(players)
