def bar(something: int) -> int:
    return something


class Lanternfish:
    adult_timer = 6

    def __init__(self, timer: int = 8) -> None:
        self.timer = timer

    def evolve(self) -> None:
        self.timer = self.timer - 1 if self.timer else Lanternfish.adult_timer

    def __str__(self):
        return str(self.timer)


class LanternfishPopulation:
    def __init__(self, timers: list[int]) -> None:
        self.fish = [Lanternfish(timer) for timer in timers]

    def pass_time(self, days: int) -> None:
        if days > 0:
            for fish in list(self.fish):
                if fish.timer == 0:
                    self.fish.append(Lanternfish())
                fish.evolve()
            self.pass_time(days - 1)

    def __len__(self) -> int:
        return len(self.fish)


if __name__ == "__main__":
    from aocd import models

    puzzle = models.Puzzle(year=2021, day=6)
    data = [int(x) for x in puzzle.input_data.split(",")]
    population = LanternfishPopulation(data)
    population.pass_time(days=80)
    puzzle.answer_a = len(population)
