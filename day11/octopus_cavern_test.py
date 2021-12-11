import unittest

from octopus_cavern import OctopusCavern


class OctopusCavernTest(unittest.TestCase):
    def setUp(self):
        self.data = [
            [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
            [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
            [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
            [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
            [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
            [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
            [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
            [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
            [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
            [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
        ]

    def test_after_10(self):
        cavern = OctopusCavern(self.data)
        flashes = 0
        for _ in range(10):
            flashes += cavern.evolve()
        self.assertEqual(204, flashes)

    def test_after_100(self):
        cavern = OctopusCavern(self.data)
        flashes = 0
        for _ in range(100):
            flashes += cavern.evolve()
        self.assertEqual(1656, flashes)


if __name__ == "__main__":
    unittest.main()
