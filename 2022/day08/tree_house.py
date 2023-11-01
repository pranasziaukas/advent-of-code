from aocd import models, transforms

# Possible directions
D = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def parse(raw_data: str) -> [[int]]:
    return [[int(x) for x in line] for line in transforms.lines(raw_data)]


class Forest:
    def __init__(self, grid: [[int]]) -> None:
        self.grid = grid
        self.max_x = len(grid)
        self.max_y = len(grid[0])

    def _is_inside(self, x: int, y: int) -> bool:
        return 0 <= x < self.max_x and 0 <= y < self.max_y

    def count_visible(self) -> int:
        result = 0
        for xx in range(self.max_x):
            for yy in range(self.max_y):
                visible = False
                for dx, dy in D:
                    x = xx
                    y = yy
                    while True:
                        x += dx
                        y += dy
                        if not self._is_inside(x, y):
                            visible = True
                            break
                        if self.grid[x][y] >= self.grid[xx][yy]:
                            break
                    if visible:
                        result += 1
                        break
        return result

    def find_max_score(self) -> int:
        max_score = 0
        for xx in range(self.max_x):
            for yy in range(self.max_y):
                score = 1
                for dx, dy in D:
                    x = xx
                    y = yy
                    distance = 0
                    while True:
                        x += dx
                        y += dy
                        if not self._is_inside(x, y):
                            score *= distance
                            break
                        if self.grid[x][y] >= self.grid[xx][yy]:
                            distance += 1
                            score *= distance
                            break
                        else:
                            distance += 1
                max_score = max(score, max_score)
        return max_score


if __name__ == "__main__":
    puzzle = models.Puzzle(year=2022, day=8)

    data_demo = parse(puzzle.example_data)
    assert Forest(data_demo).count_visible() == 21
    assert Forest(data_demo).find_max_score() == 8

    data = parse(puzzle.input_data)
    puzzle.answer_a = Forest(data).count_visible()
    puzzle.answer_b = Forest(data).find_max_score()
