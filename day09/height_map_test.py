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

    def test_get_low_points(self):
        self.assertCountEqual([1, 0, 5, 5], self.height_map.low_points)


if __name__ == "__main__":
    unittest.main()
