from __future__ import annotations
from itertools import permutations
from math import ceil, floor
from typing import Iterator


class SnailfishDigit:
    def __init__(
        self, value: int, depth: int, previous: SnailfishDigit = None, succeeding: SnailfishDigit = None
    ) -> None:
        """Create a Snailfish digit."""
        self.value = value
        self.depth = depth
        self.succeeding = succeeding
        self.previous = previous

    def __repr__(self) -> str:
        """Representation of a digit."""
        return f"{'[' * self.depth} {self.value} {']' * self.depth}"


class SnailfishNumber:
    def __init__(self, representation: str) -> None:
        """Create a Snailfish number based on its string representation."""
        self._head = SnailfishNumber._get_head_digit(representation)
        needs_reduction = True
        while needs_reduction:
            needs_reduction = self._reduce()

    @staticmethod
    def _get_head_digit(representation: str) -> SnailfishDigit:
        """Parse a number and return its head digit."""
        head = tail = None
        depth = 0
        for x in representation:
            if x == "[":
                depth += 1
            elif x == "]":
                depth -= 1
            elif x.isdigit():
                digit = SnailfishDigit(int(x), depth, previous=tail)
                try:
                    tail.succeeding = digit
                except AttributeError:
                    head = digit
                finally:
                    tail = digit
        return head

    def _explode(self, digit: SnailfishDigit) -> None:
        """Explode a pair given its first digit."""
        first = digit
        second = digit.succeeding
        new_digit = SnailfishDigit(0, digit.depth - 1, previous=first.previous, succeeding=second.succeeding)
        try:
            first.previous.value += first.value
            first.previous.succeeding = new_digit
        except AttributeError:
            self._head = new_digit
        try:
            second.succeeding.value += second.value
            second.succeeding.previous = new_digit
        except AttributeError:
            pass

    def _split(self, digit: SnailfishDigit) -> None:
        """Split a digit."""
        first = SnailfishDigit(floor(digit.value / 2), digit.depth + 1, previous=digit.previous)
        second = SnailfishDigit(ceil(digit.value / 2), digit.depth + 1, previous=first, succeeding=digit.succeeding)
        first.succeeding = second
        try:
            digit.previous.succeeding = first
        except AttributeError:
            self._head = first
        try:
            digit.succeeding.previous = second
        except AttributeError:
            pass

    def _reduce(self) -> bool:
        """Reduce a number once and acknowledge the action."""
        for digit in self:
            if digit.depth > 4:
                self._explode(digit)
                return True
        for digit in self:
            if digit.value > 9:
                self._split(digit)
                return True
        return False

    def __iter__(self) -> Iterator[SnailfishDigit]:
        """Iterate over the digits."""
        digit = self._head
        while digit:
            yield digit
            digit = digit.succeeding

    def __str__(self) -> str:
        """String serialization of a number."""
        representation = ""
        depth = 0
        for digit in self:
            while depth < digit.depth:
                representation += "["
                depth += 1
            while depth > digit.depth:
                representation = representation[:-1] + "],"
                depth -= 1
            representation += f"{digit.value},"
            digit = digit.succeeding
        return representation[:-1] + "]" * depth

    def __repr__(self) -> str:
        """Representation of a number."""
        return f"SnailfishNumber({str(self)})"

    def __len__(self) -> int:
        """Magnitude of a number."""
        value_depths = [(digit.value, digit.depth) for digit in self]
        while len(value_depths) > 1:
            for i, ((this_value, this_depth), (that_value, that_depth)) in enumerate(
                zip(value_depths, value_depths[1:])
            ):
                if this_depth != that_depth:
                    continue
                val = this_value * 3 + that_value * 2
                value_depths = value_depths[:i] + [(val, this_depth - 1)] + value_depths[i + 2 :]
                break
        return value_depths[0][0]

    def __add__(self, other: SnailfishNumber) -> SnailfishNumber:
        """Sum of two numbers."""
        return SnailfishNumber(f"[{str(self)},{str(other)}]")

    def __eq__(self, other: SnailfishNumber) -> bool:
        """Check the equality of two numbers."""
        return str(self) == str(other)


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=18)
    numbers = [SnailfishNumber(x) for x in transforms.lines(puzzle.input_data)]
    puzzle.answer_a = len(sum(numbers[1:], start=numbers[0]))
    puzzle.answer_b = max(len(x + y) for x, y in permutations(numbers, 2))
