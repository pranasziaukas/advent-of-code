import unittest

from crab_alignment import CrabSwarm


class FooTest(unittest.TestCase):
    def setUp(self):
        data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        self.swarm = CrabSwarm(data)

    def test_optimal_position(self):
        self.assertEqual(2, self.swarm.get_optimal_position())

    def test_fuel_consumptions(self):
        self.assertEqual(37, self.swarm.get_fuel_consumption(2))
        self.assertEqual(41, self.swarm.get_fuel_consumption(1))
        self.assertEqual(39, self.swarm.get_fuel_consumption(3))
        self.assertEqual(71, self.swarm.get_fuel_consumption(10))


if __name__ == "__main__":
    unittest.main()
