import unittest

from calorie_counting import sum_top


class CalorieCountingTest(unittest.TestCase):
    def test_sum_one(self):
        self.assertEqual(1, sum_top([[1]]))

    def test_sum_two(self):
        self.assertEqual(3, sum_top([[1], [1, 2]]))
        self.assertEqual(4, sum_top([[1], [1, 2]], how_many=2))

    def test_sum_many(self):
        data = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
        self.assertEqual(24000, sum_top(data))
        self.assertEqual(45000, sum_top(data, how_many=3))


if __name__ == "__main__":
    unittest.main()
