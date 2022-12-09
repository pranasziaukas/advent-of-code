from enum import IntEnum


class Shape(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


CODE_SHAPES = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS,
}


def parse(raw_data: str) -> [(str, str)]:
    return [tuple(raw_shapes.split()) for raw_shapes in raw_data.splitlines()]


def find_shapes_simple(that_code: str, this_code: str) -> (Shape, Shape):
    shape_by_code = dict(
        CODE_SHAPES,
        **{
            "X": Shape.ROCK,
            "Y": Shape.PAPER,
            "Z": Shape.SCISSORS,
        }
    )
    return shape_by_code[that_code], shape_by_code[this_code]


def find_shapes_advanced(that_code: str, this_code: str) -> (Shape, Shape):
    that_shape = CODE_SHAPES[that_code]

    shift_by_code = {
        "X": -1,
        "Y": 0,
        "Z": 1,
    }
    this_shift = shift_by_code[this_code]
    this_shape = Shape((that_shape + this_shift) % 3)

    return that_shape, this_shape


def score(that_shape: Shape, this_shape: Shape) -> int:
    result = 0
    match (this_shape - that_shape) % 3:
        case 0:
            result = 3
        case 1:
            result = 6
    return result + this_shape + 1


def score_old(that_shape: Shape, this_shape: Shape) -> int:
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
    return result + this_shape + 1


if __name__ == "__main__":
    from aocd import models

    puzzle = models.Puzzle(year=2022, day=2)

    data_demo = parse(puzzle.example_data)
    assert sum(score(*find_shapes_simple(*x)) for x in data_demo) == 15
    assert sum(score(*find_shapes_advanced(*x)) for x in data_demo) == 12

    data = parse(puzzle.input_data)
    puzzle.answer_a = sum(score(*find_shapes_simple(*x)) for x in data)
    puzzle.answer_b = sum(score(*find_shapes_advanced(*x)) for x in data)
