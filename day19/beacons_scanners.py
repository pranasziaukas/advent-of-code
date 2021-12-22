from __future__ import annotations
from dataclasses import dataclass
from time import perf_counter as pfc
import re
from itertools import combinations, permutations, product
from collections import Counter


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __abs__(self) -> int:
        return self.x ** 2 + self.y ** 2 + self.z ** 2


@dataclass
class Transformation:
    axes: [str]
    signs: [int]

    def apply(self, point: Point) -> Point:
        """Transform a given point."""
        return Point(*[sign * getattr(point, axis) for axis, sign in zip(self.axes, self.signs)])


# TODO: optimize to 24 unique transformations (instead of 48)
T = [Transformation(axes, signs) for axes in permutations(["x", "y", "z"]) for signs in product([-1, 1], repeat=3)]


@dataclass
class Scanner:
    beacons: [Point]
    position: Point

    def __post_init__(self) -> None:
        # A kind of fingerprinting for points in space.
        self._distances = [{abs(p - q) for q in self.beacons if p != q} for p in self.beacons]

    def align_with(self, other: Scanner) -> None:
        """Try to align with a known scanner."""
        pairs = []
        for p, p_distances in zip(self.beacons, self._distances):
            for q, q_distances in zip(other.beacons, other._distances):
                # There are 11 distances between 12 mutual points
                if len(p_distances & q_distances) >= 11:
                    pairs.append((p, q))

        if len(pairs):
            for transformation in T:
                offsets = {q - transformation.apply(p) for p, q in pairs}
                if len(offsets) == 1:
                    # Apply the found transformation
                    self.position = offsets.pop()
                    self.beacons = [transformation.apply(p) + self.position for p in self.beacons]


class ScannerMap:
    def __init__(self, reports: [[Point]]) -> None:
        self.scanners = [Scanner(beacons, Point(0, 0, 0) if n == 0 else None) for n, beacons in enumerate(reports)]

        while any(scanner.position is None for scanner in self.scanners):
            for known_scanner in [scanner for scanner in self.scanners if scanner.position is not None]:
                for unknown_scanner in [scanner for scanner in self.scanners if scanner.position is None]:
                    unknown_scanner.align_with(known_scanner)

    def get_beacons(self) -> {Point}:
        """Get the unique beacon locations, all relative to the first scanner."""
        return {p for scanner in self.scanners for p in scanner.beacons}


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=19)
    data = [
        [Point(*map(int, beacon.split(","))) for beacon in scanner.split("\n")[1:]]
        for scanner in puzzle.input_data.split("\n\n")
    ]
    scanner_map = ScannerMap(data)
    puzzle.answer_a = len(scanner_map.get_beacons())
