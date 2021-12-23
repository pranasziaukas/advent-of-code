from collections import namedtuple
from re import findall

Cube = namedtuple("Cube", ["x", "y", "z"])


class Reactor:
    def __init__(self):
        self.cubes: {Cube} = set()

    def execute(self, command: str, limit: int = None) -> None:
        is_on = command.startswith("on")
        coords = list(map(int, findall(r"-?\d+", command)))

        if limit and not all(-limit <= coord <= limit for coord in coords):
            return

        for x in range(coords[0], coords[1] + 1):
            for y in range(coords[2], coords[3] + 1):
                for z in range(coords[4], coords[5] + 1):
                    if is_on:
                        self.cubes.add(Cube(x, y, z))
                    else:
                        self.cubes.discard(Cube(x, y, z))

    def __len__(self) -> int:
        return len(self.cubes)


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=22)
    data = transforms.lines(puzzle.input_data)

    reactor = Reactor()
    for line in data:
        reactor.execute(line, limit=50)
    puzzle.answer_a = len(reactor)
