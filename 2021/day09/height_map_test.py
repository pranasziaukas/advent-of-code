import unittest

from height_map import HeightMap


class HeightMapTest(unittest.TestCase):
    def setUp(self):
        data = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
        ]

        self.height_map = HeightMap(data)

    def test_low_points(self):
        low_points = [1, 0, 5, 5]
        self.assertCountEqual(low_points, self.height_map.low_points)

    def test_largest_basins(self):
        basins = [
            [2, 1, 3],
            [4, 3, 2, 1, 0, 4, 2, 1, 2],
            [8, 7, 8, 8, 5, 6, 7, 8, 8, 7, 6, 7, 8, 8],
            [8, 6, 7, 8, 6, 5, 6, 7, 8],
        ]
        # Equal nested lists, regardless of their order
        self.assertCountEqual([sorted(x) for x in basins], [sorted(x) for x in self.height_map.basins])


if __name__ == "__main__":
    unittest.main()
