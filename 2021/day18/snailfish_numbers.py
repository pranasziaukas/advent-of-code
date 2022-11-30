from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations
from math import ceil, floor


@dataclass
class SnailfishDigit:
    value: int
    depth: int

    def __str__(self) -> str:
        """String representation of a digit."""
        return f"{self.value}@{self.depth}"


class SnailfishNumber:
    def __init__(self, representation: str = "") -> None:
        """Create a Snailfish number based on its string representation."""
        self._digits = []

        digits = []
        depth = 0
        for x in representation:
            if x.isdigit():
                digits.append(SnailfishDigit(int(x), depth))
            elif x == "[":
                depth += 1
            elif x == "]":
                depth -= 1
        self.digits = digits

    @property
    def digits(self) -> [SnailfishDigit]:
        return self._digits[:]

    @digits.setter
    def digits(self, digits: [SnailfishDigit]) -> None:
        self._digits = digits
        self._reduce()

    def _reduce(self) -> None:
        def explode():
            for n, (x, y) in enumerate(zip(self._digits[:-1], self._digits[1:])):
                if x.depth < 5 or x.depth != y.depth:
                    continue
                if n > 0:
                    self._digits[n - 1].value += x.value
                if n < len(self._digits) - 2:
                    self._digits[n + 2].value += y.value
                new_digit = SnailfishDigit(0, x.depth - 1)
                self._digits = self._digits[:n] + [new_digit] + self._digits[n + 2 :]
                return True
            return False

        def split():
            for n, digit in enumerate(self._digits):
                if digit.value < 10:
                    continue
                new_digits = [
                    SnailfishDigit(floor(digit.value / 2), digit.depth + 1),
                    SnailfishDigit(ceil(digit.value / 2), digit.depth + 1),
                ]
                self._digits = self._digits[:n] + new_digits + self._digits[n + 1 :]
                return True
            return False

        while True:
            if explode():
                continue
            if not split():
                break

    def __add__(self, other: SnailfishNumber) -> SnailfishNumber:
        """Sum of two numbers."""
        number = SnailfishNumber()
        number.digits = [SnailfishDigit(d.value, d.depth + 1) for d in self.digits + other.digits]
        return number

    def __len__(self) -> int:
        """Magnitude of a number."""
        digits = self.digits
        # reduce to a single digit
        while len(digits) > 1:
            for n, (x, y) in enumerate(zip(digits[:-1], digits[1:])):
                if x.depth != y.depth:
                    continue
                new_digit = SnailfishDigit(3 * x.value + 2 * y.value, x.depth - 1)
                digits = digits[:n] + [new_digit] + digits[n + 2 :]
                break
        return digits[0].value

    def __str__(self) -> str:
        """String representation of a number."""
        return " ".join(str(digit) for digit in self.digits)

    def __eq__(self, other: SnailfishNumber) -> bool:
        """Check the equality of two numbers."""
        return str(self) == str(other)


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=18)
    numbers = [SnailfishNumber(x) for x in transforms.lines(puzzle.input_data)]
    puzzle.answer_a = len(sum(numbers[1:], start=numbers[0]))
    puzzle.answer_b = max(len(x + y) for x, y in permutations(numbers, 2))
