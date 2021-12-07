import unittest

from crab_alignment import CrabSwarm, compounding_cost
import math


class CrabAlignmentTest(unittest.TestCase):
    def setUp(self):
        data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        self.swarm = CrabSwarm(data)

    def test_median_position(self):
        self.assertEqual(2, self.swarm.median)

    def test_fuel_consumptions(self):
        self.assertEqual(37, self.swarm.get_fuel_consumption(2))
        self.assertEqual(41, self.swarm.get_fuel_consumption(1))
        self.assertEqual(39, self.swarm.get_fuel_consumption(3))
        self.assertEqual(71, self.swarm.get_fuel_consumption(10))

    def test_approx_average_position(self):
        self.assertTrue(5 in [math.floor(self.swarm.average), math.ceil(self.swarm.average)])

    def test_compounding_fuel_consumptions(self):
        self.assertEqual(168, self.swarm.get_fuel_consumption(5, compounding_cost))
        self.assertEqual(206, self.swarm.get_fuel_consumption(2, compounding_cost))


if __name__ == "__main__":
    unittest.main()
