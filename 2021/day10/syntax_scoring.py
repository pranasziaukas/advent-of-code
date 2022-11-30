from collections import deque
from dataclasses import dataclass
from enum import Enum, auto


class Type(Enum):
    ERROR = auto()
    INCOMPLETE = auto()


@dataclass
class SyntaxScore:
    type: Type
    value: int


OPENERS_CLOSERS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def get_score(entry: str) -> SyntaxScore:
    """Get score of a known bad navigation subsystem entry."""
    queue = deque()

    # error checker
    error_scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    for symbol in entry:
        if symbol in OPENERS_CLOSERS.keys():
            queue.append(symbol)
        else:
            if OPENERS_CLOSERS[queue.pop()] != symbol:
                return SyntaxScore(Type.ERROR, error_scores[symbol])

    # no errors found, must be incomplete
    incomplete_scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    value = 0
    while queue:
        symbol = queue.pop()
        value *= 5
        value += incomplete_scores[OPENERS_CLOSERS[symbol]]
    return SyntaxScore(Type.INCOMPLETE, value)


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=10)
    data = transforms.lines(puzzle.input_data)

    error_value_total = 0
    incomplete_values = []
    for data_entry in data:
        score = get_score(data_entry)
        if score.type == Type.ERROR:
            error_value_total += score.value
        else:
            incomplete_values.append(score.value)
    # sum of all error scores
    puzzle.answer_a = error_value_total
    # median of all incomplete scores
    puzzle.answer_b = sorted(incomplete_values)[len(incomplete_values) // 2]
