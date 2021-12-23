from __future__ import annotations

from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Player:
    position: int
    score: int = 0

    def __add__(self, dice_result: int) -> Player:
        """Advance the player pawn."""
        position = (self.position + dice_result) % 10
        score = self.score + position + 1
        return Player(position, score)


PlayerPair = (Player, Player)


class PracticeGame:
    def __init__(self, player_pair: PlayerPair = None) -> None:
        self.players = list(player_pair) if player_pair else []
        self.dice = 0
        self.roll_count = 0

    def roll(self) -> int:
        """Roll dice."""
        if self.dice == 100:
            self.dice = 1
        else:
            self.dice += 1
        self.roll_count += 1
        return self.dice

    def take_turn(self, player: Player) -> Player:
        """Take one turn."""
        dice_result = sum(self.roll() for _ in range(3))
        return player + dice_result

    def play(self) -> None:
        """Play a full game."""

        # Player 1 starts first
        n = 0
        while all(player.score < 1000 for player in self.players):
            self.players[n] = self.take_turn(self.players[n])
            n = 1 - n


class DiracGame:
    def __init__(self) -> None:
        self.seen_winning_universes: dict[PlayerPair, (int, int)] = {}

    def winning_universes(self, player_pair: PlayerPair) -> (int, int):
        """Count wins in different universes."""
        x, y = 0, 0
        try:
            # Get a known result.
            x, y = self.seen_winning_universes[player_pair]
        except KeyError:
            player_next, player_last = player_pair
            if player_last.score >= 21:
                y += 1
            else:
                for dice_rolls in product([1, 2, 3], repeat=3):
                    new_player_pair = (player_last, player_next + sum(dice_rolls))
                    dy, dx = self.winning_universes(new_player_pair)
                    self.seen_winning_universes[new_player_pair] = (dy, dx)
                    x += dx
                    y += dy
        finally:
            return x, y


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=21)
    data = tuple(Player(int(line.split(" ")[-1]) - 1) for line in transforms.lines(puzzle.input_data))

    practice_game = PracticeGame(data)
    practice_game.play()
    puzzle.answer_a = practice_game.roll_count * min(p.score for p in practice_game.players)

    dirac_game = DiracGame()
    puzzle.answer_b = max(dirac_game.winning_universes(data))
