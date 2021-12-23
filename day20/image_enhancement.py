from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Point:
    x: int
    y: int


class Image:
    def __init__(self, light_codes: {int}, pixels: {Point}) -> None:
        self.light_codes = light_codes
        self.pixels = pixels

        self._light_outside = False

    @property
    def pixels(self) -> {Point}:
        """Lit pixels in the finite sub-image."""
        return self._pixels

    @pixels.setter
    def pixels(self, pixels: {Point}) -> None:
        """Set lit pixels, recalculate the +-1 padded finite boundaries."""
        self._pixels = pixels

        for axis in ["x", "y"]:
            setattr(
                self,
                f"range_{axis}",
                range(min(getattr(p, axis) for p in pixels) - 1, max(getattr(p, axis) for p in pixels) + 2),
            )

    def __len__(self) -> int:
        """Count lit pixels."""
        if self._light_outside:
            raise OverflowError
        return len(self._pixels)

    def _is_outside(self, point: Point) -> bool:
        """Check if the point is outside the finite sub-image."""
        return not (point.x in self.range_x and point.y in self.range_y)

    def enhance(self, steps: int = 1) -> None:
        """Enhance the image based on the existing decoding algorithm."""
        if steps <= 0:
            return

        pixels = set()
        for x in self.range_x:
            for y in self.range_y:
                code = 0
                pixel = None
                for n, (dy, dx) in enumerate(product([1, 0, -1], repeat=2)):
                    pixel = Point(x + dx, y + dy)
                    if pixel in self.pixels:
                        code |= 1 << n
                    elif self._is_outside(pixel):
                        code |= self._light_outside << n
                if code in self.light_codes:
                    pixels.add(pixel)
        self.pixels = pixels

        # Determine if the (infinite) outside pixels are lit
        outside_code = (2 ** 9) - 1 if self._light_outside else 0
        self._light_outside = outside_code in self.light_codes

        self.enhance(steps - 1)

    def __str__(self):
        """Visualize results."""
        result = ""
        for y in self.range_y:
            for x in self.range_x:
                result += "#" if Point(x, y) in self.pixels else "."
            result += "\n"
        return result[:-1]


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=20)
    data = transforms.lines(puzzle.input_data)

    image = Image(
        {n for n, value in enumerate(data[0]) if value == "#"},
        {Point(x, y) for y, line in enumerate(data[2:]) for x, value in enumerate(line) if value == "#"},
    )

    image.enhance(steps=2)
    puzzle.answer_a = len(image)
