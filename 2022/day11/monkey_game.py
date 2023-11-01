import math
import operator
import re
from collections import deque
from dataclasses import dataclass
from typing import Callable

from aocd import models

OPERATORS = {"+": operator.add, "*": operator.mul}


@dataclass
class Monkey:
    items: deque[int]
    op: Callable[[int, int], int]
    op_value: int | None
    divisor: int
    pass_if_true: int
    pass_if_false: int
    inspections: int = 0

    def inspect(self, value: int) -> int:
        self.inspections += 1
        other_value = self.op_value if self.op_value else value
        return self.op(value, other_value)


def parse(raw_data: str) -> [Monkey]:
    prog = re.compile(
        r"Monkey (\d+):\s+Starting items: ((\d+(, )?)+)\s+"
        r"Operation: new = old ([+-/*]) (\d+|old)\s+"
        r"Test: divisible by (\d+)\s+"
        r"If true: throw to monkey (\d+)\s+"
        r"If false: throw to monkey (\d+)"
    )
    monkeys_raw = raw_data.split("\n\n")
    monkeys = []
    for monkey_raw in monkeys_raw:
        matches = prog.match(monkey_raw)

        # identifier = int(matches.group(1))
        items = deque(int(item) for item in (matches.group(2).split(",")))
        op = OPERATORS[matches.group(5)]
        op_value_raw = matches.group(6)
        op_value = int(op_value_raw) if op_value_raw.isdigit() else None
        divisor = int(matches.group(7))
        pass_if_true = int(matches.group(8))
        pass_if_false = int(matches.group(9))

        monkeys.append(Monkey(items, op, op_value, divisor, pass_if_true, pass_if_false))

    return monkeys


def play(monkeys: [Monkey], rounds: int = 1, reduction: bool = True) -> None:
    lcm = math.lcm(*[m.divisor for m in monkeys])

    for _ in range(rounds):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                item_before = monkey.items.popleft()
                item_after = monkey.inspect(item_before)
                if reduction:
                    item_after //= 3
                item_after %= lcm
                if item_after % monkey.divisor == 0:
                    monkeys[monkey.pass_if_true].items.append(item_after)
                else:
                    monkeys[monkey.pass_if_false].items.append(item_after)


def multiply_top_two_inspections(monkeys: [Monkey]) -> int:
    return operator.mul(*sorted([m.inspections for m in monkeys], reverse=True)[:2])


if __name__ == "__main__":
    puzzle = models.Puzzle(year=2022, day=11)

    monkeys_data_demo = parse(puzzle.example_data)
    play(monkeys_data_demo, rounds=20)
    assert multiply_top_two_inspections(monkeys_data_demo) == 10605

    monkeys_data = parse(puzzle.input_data)
    play(monkeys_data, rounds=20)
    puzzle.answer_a = multiply_top_two_inspections(monkeys_data)

    monkeys_data_demo_b = parse(puzzle.example_data)
    play(monkeys_data_demo_b, rounds=10000, reduction=False)
    assert multiply_top_two_inspections(monkeys_data_demo_b) == 2713310158

    monkeys_data_b = parse(puzzle.input_data)
    play(monkeys_data_b, rounds=10000, reduction=False)
    puzzle.answer_b = multiply_top_two_inspections(monkeys_data_b)
