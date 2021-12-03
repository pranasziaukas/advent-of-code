Command = tuple[str, int]


class Submarine:
    def __init__(self) -> None:
        self.horizontal_position = 0
        self.depth = 0

    def forward(self, distance: int) -> None:
        self.horizontal_position += distance

    def down(self, distance: int) -> None:
        self.depth += distance

    def up(self, distance: int) -> None:
        self.depth -= distance

    def control(self, commands: list[Command]) -> None:
        for action, value in commands:
            getattr(self, action)(value)


if __name__ == "__main__":
    from aocd import models, transforms

    def parse_commands(raw_commands: list[str]) -> list[Command]:
        return [(x, int(y)) for x, y in [x_y.split() for x_y in raw_commands]]

    puzzle = models.Puzzle(year=2021, day=2)
    data = parse_commands(transforms.lines(puzzle.input_data))

    submarine = Submarine()
    submarine.control(data)
    puzzle.answer_a = submarine.horizontal_position * submarine.depth
