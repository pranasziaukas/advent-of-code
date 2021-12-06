def bar(something: int) -> int:
    return something


class Lanternfish:
    def __init__(self, timers: list[int]) -> None:
        # Group timers into groups of different stages of fertility.
        self.fertility = [0] * 9
        for timer in timers:
            self.fertility[timer] += 1

    def pass_time(self, days: int = 1) -> None:
        if days > 0:
            self.fertility = [
                # Timers 1-6 are mapped to 0-5 respectively.
                *[self.fertility[n] for n in range(1, 7)],
                # Timers 0 and 7 are mapped to 6.
                self.fertility[0] + self.fertility[7],
                # Timer 8 is mapped to 7.
                self.fertility[8],
                # Timer 0 is mapped to 8.
                self.fertility[0],
            ]
            self.pass_time(days - 1)

    def __len__(self) -> int:
        return sum(self.fertility)


if __name__ == "__main__":
    from aocd import models

    puzzle = models.Puzzle(year=2021, day=6)
    data = [int(x) for x in puzzle.input_data.split(",")]

    population = Lanternfish(data)
    population.pass_time(80)
    puzzle.answer_a = len(population)

    population = Lanternfish(data)
    population.pass_time(256)
    puzzle.answer_b = len(population)
