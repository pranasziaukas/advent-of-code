def parse(raw_data: str) -> [[int]]:
    return [[int(x) for x in raw_calories.splitlines()] for raw_calories in raw_data.split("\n\n")]


def sum_top(calories_journal: [[int]], how_many: int = 1) -> int:
    top_calories = sorted([sum(calories) for calories in calories_journal], reverse=True)
    return sum(top_calories[:how_many])


if __name__ == "__main__":
    from aocd import models

    puzzle = models.Puzzle(year=2022, day=1)

    data_demo = parse(puzzle.example_data)
    assert sum_top(data_demo) == 24000

    data = parse(puzzle.input_data)
    puzzle.answer_a = sum_top(data)
    puzzle.answer_b = sum_top(data, how_many=3)
