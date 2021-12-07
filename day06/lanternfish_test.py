import unittest

from lanternfish import Lanternfish


class LanternfishTest(unittest.TestCase):
    def setUp(self):
        data = [3, 4, 3, 1, 2]
        self.population = Lanternfish(data)

    def test_initial(self):
        self.assertEqual(5, len(self.population))

    def test_18(self):
        self.population.pass_time(18)
        self.assertEqual(26, len(self.population))

    def test_80(self):
        self.population.pass_time(80)
        self.assertEqual(5934, len(self.population))

    def test_265(self):
        self.population.pass_time(256)
        self.assertEqual(26984457539, len(self.population))


if __name__ == "__main__":
    unittest.main()
