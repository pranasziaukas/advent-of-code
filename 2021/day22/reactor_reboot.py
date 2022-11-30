from __future__ import annotations

from collections import namedtuple
from dataclasses import dataclass
from re import findall

from math import prod

Point = namedtuple("Point", ["x", "y", "z"])


@dataclass
class Cuboid:
    min: Point
    max: Point

    @property
    def has_volume(self) -> bool:
        """Check if a given cuboid has volume."""
        return all(getattr(self.min, axis) <= getattr(self.max, axis) for axis in ["x", "y", "z"])

    def __sub__(self, other: Cuboid) -> [Cuboid]:
        """Difference between two cuboids (up to 6 sub-cuboids)."""
        # Quick return if cuboids certainly don't overlap.
        if any(
            getattr(this.min, axis) > getattr(that.max, axis)
            for this, that in [(self, other), (other, self)]
            for axis in ["x", "y", "z"]
        ):
            return [self]

        cuboids = [
            Cuboid(min=self.min, max=Point(self.max.x, self.max.y, min(self.max.z, other.min.z - 1))),
            Cuboid(min=Point(self.min.x, self.min.y, max(self.min.z, other.max.z + 1)), max=self.max),
            Cuboid(
                min=Point(self.min.x, self.min.y, max(self.min.z, other.min.z)),
                max=Point(self.max.x, min(self.max.y, other.min.y - 1), min(self.max.z, other.max.z)),
            ),
            Cuboid(
                min=Point(self.min.x, max(self.min.y, other.max.y + 1), max(self.min.z, other.min.z)),
                max=Point(self.max.x, self.max.y, min(self.max.z, other.max.z)),
            ),
            Cuboid(
                min=Point(self.min.x, max(self.min.y, other.min.y), max(self.min.z, other.min.z)),
                max=Point(min(self.max.x, other.min.x - 1), min(self.max.y, other.max.y), min(self.max.z, other.max.z)),
            ),
            Cuboid(
                min=Point(max(self.min.x, other.max.x + 1), max(self.min.y, other.min.y), max(self.min.z, other.min.z)),
                max=Point(self.max.x, min(self.max.y, other.max.y), min(self.max.z, other.max.z)),
            ),
        ]
        return [cuboid for cuboid in cuboids if cuboid.has_volume]

    def __len__(self) -> int:
        """Size of a given cuboid."""
        return prod(getattr(self.max, axis) - getattr(self.min, axis) + 1 for axis in ["x", "y", "z"])


class Reactor:
    def __init__(self):
        self.cuboids: [Cuboid] = []

    def execute(self, command: str, limit: int = None) -> None:
        """Execute a reactor command."""
        is_on = command.startswith("on")
        coords = list(map(int, findall(r"-?\d+", command)))

        if limit and not all(-limit <= coord <= limit for coord in coords):
            return

        new_cuboid = Cuboid(min=Point(coords[0], coords[2], coords[4]), max=Point(coords[1], coords[3], coords[5]))
        cuboids = [new_cuboid] if is_on else []
        for cuboid in self.cuboids:
            cuboids += cuboid - new_cuboid

        self.cuboids = cuboids

    def __len__(self) -> int:
        """Total size of cuboids in the ON state."""
        return sum(len(cuboid) for cuboid in self.cuboids)


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=22)
    data = transforms.lines(puzzle.input_data)

    limited_reactor = Reactor()
    for line in data:
        limited_reactor.execute(line, limit=50)
    puzzle.answer_a = len(limited_reactor)

    reactor = Reactor()
    for line in data:
        reactor.execute(line)
    puzzle.answer_b = len(reactor)
