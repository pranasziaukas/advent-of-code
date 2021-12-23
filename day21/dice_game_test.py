import unittest

from dice_game import Player, Game


class FooTest(unittest.TestCase):
    def setUp(self):
        self.game = Game(Player(3), Player(7))

    def test_one_turn(self):
        self.game.take_turn()
        self.assertEqual(Player(9, 10), self.game.player_last)
        self.assertEqual(Player(7, 0), self.game.player_next)
        self.assertEqual(3, self.game.roll_count)

    def test_full_game(self):
        self.game.play()
        self.assertEqual(Player(9, 1000), self.game.player_last)
        self.assertEqual(Player(2, 745), self.game.player_next)
        self.assertEqual(993, self.game.roll_count)


if __name__ == "__main__":
    unittest.main()
