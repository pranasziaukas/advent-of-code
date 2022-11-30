class Monad:
    def __init__(self, instructions: [str]) -> None:
        # (position, p2) where p1=26 -> (position, p3) where p1=1
        self.map = {}

        buffer = []
        position = 0
        for n, instruction in enumerate(instructions):
            if instruction == "inp w":
                p1, p2, p3 = [int(instructions[n + m].split()[-1]) for m in [4, 5, 15]]
                if p1 == 1:
                    buffer.append((position, p3))
                elif p1 == 26:
                    self.map[(position, p2)] = buffer.pop()
                position += 1
        self.positions = position

    @staticmethod
    def _digits_to_int(digits: [int]) -> int:
        return int("".join(str(digit) for digit in digits))

    def maximize(self) -> int:
        """Find the largest valid serial number."""
        digits = [9] * self.positions

        for p in self.map:
            delta = self.map[p][1] + p[1]
            # target
            # digits[map[p][0]] + map[p][1] + p[1] == digits[p[0]]
            if delta < 0:
                digits[p[0]] = 9 + delta
            else:
                digits[self.map[p][0]] = 9 - delta

        return Monad._digits_to_int(digits)

    def minimize(self) -> int:
        """Find the smallest valid serial number."""
        digits = [1] * self.positions

        for p in self.map:
            delta = self.map[p][1] + p[1]
            if delta < 0:
                digits[self.map[p][0]] = 1 - delta
            else:
                digits[p[0]] = 1 + delta

        return Monad._digits_to_int(digits)


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=24)
    data = transforms.lines(puzzle.input_data)
    monad = Monad(data)
    puzzle.answer_a = monad.maximize()
    puzzle.answer_b = monad.minimize()
