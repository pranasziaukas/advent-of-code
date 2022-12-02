import unittest

from rock_paper_scissors import Shape, score, find_shapes_simple, find_shapes_advanced


class RockPaperScissorsTest(unittest.TestCase):
    def test_score_tie(self):
        self.assertEqual(4, score(Shape.ROCK, Shape.ROCK))
        self.assertEqual(6, score(Shape.SCISSORS, Shape.SCISSORS))

    def test_score_loss(self):
        self.assertEqual(1, score(Shape.PAPER, Shape.ROCK))
        self.assertEqual(3, score(Shape.ROCK, Shape.SCISSORS))

    def test_score_win(self):
        self.assertEqual(7, score(Shape.SCISSORS, Shape.ROCK))
        self.assertEqual(8, score(Shape.ROCK, Shape.PAPER))

    def test_find_shapes_simple(self):
        self.assertEqual((Shape.ROCK, Shape.ROCK), find_shapes_simple(("A", "X")))
        self.assertEqual((Shape.PAPER, Shape.SCISSORS), find_shapes_simple(("B", "Z")))

    def test_find_shapes_advanced(self):
        self.assertEqual((Shape.ROCK, Shape.SCISSORS), find_shapes_advanced(("A", "X")))
        self.assertEqual((Shape.PAPER, Shape.SCISSORS), find_shapes_advanced(("B", "Z")))


if __name__ == "__main__":
    unittest.main()
