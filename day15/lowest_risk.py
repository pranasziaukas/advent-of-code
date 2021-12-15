from collections import namedtuple
from heapq import heappop, heappush


Point = namedtuple("Point", ["x", "y"])


class CaveMap:
    deltas = [delta for value in [-1, 1] for delta in [Point(value, 0), Point(0, value)]]

    def __init__(self, risk_data: list[str], tiles: int = 1):
        self.tiles = tiles
        self._point_risks = {
            Point(x, y): int(value) for x, risk_line in enumerate(risk_data) for y, value in enumerate(risk_line)
        }

        self.len_x = len(risk_data)
        self.len_y = len(risk_data[0])

    def get_risk(self, point: Point) -> int:
        risk = self._point_risks[Point(point.x % self.len_x, point.y % self.len_y)]
        risk += point.x // self.len_x + point.y // self.len_y
        while risk > 9:
            risk -= 9
        return risk

    def get_lowest_cumulative_risk(self) -> int:
        start_point = Point(0, 0)
        end_point = Point(self.tiles * self.len_x - 1, self.tiles * self.len_y - 1)

        cumulative_risks = {}
        heap = [(-self.get_risk(start_point), start_point)]
        while heap:
            risk_so_far, destination = heappop(heap)
            if not (start_point.x <= destination.x <= end_point.x and start_point.y <= destination.y <= end_point.x):
                continue

            total_risk = risk_so_far + self.get_risk(destination)
            if destination not in cumulative_risks or cumulative_risks[destination] > total_risk:
                cumulative_risks[destination] = total_risk
                if destination == end_point:
                    break
                for delta in CaveMap.deltas:
                    heappush(heap, (total_risk, Point(destination.x + delta.x, destination.y + delta.y)))
        return cumulative_risks[end_point]


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=15)
    data = transforms.lines(puzzle.input_data)

    cave_map = CaveMap(data)
    puzzle.answer_a = cave_map.get_lowest_cumulative_risk()

    cave_map = CaveMap(data, tiles=5)
    puzzle.answer_b = cave_map.get_lowest_cumulative_risk()
