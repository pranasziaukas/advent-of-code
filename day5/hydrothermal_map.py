from collections import defaultdict


class HydrothermalMap:
    def __init__(self):
        self.point_vents = defaultdict(int)

    @staticmethod
    def _parse_line_description(line_description: str) -> list[int]:
        return [int(coord) for point_desc in line_description.split(" -> ") for coord in point_desc.split(",")]

    def draw(self, line_description: str, ignore_diagonal: bool = False) -> None:
        x1, y1, x2, y2 = self._parse_line_description(line_description)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.point_vents[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.point_vents[(x, y1)] += 1
        elif not ignore_diagonal and abs(x1 - x2) == abs(y1 - y2):
            dx = 1 if x1 < x2 else -1
            dy = 1 if y1 < y2 else -1
            for n in range(abs(x1 - x2) + 1):
                self.point_vents[(x1 + n * dx, y1 + n * dy)] += 1

    def get_intersection_count(self) -> int:
        return sum(1 for vents in self.point_vents.values() if vents > 1)


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=5)
    data = transforms.lines(puzzle.input_data)

    hydrothermal_map_simplified = HydrothermalMap()
    for line in data:
        hydrothermal_map_simplified.draw(line, ignore_diagonal=True)
    puzzle.answer_a = hydrothermal_map_simplified.get_intersection_count()

    hydrothermal_map = HydrothermalMap()
    for line in data:
        hydrothermal_map.draw(line)
    puzzle.answer_b = hydrothermal_map.get_intersection_count()
