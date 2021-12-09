Point = int
Points = list[Point]
Map = list[Points]


class HeightMap:
    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def __init__(self, map_values: Map):
        self.map_values = map_values
        self.max_x = len(map_values)
        self.max_y = len(map_values[0])

        self.low_points = self._get_low_points()

    def _is_inside(self, x: int, y: int) -> bool:
        return 0 <= x < self.max_x and 0 <= y < self.max_y

    def _get_low_points(self) -> Points:
        points = []
        for x in range(self.max_x):
            for y in range(self.max_y):
                is_low = True
                for dx, dy in HeightMap.neighbors:
                    if self._is_inside(x + dx, y + dy) and self.map_values[x + dx][y + dy] <= self.map_values[x][y]:
                        is_low = False
                        break
                if is_low:
                    points.append(self.map_values[x][y])
        return points


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=9)
    data = [[int(x) for x in line] for line in transforms.lines(puzzle.input_data)]
    height_map = HeightMap(data)

    puzzle.answer_a = sum(height_map.low_points) + len(height_map.low_points)
