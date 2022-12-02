from enum import IntEnum


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def parse(raw_data: str) -> [(Shape, Shape)]:
    shape_by_code = {
        "A": Shape.ROCK,
        "X": Shape.ROCK,
        "B": Shape.PAPER,
        "Y": Shape.PAPER,
        "C": Shape.SCISSORS,
        "Z": Shape.SCISSORS,
    }
    return [tuple(shape_by_code[x] for x in raw_shapes.split()) for raw_shapes in raw_data.splitlines()]


def score(that_shape: Shape, this_shape: Shape) -> int:
    result = 0
    if that_shape == this_shape:
        result = 3
    elif (
        this_shape == Shape.ROCK
        and that_shape == Shape.SCISSORS
        or this_shape == Shape.PAPER
        and that_shape == Shape.ROCK
        or this_shape == Shape.SCISSORS
        and that_shape == Shape.PAPER
    ):
        result = 6
    return result + this_shape


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2022, day=2)

    data_demo = parse(puzzle.example_data)
    assert sum(score(*x) for x in data_demo) == 15

    data = parse(puzzle.input_data)
    puzzle.answer_a = sum(score(*x) for x in data)
