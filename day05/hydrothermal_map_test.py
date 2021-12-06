import unittest

from hydrothermal_map import HydrothermalMap


class FooTest(unittest.TestCase):
    def setUp(self):
        self.data = [
            "0,9 -> 5,9",
            "8,0 -> 0,8",
            "9,4 -> 3,4",
            "2,2 -> 2,1",
            "7,0 -> 7,4",
            "6,4 -> 2,0",
            "0,9 -> 2,9",
            "3,4 -> 1,4",
            "0,0 -> 8,8",
            "5,5 -> 8,2",
        ]

    def test_perpendicular_intersections(self):
        hydrothermal_map = HydrothermalMap()
        for line in self.data:
            hydrothermal_map.draw(line, ignore_diagonal=True)
        self.assertEqual(5, hydrothermal_map.get_intersection_count())

    def test_intersections(self):
        hydrothermal_map = HydrothermalMap()
        for line in self.data:
            hydrothermal_map.draw(line)
        self.assertEqual(12, hydrothermal_map.get_intersection_count())


if __name__ == "__main__":
    unittest.main()
