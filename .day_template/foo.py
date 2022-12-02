def parse(raw_data: str) -> str:
    return raw_data


def bar(something: str) -> str:
    return something


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=0)

    data_demo = parse(puzzle.example_data)
    assert bar(data_demo) == 42

    data = transforms.lines(puzzle.input_data)
    puzzle.answer_a = bar("hello")
    puzzle.answer_b = bar("world")
