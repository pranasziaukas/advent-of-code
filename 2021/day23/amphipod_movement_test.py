import unittest

from amphipod_movement import Burrow


class AmphipodMovementTest(unittest.TestCase):
    def test_small_burrow(self):
        burrow = Burrow(["BA", "CD", "BC", "DA"])
        self.assertEqual(12521, burrow.find_optimal_energy())

    def test_big_burrow(self):
        burrow = Burrow(["BDDA", "CCBD", "BBAC", "DACA"])
        self.assertEqual(44169, burrow.find_optimal_energy())


if __name__ == "__main__":
    unittest.main()
