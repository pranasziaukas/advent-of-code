DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def find_line_number(line: str) -> int:
    first = (9999999, 0)
    last = (0, 0)
    for n, digit in enumerate(DIGITS, 1):
        if digit in line:
            first = min(first, (line.index(digit), n))
            last = max(last, (line.rindex(digit), n))
        str_n = str(n)
        if str_n in line:
            first = min(first, (line.index(str_n), n))
            last = max(last, (line.rindex(str_n), n))
    return 10 * first[1] + last[1]


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2023, day=1)
    data_demo = transforms.lines(puzzle.example_data)
    assert sum(find_line_number(x) for x in data_demo) == 142

    data = transforms.lines(puzzle.input_data)
    puzzle.answer_a = sum(find_line_number(x) for x in data)
    puzzle.answer_b = sum(find_line_number(x) for x in data)
