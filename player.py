""" Creates Player Object to store information of each Player. When a new Player is created it gets a color from COLORS.
Every Player has a name, color, score and the possibility to cast a crash once a round"""

from colorama import Fore


class Player:
    COLORS = (Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA)
    color_index = 0

    @classmethod
    def get_color(cls) -> str:
        # Get the current color based on the index
        color = cls.COLORS[cls.color_index]
        # Increment the index and wrap around if it exceeds the length of COLORS
        cls.color_index = (cls.color_index + 1) % len(cls.COLORS)
        return color

    def __init__(self, name) -> None:
        self.name = name
        self.color = self.get_color()
        self.score = 0
        self.scored_in_a_row = 0
        self.has_crash = True

    def update_score(self, score) -> None:
        if not score:
            self.scored_in_a_row = 0
        else:
            self.score += score

    def __repr__(self) -> str:
        return f"Player(name={self.name}, color={self.color}, score={self.score})"
