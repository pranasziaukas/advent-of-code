Digit = frozenset[str]
Digits = list[Digit]


def parse_entry(entry: str) -> tuple[Digits, Digits]:
    """Parse raw entry into patterns and output digits."""
    patterns, digits = [[frozenset(digit_str) for digit_str in sub_entry.split()] for sub_entry in entry.split(" | ")]
    return patterns, digits


class DigitDecoder:
    def __init__(self, patterns: Digits) -> None:
        digit_by_value = {}

        # Assign values by unique segment counts
        for pattern in patterns:
            # 1, 4, 7, 8 have 2, 4, 3, 7 segments respectively
            for value, length in [(1, 2), (4, 4), (7, 3), (8, 7)]:
                if len(pattern) == length:
                    digit_by_value[value] = pattern

        # Assign values with six segments
        for pattern in patterns:
            if len(pattern) == 6:
                # 9 "contains" 4
                if pattern.issuperset(digit_by_value[4]):
                    digit_by_value[9] = pattern
                # 0 "contains" 1
                elif pattern.issuperset(digit_by_value[1]):
                    digit_by_value[0] = pattern
                # 6 otherwise
                else:
                    digit_by_value[6] = pattern

        # Assign values with five segments
        for pattern in patterns:
            if len(pattern) == 5:
                # 3 "contains" 1
                if pattern.issuperset(digit_by_value[1]):
                    digit_by_value[3] = pattern
                # 5 "is contained" within 6
                elif pattern.issubset(digit_by_value[6]):
                    digit_by_value[5] = pattern
                # 2 otherwise
                else:
                    digit_by_value[2] = pattern

        self._map = {digit: str(value) for value, digit in digit_by_value.items()}

    def digits_to_int(self, digits: Digits) -> int:
        return int("".join(self._map[digit] for digit in digits))


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=8)
    data = transforms.lines(puzzle.input_data)
    patterns_outputs = [parse_entry(entry) for entry in data]

    count_1478 = 0
    for _, output in patterns_outputs:
        count_1478 += sum(1 for digit in output if len(digit) in [2, 4, 3, 7])
    puzzle.answer_a = count_1478

    output_sum = 0
    for digit_patterns, output in patterns_outputs:
        output_sum += DigitDecoder(digit_patterns).digits_to_int(output)
    puzzle.answer_b = output_sum
