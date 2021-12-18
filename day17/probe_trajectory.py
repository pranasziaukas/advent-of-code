from collections import namedtuple
from dataclasses import dataclass
from re import search


Point = namedtuple("Point", ["x", "y"])


@dataclass
class ProbeLauncher:
    min_x: int
    max_x: int
    min_y: int
    max_y: int

    def __post_init__(self) -> None:
        # Assuming `dy > 0`, trajectory will pass `y = 0` for the first time at `y' = -dy - 1`.
        # `dy = -(min_y + 1)` is the optimal solution.
        # The apex `y` is then the sum of an arithmetic progression:
        self.apex_y = self.min_y * (self.min_y + 1) // 2


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=17)
    data = transforms.lines(puzzle.input_data)[0]
    boundaries = map(int, search("x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", data).groups())
    probe_launcher = ProbeLauncher(*boundaries)
    puzzle.answer_a = probe_launcher.apex_y
