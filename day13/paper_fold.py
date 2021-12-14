from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])


class Sheet:
    def __init__(self, lines: list[str]) -> None:
        self.points = set()
        for line in lines:
            x_str, y_str = line.split(",")
            self.points.add(Point(int(x_str), int(y_str)))

    @property
    def max_x(self):
        return max(point.x for point in self.points)

    @property
    def max_y(self):
        return max(point.y for point in self.points)

    def fold(self, axis: str, value: int) -> None:
        folded_points = set()
        for point in self.points:
            if (current_value := getattr(point, axis)) > value:
                folded_points.add(point._replace(**{axis: value - (current_value - value)}))
            else:
                folded_points.add(point)
        self.points = folded_points

    def __len__(self) -> int:
        return len(self.points)


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=13)
    data = transforms.lines(puzzle.input_data)

    points_folds_separator = data.index("")
    sheet = Sheet(data[:points_folds_separator])
    folds = []
    for raw_fold in data[points_folds_separator + 1 :]:
        command, value_str = raw_fold.split("=")
        folds.append({"axis": command[-1], "value": int(value_str)})

    # do the first fold
    sheet.fold(**folds[0])
    puzzle.answer_a = len(sheet)

    # do the rest of the folds and print
    for fold in folds[1:]:
        sheet.fold(**fold)
    for y in range(sheet.max_y + 1):
        print("")
        for x in range(sheet.max_x + 1):
            print(f"{'#' if Point(x, y) in sheet.points else '.'}", end="")
    # PART TWO REQUIRES MANUAL SUBMISSION AFTER READING THE PRINT
