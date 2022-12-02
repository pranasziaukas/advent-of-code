import unittest

from rock_paper_scissors import Shape, score


class FooTest(unittest.TestCase):
    def test_score_tie(self):
        self.assertEqual(4, score(Shape.ROCK, Shape.ROCK))
        self.assertEqual(6, score(Shape.SCISSORS, Shape.SCISSORS))

    def test_score_loss(self):
        self.assertEqual(1, score(Shape.PAPER, Shape.ROCK))
        self.assertEqual(3, score(Shape.ROCK, Shape.SCISSORS))

    def test_score_win(self):
        self.assertEqual(7, score(Shape.SCISSORS, Shape.ROCK))
        self.assertEqual(8, score(Shape.ROCK, Shape.PAPER))


if __name__ == "__main__":
    unittest.main()
