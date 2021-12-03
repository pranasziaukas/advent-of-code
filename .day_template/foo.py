def bar(something: int) -> int:
    return something


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=0)
    data = transforms.numbers(puzzle.input_data)
    puzzle.answer_a = bar(1)
    puzzle.answer_b = bar(2)
