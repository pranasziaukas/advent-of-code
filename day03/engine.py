from math import prod
from collections import defaultdict


def adjacent_symbols(grid: [str], y: int, start_x: int, max_y: int, max_x: int) -> ([int], defaultdict[list]):
    line = grid[y]
    above = grid[y - 1] if y > 0 else []
    below = grid[y + 1] if y < max_y - 1 else []
    gears = []
    has_symbol = False

    for c in range(max(0, start_x - 1), max_x):
        if above and above[c] not in '0123456789.':
            has_symbol = True
            if above[c] == '*':
                gears.append((y - 1, c))

        if below and below[c] not in '0123456789.':
            has_symbol = True
            if below[c] == '*':
                gears.append((y + 1, c))

        if not line[c].isdigit():
            has_symbol |= line[c] != '.'
            if line[c] == '*':
                gears.append((y, c))

            if c > start_x:
                break

    return has_symbol, gears


def extract_number(row, start_x, max_x):
    end = start_x + 1
    while end < max_x and row[end].isdigit():
        end += 1

    return int(row[start_x:end])


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2023, day=3)
    data = transforms.lines(puzzle.input_data)
    height, width = len(data), len(data[0])

    answer1 = answer2 = 0
    gears = defaultdict(list)

    for y, row in enumerate(data):
        x = 0

        while x < width:
            while x < width and not row[x].isdigit():
                x += 1

            if x >= width:
                break

            adj_to_symbol, adj_gears = adjacent_symbols(data, y, x, height, width)

            if adj_to_symbol:
                number = extract_number(row, x, width)
                answer1 += number

                for rc in adj_gears:
                    gears[rc].append(number)

            while x < width and row[x].isdigit():
                x += 1

    puzzle.answer_a = answer1

    answer2 = sum(map(prod, filter(lambda x: len(x) == 2, gears.values())))
    puzzle.answer_b = answer2
