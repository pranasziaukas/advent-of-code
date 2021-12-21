from dataclasses import dataclass
from re import search


@dataclass
class Velocity:
    x: int
    y: int

    def next(self) -> None:
        self.x = max(0, self.x - 1)
        self.y -= 1


@dataclass
class Position:
    velocity: Velocity
    x: int = 0
    y: int = 0

    def next(self) -> None:
        self.x += self.velocity.x
        self.y += self.velocity.y
        self.velocity.next()


@dataclass
class ProbeLauncher:
    min_x: int
    max_x: int
    min_y: int
    max_y: int

    def __post_init__(self) -> None:
        # Aiming to cover sensible cases.
        assert self.min_x > 0
        assert self.max_x > 0
        assert self.min_y < 0

        # Assuming `dy > 0`, trajectory will pass `y = 0` for the first time at `y' = -dy - 1`.
        # `dy = -(min_y + 1)` is the optimal solution.
        # The apex `y` is then the sum of an arithmetic progression:
        self.apex_y = self.min_y * (self.min_y + 1) // 2
        self.velocities = self._find_velocities()

    def _find_velocities(self) -> [Velocity]:
        velocities = []
        for dx in range(self.max_x + 1):
            for dy in range(self.min_y, -self.min_y):
                probe_position = Position(Velocity(dx, dy))
                while probe_position.x <= self.max_x and probe_position.y >= self.min_y:
                    if probe_position.x >= self.min_x and probe_position.y <= self.max_y:
                        velocities.append(probe_position.velocity)
                        break
                    probe_position.next()
        return velocities


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=17)
    data = transforms.lines(puzzle.input_data)[0]
    boundaries = map(int, search(r"x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", data).groups())
    probe_launcher = ProbeLauncher(*boundaries)
    puzzle.answer_a = probe_launcher.apex_y
    puzzle.answer_b = len(probe_launcher.velocities)
