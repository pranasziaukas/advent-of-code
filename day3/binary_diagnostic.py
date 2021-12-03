from collections import defaultdict, Counter

INVERTER = {str(n): str(1 - n) for n in range(2)}


class Report:
    def __init__(self, readings: list[str]) -> None:
        self.readings = readings
        top_bits = [sorted(positions)[len(positions) // 2] for positions in zip(*readings)]
        self.gamma_rate = int("".join(top_bits), 2)
        self.epsilon_rate = int("".join(INVERTER[bit] for bit in top_bits), 2)


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=3)
    data = transforms.lines(puzzle.input_data)

    report = Report(data)
    puzzle.answer_a = report.gamma_rate * report.epsilon_rate
