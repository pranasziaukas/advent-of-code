import unittest

from lowest_risk import CaveMap


class LowestRiskTest(unittest.TestCase):
    def setUp(self):
        self.risk_data = [
            "1163751742",
            "1381373672",
            "2136511328",
            "3694931569",
            "7463417111",
            "1319128137",
            "1359912421",
            "3125421639",
            "1293138521",
            "2311944581",
        ]

    def test_lowest_risk(self):
        cave_map = CaveMap(self.risk_data)
        self.assertEqual(40, cave_map.get_lowest_cumulative_risk())

    def test_lowest_risk_5_tiles(self):
        cave_map = CaveMap(self.risk_data, tiles=5)
        self.assertEqual(315, cave_map.get_lowest_cumulative_risk())


if __name__ == "__main__":
    unittest.main()
