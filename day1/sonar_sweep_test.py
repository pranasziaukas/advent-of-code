import unittest

from sonar_sweep import count_increasing


class SonarSweepTest(unittest.TestCase):
    def setUp(self):
        self.data = [
            199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263,
        ]

    def test_simple(self):
        self.assertEqual(7, count_increasing(self.data))

    def test_lagged(self):
        self.assertEqual(5, count_increasing(self.data, lag=3))


if __name__ == "__main__":
    unittest.main()
