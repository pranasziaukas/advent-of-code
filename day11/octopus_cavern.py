from collections import deque


class OctopusCavern:
    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid
        self.max_x = len(grid)
        self.max_y = len(grid[0])

    def _is_inside(self, x: int, y: int) -> bool:
        return 0 <= x < self.max_x and 0 <= y < self.max_y

    def evolve(self) -> int:
        """Evolve the grid and return the number of flashes."""
        flashes = 0
        queue = deque()

        def power_up(xx: int, yy: int) -> None:
            self.grid[xx][yy] += 1
            if self.grid[xx][yy] == 10:
                queue.append((xx, yy))

        # increase energy levels
        for x in range(self.max_x):
            for y in range(self.max_y):
                power_up(x, y)

        # initiate flashes
        while queue:
            x, y = queue.pop()
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if self._is_inside(x + dx, y + dy) and (dx, dy) != (0, 0):
                        power_up(x + dx, y + dy)

        # cooldown
        for x in range(self.max_x):
            for y in range(self.max_y):
                if self.grid[x][y] > 9:
                    self.grid[x][y] = 0
                    flashes += 1

        return flashes


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=11)
    data = [[int(x) for x in line] for line in transforms.lines(puzzle.input_data)]
    cavern = OctopusCavern(data)
    result = 0
    for _ in range(100):
        result += cavern.evolve()
    puzzle.answer_a = result
