import unittest

from tree_house import Forest


class TreeHouseTest(unittest.TestCase):
    def setUp(self):
        self.data = [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]]

    def test_forest_visible(self):
        self.assertEqual(21, Forest(self.data).count_visible())

    def test_forest_score(self):
        self.assertEqual(8, Forest(self.data).find_max_score())


if __name__ == "__main__":
    unittest.main()
