import unittest

from sea_cucumbers import SeaCucumberGrid


class SeaCucumberGridTest(unittest.TestCase):
    def setUp(self):
        self.initial_state = [
            "v...>>.vv>",
            ".vv>>.vv..",
            ">>.>v>...v",
            ">>v>>.>.v.",
            "v>v.vv.v..",
            ">.>>..v...",
            ".vv..>.>v.",
            "v.v..>>v.v",
            "....v..v.>",
        ]
        self.grid = SeaCucumberGrid(self.initial_state)

    def test_state_size(self):
        self.assertEqual(10, self.grid.width)
        self.assertEqual(9, self.grid.height)

    def test_no_steps(self):
        self.grid.evolve(steps=0)
        self.assertListEqual(self.initial_state, self.grid.state)

    def test_1_step(self):
        state = [
            "....>.>v.>",
            "v.v>.>v.v.",
            ">v>>..>v..",
            ">>v>v>.>.v",
            ".>v.v...v.",
            "v>>.>vvv..",
            "..v...>>..",
            "vv...>>vv.",
            ">.v.v..v.v",
        ]
        self.grid.evolve(steps=1)
        self.assertListEqual(state, self.grid.state)

    def test_2_steps(self):
        state = [
            ">.v.v>>..v",
            "v.v.>>vv..",
            ">v>.>.>.v.",
            ">>v>v.>v>.",
            ".>..v....v",
            ".>v>>.v.v.",
            "v....v>v>.",
            ".vv..>>v..",
            "v>.....vv.",
        ]
        self.grid.evolve(steps=2)
        self.assertListEqual(state, self.grid.state)

    def test_3_steps(self):
        state = [
            "v>v.v>.>v.",
            "v...>>.v.v",
            ">vv>.>v>..",
            ">>v>v.>.v>",
            "..>....v..",
            ".>.>v>v..v",
            "..v..v>vv>",
            "v.v..>>v..",
            ".v>....v..",
        ]
        self.grid.evolve(steps=3)
        self.assertListEqual(state, self.grid.state)

    def test_4_steps(self):
        state = [
            "v>..v.>>..",
            "v.v.>.>.v.",
            ">vv.>>.v>v",
            ">>.>..v>.>",
            "..v>v...v.",
            "..>>.>vv..",
            ">.v.vv>v.v",
            ".....>>vv.",
            "vvv>...v..",
        ]
        self.grid.evolve(steps=4)
        self.assertListEqual(state, self.grid.state)

    def test_5_steps(self):
        state = [
            "vv>...>v>.",
            "v.v.v>.>v.",
            ">.v.>.>.>v",
            ">v>.>..v>>",
            "..v>v.v...",
            "..>.>>vvv.",
            ".>...v>v..",
            "..v.v>>v.v",
            "v.v.>...v.",
        ]
        self.grid.evolve(steps=5)
        self.assertListEqual(state, self.grid.state)

    def test_10_steps(self):
        state = [
            "..>..>>vv.",
            "v.....>>.v",
            "..v.v>>>v>",
            "v>.>v.>>>.",
            "..v>v.vv.v",
            ".v.>>>.v..",
            "v.v..>v>..",
            "..v...>v.>",
            ".vv..v>vv.",
        ]
        self.grid.evolve(steps=10)
        self.assertListEqual(state, self.grid.state)

    def test_20_steps(self):
        state = [
            "v>.....>>.",
            ">vv>.....v",
            ".>v>v.vv>>",
            "v>>>v.>v.>",
            "....vv>v..",
            ".v.>>>vvv.",
            "..v..>>vv.",
            "v.v...>>.v",
            "..v.....v>",
        ]
        self.grid.evolve(steps=20)
        self.assertListEqual(state, self.grid.state)

    def test_58_steps(self):
        state = [
            "..>>v>vv..",
            "..v.>>vv..",
            "..>>v>>vv.",
            "..>>>>>vv.",
            "v......>vv",
            "v>v....>>v",
            "vvv.....>>",
            ">vv......>",
            ".>v.vv.v..",
        ]
        self.grid.evolve(steps=58)
        self.assertListEqual(state, self.grid.state)

    def test_steps_to_converge(self):
        self.grid.converge()
        self.assertEqual(58, self.grid.steps)


if __name__ == "__main__":
    unittest.main()
