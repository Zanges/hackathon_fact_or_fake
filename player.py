class Player:
    COLORS = ("red", "green", "blue", "green")
    color_index = 0

    def __init__(self, name) -> None:
        self.name = name
        self.color = self.get_color()
        self.score = 0
        self.scored_in_a_row = 0
        self.has_a_run = self.scored_in_a_row > 2
        self.has_crash = True


    def update_score(self, score) -> None:
        if not score:
            self.scored_in_a_row = 0
        else:
            self.score += score
            self.scored_in_a_row += 1
        if self.has_a_run:
            self.score += 3

    @classmethod
    def get_color(cls) -> str:
        # Get the current color based on the index
        color = cls.COLORS[cls.color_index]
        # Increment the index and wrap around if it exceeds the length of COLORS
        cls.color_index = (cls.color_index + 1) % len(cls.COLORS)
        return color

    def __repr__(self) -> str:
        return (
            f"Player(name={self.name}, color={self.color}, score={self.score})"
        )


# player_1 = Player("Phil")
# print(player_1)
# player_2 = Player("Paul")
# print(player_2)
# player_3 = Player("Lea")
# print(player_3)
