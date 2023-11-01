from aocd import models, transforms
from textwrap import wrap

WIDTH = 40


class RayTube:
    def __init__(self) -> None:
        self.x = 1
        self.cycle = 1

        self.strengths = 0
        self._grid = ""

    @property
    def strength(self) -> int:
        return self.cycle * self.x

    @property
    def grid(self) -> str:
        return "\n".join(wrap(self._grid, WIDTH))

    def next_cycle(self) -> None:
        self._grid += "#" if abs(self.x - (self.cycle - 1) % WIDTH) <= 1 else " "
        if self.cycle in (20, 60, 100, 140, 180, 220):
            self.strengths += self.strength
        self.cycle += 1

    def do(self, operation: str) -> None:
        match operation.split():
            case ["noop"]:
                self.next_cycle()
            case ["addx", x]:
                self.next_cycle()
                self.next_cycle()
                self.x += int(x)


if __name__ == "__main__":

    puzzle = models.Puzzle(year=2022, day=10)

    ops_demo = transforms.lines(puzzle.example_data)
    tube_demo = RayTube()
    for op in ops_demo:
        tube_demo.do(op)
    assert tube_demo.x == -1

    ops = transforms.lines(puzzle.input_data)
    tube = RayTube()
    for op in ops:
        tube.do(op)

    puzzle.answer_a = tube.strengths
    print(tube.grid)
