from collections import deque

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
        self.basins = self._get_basins()

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

    def _get_basins(self) -> list[Points]:
        basins = []
        seen = set()
        for x in range(self.max_x):
            for y in range(self.max_y):
                if (x, y) not in seen and self.map_values[x][y] != 9:
                    basin = []
                    queue = deque([(x, y)])
                    while queue:
                        x, y = queue.popleft()
                        if (x, y) in seen or self.map_values[x][y] == 9:
                            continue
                        seen.add((x, y))
                        basin.append(self.map_values[x][y])
                        for dx, dy in HeightMap.neighbors:
                            if self._is_inside(x + dx, y + dy):
                                queue.append((x + dx, y + dy))
                    basins.append(basin)
        return basins


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=9)
    data = [[int(x) for x in line] for line in transforms.lines(puzzle.input_data)]
    height_map = HeightMap(data)

    puzzle.answer_a = sum(height_map.low_points) + len(height_map.low_points)

    largest_basins = sorted(height_map.basins, key=len, reverse=True)
    largest_basin_areas = 1
    for n in range(3):
        largest_basin_areas *= len(largest_basins[n])
    puzzle.answer_b = largest_basin_areas
