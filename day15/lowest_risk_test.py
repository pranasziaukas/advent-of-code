import unittest

from lowest_risk import CaveMap


class LowestRiskTest(unittest.TestCase):
    def setUp(self):
        risk_data = [
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
        self.cave_map = CaveMap(risk_data)

    def test_lowest_risk(self):
        self.assertEqual(40, self.cave_map.get_lowest_risk())


if __name__ == "__main__":
    unittest.main()
