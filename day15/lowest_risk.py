from collections import namedtuple
from heapq import heappop, heappush

Point = namedtuple("Point", ["x", "y"])


class CaveMap:
    deltas = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]

    def __init__(self, risk_data: list[str]):
        self.point_risks = {
            Point(x, y): int(value) for x, risk_line in enumerate(risk_data) for y, value in enumerate(risk_line)
        }

        self.end_point = max(point for point in self.point_risks)

    def get_lowest_risk(self) -> int:
        cumulative_risks = {}
        heap = [(-self.point_risks[Point(0, 0)], Point(0, 0))]
        while heap:
            risk_so_far, destination = heappop(heap)
            if destination not in self.point_risks:
                continue

            total_risk = risk_so_far + self.point_risks[destination]
            if destination not in cumulative_risks or cumulative_risks[destination] > total_risk:
                cumulative_risks[destination] = total_risk
                if destination == self.end_point:
                    break
                for delta in CaveMap.deltas:
                    heappush(heap, (total_risk, Point(destination.x + delta.x, destination.y + delta.y)))
        return cumulative_risks[self.end_point]


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=15)
    data = transforms.lines(puzzle.input_data)
    cave_map = CaveMap(data)

    puzzle.answer_a = cave_map.get_lowest_risk()
