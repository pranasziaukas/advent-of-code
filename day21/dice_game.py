from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Player:
    position: int
    score: int = 0

    def __add__(self, dice_result: int) -> Player:
        """Advance the player pawn."""
        position = (self.position + dice_result) % 10
        score = self.score + position + 1
        return Player(position, score)


class Game:
    def __init__(self, player_one: Player, player_two: Player) -> None:
        # Next = playing next or catching up.
        self.player_next = player_one
        # Last = played last or already won.
        self.player_last = player_two

        self.dice = 0
        self.roll_count = 0

    def roll(self) -> int:
        if self.dice == 100:
            self.dice = 1
        else:
            self.dice += 1
        self.roll_count += 1
        return self.dice

    def take_turn(self) -> None:
        dice_result = self.roll() + self.roll() + self.roll()
        self.player_next += dice_result
        self.player_next, self.player_last = self.player_last, self.player_next

    def play(self) -> None:
        while self.player_last.score < 1000:
            self.take_turn()


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=21)
    position1, position2 = [int(line.split(" ")[-1]) - 1 for line in transforms.lines(puzzle.input_data)]
    game = Game(Player(position1), Player(position2))

    game.play()
    puzzle.answer_a = game.roll_count * game.player_next.score
