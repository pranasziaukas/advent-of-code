import unittest
from collections import deque
from operator import add, mul

from monkey_game import Monkey, play


class MonkeyGameTest(unittest.TestCase):
    def setUp(self):
        self.monkeys = [
            Monkey(items=deque([79, 98]), op=mul, op_value=19, divisor=23, pass_if_true=2, pass_if_false=3),
            Monkey(items=deque([54, 65, 75, 74]), op=add, op_value=6, divisor=19, pass_if_true=2, pass_if_false=0),
            Monkey(items=deque([79, 60, 97]), op=mul, op_value=None, divisor=13, pass_if_true=1, pass_if_false=3),
            Monkey(items=deque([74]), op=add, op_value=3, divisor=17, pass_if_true=0, pass_if_false=1),
        ]

    def test_play_1_round_items(self):
        play(self.monkeys)
        self.assertListEqual([20, 23, 27, 26], list(self.monkeys[0].items))
        self.assertListEqual([2080, 25, 167, 207, 401, 1046], list(self.monkeys[1].items))
        self.assertListEqual([], list(self.monkeys[2].items))
        self.assertListEqual([], list(self.monkeys[3].items))

    def test_play_20_round_items(self):
        play(self.monkeys, rounds=20)
        self.assertListEqual([10, 12, 14, 26, 34], list(self.monkeys[0].items))
        self.assertListEqual([245, 93, 53, 199, 115], list(self.monkeys[1].items))
        self.assertListEqual([], list(self.monkeys[2].items))
        self.assertListEqual([], list(self.monkeys[3].items))

    def test_play_10k_round_inspections_no_reduction(self):
        play(self.monkeys, rounds=10000, reduction=False)
        self.assertEqual(52166, self.monkeys[0].inspections)
        self.assertEqual(47830, self.monkeys[1].inspections)
        self.assertEqual(1938, self.monkeys[2].inspections)
        self.assertEqual(52013, self.monkeys[3].inspections)


if __name__ == "__main__":
    unittest.main()
