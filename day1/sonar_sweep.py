def count_increasing(measurements: list[int], lag: int = 1) -> int:
    return sum(measurements[n] > measurements[n - lag] for n in range(lag, len(measurements)))


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=1)
    data = transforms.numbers(puzzle.input_data)
    puzzle.answer_a = count_increasing(data)
    puzzle.answer_b = count_increasing(data, lag=3)
