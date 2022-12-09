from aocd import models, transforms

Instruction = (str, int)

LENGTH = 10
DELTA = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def parse(raw_data: str) -> [Instruction]:
    def parse_instruction(direction: str, steps_str: str) -> Instruction:
        return direction, int(steps_str)

    return [parse_instruction(*line.split()) for line in transforms.lines(raw_data)]


def sign(x: int) -> int:
    return (x > 0) - (x < 0)


class Rope:
    def __init__(self) -> None:
        self.knots = [(0, 0)] * LENGTH
        self.seen1 = {(0, 0)}
        self.seen9 = {(0, 0)}

    def move(self, instruction: Instruction) -> None:
        direction, steps = instruction
        for _ in range(steps):
            x, y = self.knots[0]
            dx, dy = DELTA[direction]
            self.knots[0] = x + dx, y + dy

            for n in range(LENGTH - 1):
                x, y = self.knots[n]
                tx, ty = self.knots[n + 1]
                dx, dy = x - tx, y - ty

                if dx**2 + dy**2 >= 4:
                    self.knots[n + 1] = tx + sign(dx), ty + sign(dy)

            self.seen1.add(tuple(self.knots[1]))
            self.seen9.add(tuple(self.knots[9]))


if __name__ == "__main__":
    puzzle = models.Puzzle(year=2022, day=9)

    data = parse(puzzle.input_data)
    rope = Rope()
    for data_instruction in data:
        rope.move(data_instruction)

    puzzle.answer_a = len(rope.seen1)
    puzzle.answer_b = len(rope.seen9)
