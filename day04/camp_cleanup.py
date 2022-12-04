Interval = (int, int)


def parse(raw_data: str) -> [(Interval, Interval)]:
    return [tuple(tuple(int(z) for z in y.split("-")) for y in x.split(",")) for x in raw_data.splitlines()]


def contains(intervals: (Interval, Interval)) -> bool:
    (a_start, a_end), (b_start, b_end) = intervals
    return (a_start <= b_start and a_end >= b_end) or (b_start <= a_start and b_end >= a_end)


def overlaps(intervals: (Interval, Interval)) -> bool:
    (a_start, a_end), (b_start, b_end) = intervals
    return (a_start <= b_start <= a_end) or (b_start <= a_start <= b_end)


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2022, day=4)

    data_demo = parse(puzzle.example_data)
    assert sum(contains(x) for x in data_demo) == 2
    assert sum(overlaps(x) for x in data_demo) == 4

    data = parse(puzzle.input_data)
    puzzle.answer_a = sum(contains(x) for x in data)
    puzzle.answer_b = sum(overlaps(x) for x in data)
