from colorama import init, Fore, Style
from player import Player
init()
podium_color = Fore.YELLOW



def display_podium(players: dict[str, Player]):
    """Displays a podium for the happy winners using a grid structure."""
    sorted_scores = sorted(players.values(), key=lambda x: x.score, reverse=True)


    scale_factor = 10
    podium_info = [(player.name, player.score // scale_factor, player.score) for player in sorted_scores]
    max_height = max(height for _, height, _ in podium_info)

    grid = []
    for level in range(max_height + 1):
        row = []
        for _, height, _ in podium_info:
            if max_height - level < height:
                row.append(podium_color + "|      |" + Style.RESET_ALL)
            elif max_height - level == height:
                row.append(podium_color + "@******@" + Style.RESET_ALL)
            else:
                row.append("        ")
        grid.append(row)



    for row in grid:
        print("  ".join(row))


    score_row = [f"{score:^8}" for _, _, score in podium_info]
    print("  ".join(score_row))


    name_row = [f"{name.center(8)}" for name, _, _ in podium_info]
    print("  ".join(name_row))



# scores = {
#     "Phillip": 60,
#     "Zanges": 30,
#     "Lea": 10,
#     "Amir": 40,
#     "Gorge": 20,
#     "Bob": 0
# }
#
# display_podium(scores)