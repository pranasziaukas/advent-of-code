from dataclasses import dataclass


@dataclass(frozen=True)
class Game:
    red: int
    green: int
    blue: int

    def has(self, color: str) -> int:
        return self.__dict__[color]


GAME = Game(12, 13, 14)


def is_possible(line: str) -> int:
    title, facts_raw = line.split(": ")
    facts = facts_raw.split("; ")
    for fact in facts:
        observations = fact.split(", ")
        for observation in observations:
            value, color = observation.split(" ")
            if GAME.has(color) < int(value):
                return 0
    return int(title.split(" ")[1])


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2023, day=2)

    data_demo = transforms.lines(puzzle.example_data)
    assert sum(is_possible(x) for x in data_demo) == 8

    data = transforms.lines(puzzle.input_data)
    puzzle.answer_a = sum(is_possible(x) for x in data)
