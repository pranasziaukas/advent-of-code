from typing import Callable
import math


def linear_cost(distance: int) -> int:
    return distance


def compounding_cost(distance: int) -> int:
    return distance * (distance + 1) // 2


class CrabSwarm:
    def __init__(self, positions: list[int]):
        self._positions = sorted(positions)

        self.median = self._positions[len(self._positions) // 2]
        self.average = sum(self._positions) / len(self._positions)

    def get_fuel_consumption(self, position: int, cost_function: Callable[[int], int] = linear_cost) -> int:
        return sum(cost_function(abs(position - x)) for x in self._positions)


if __name__ == "__main__":
    from aocd import models

    puzzle = models.Puzzle(year=2021, day=7)
    data = [int(x) for x in puzzle.input_data.split(",")]

    swarm = CrabSwarm(data)
    # Median minimizes /sum_{x} |x - x*|
    optimal_position_linear = swarm.median
    puzzle.answer_a = swarm.get_fuel_consumption(optimal_position_linear)

    # Average approximately minimizes /sum_{x} |x - x*| (|x - x*| + 1) / 2
    # over integer values
    optimal_positions_compounding = [math.floor(swarm.average), math.ceil(swarm.average)]
    puzzle.answer_b = min(swarm.get_fuel_consumption(p, compounding_cost) for p in optimal_positions_compounding)
