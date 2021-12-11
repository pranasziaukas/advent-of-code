from collections import deque


def get_error_score(entry: str) -> int:
    openers_closers = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    symbol_scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    queue = deque()
    for symbol in entry:
        if symbol in openers_closers.keys():
            queue.append(symbol)
        else:
            if openers_closers[queue.pop()] != symbol:
                return symbol_scores[symbol]
    return 0


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=10)
    data = transforms.lines(puzzle.input_data)

    scores = 0
    for data_entry in data:
        scores += get_error_score(data_entry)
    puzzle.answer_a = scores
