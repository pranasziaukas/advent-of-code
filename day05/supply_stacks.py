from collections import defaultdict
from dataclasses import dataclass
from string import ascii_uppercase

Stacks = {int: [str]}


@dataclass(frozen=True)
class Command:
    how_many: int
    source: int
    destination: int


class Stock:
    def __init__(self, initial_stacks: Stacks, reverse=True) -> None:
        self._stacks = initial_stacks.copy()
        self._reverse = reverse

    def do(self, command: Command) -> None:
        blocks = self._stacks[command.source][: command.how_many]
        if self._reverse:
            blocks = list(reversed(blocks))
        self._stacks[command.source] = self._stacks[command.source][command.how_many :]
        self._stacks[command.destination] = blocks + self._stacks[command.destination]

    def get_top(self) -> str:
        return "".join(x[0] for x in self._stacks.values() if len(x))


def parse(raw_data: str) -> (Stacks, [Command]):
    raw_stacks, raw_commands = raw_data.split("\n\n")

    stacks_lines = raw_stacks.splitlines()
    prep_stacks = defaultdict(list)
    for line in stacks_lines[:-1]:
        for n, x in enumerate(line):
            if x in ascii_uppercase:
                prep_stacks[n].append(x)
    stack_labels = [int(x) for x in stacks_lines[-1].split()]
    stacks = {stack_labels[n]: prep_stacks[prep_label] for n, prep_label in enumerate(sorted(prep_stacks.keys()))}

    commands = [Command(*[int(x) for x in y.split()[1::2]]) for y in raw_commands.splitlines()]

    return stacks, commands


if __name__ == "__main__":
    from aocd import models

    puzzle = models.Puzzle(year=2022, day=5)

    stacks_demo, commands_demo = parse(puzzle.example_data)
    stock_demo = Stock(stacks_demo)
    for cmd in commands_demo:
        stock_demo.do(cmd)
    assert stock_demo.get_top() == "CMZ"
    stock_demo_other = Stock(stacks_demo, reverse=False)
    for cmd in commands_demo:
        stock_demo_other.do(cmd)
    assert stock_demo_other.get_top() == "MCD"

    stacks, commands = parse(puzzle.input_data)
    stock = Stock(stacks)
    for cmd in commands:
        stock.do(cmd)
    puzzle.answer_a = stock.get_top()
    stock_other = Stock(stacks, reverse=False)
    for cmd in commands:
        stock_other.do(cmd)
    puzzle.answer_b = stock_other.get_top()
