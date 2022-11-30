import unittest

from probe_trajectory import ProbeLauncher


class ProbeLauncherTest(unittest.TestCase):
    def setUp(self):
        self.probe_launcher = ProbeLauncher(min_x=20, max_x=30, min_y=-10, max_y=-5)

    def test_apex_y(self):
        self.assertEqual(45, self.probe_launcher.apex_y)

    def test_available_velocities_count(self):
        self.assertEqual(112, len(self.probe_launcher.velocities))


if __name__ == "__main__":
    unittest.main()
