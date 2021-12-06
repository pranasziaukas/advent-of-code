import unittest

from lanternfish import LanternfishPopulation


class FooTest(unittest.TestCase):
    def setUp(self):
        data = [3, 4, 3, 1, 2]
        self.population = LanternfishPopulation(data)

    def test_initial(self):
        self.assertEqual(5, len(self.population))

    def test_18(self):
        self.population.pass_time(days=18)
        self.assertEqual(26, len(self.population))

    def test_80(self):
        self.population.pass_time(days=80)
        self.assertEqual(5934, len(self.population))


if __name__ == "__main__":
    unittest.main()
