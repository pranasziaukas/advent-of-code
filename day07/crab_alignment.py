class CrabSwarm:
    def __init__(self, positions: list[int]):
        self.positions = positions

    def get_optimal_position(self) -> int:
        return sorted(self.positions)[len(self.positions) // 2]

    def get_fuel_consumption(self, position: int) -> int:
        return sum(abs(position - x) for x in self.positions)


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=7)
    data = [int(x) for x in puzzle.input_data.split(",")]

    swarm = CrabSwarm(data)
    optimal_position = swarm.get_optimal_position()
    puzzle.answer_a = swarm.get_fuel_consumption(optimal_position)
