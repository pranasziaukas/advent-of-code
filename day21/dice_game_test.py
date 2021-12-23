import unittest

from dice_game import DiracGame, Player, PracticeGame


class FooTest(unittest.TestCase):
    def setUp(self):
        self.player_pair = (Player(3), Player(7))

    def test_practice_one_turn_each(self):
        game = PracticeGame()

        player_one = self.player_pair[0]
        player_one_after = game.take_turn(player_one)
        self.assertEqual(Player(9, 10), player_one_after)
        self.assertEqual(3, game.roll_count)

        player_two = self.player_pair[1]
        player_two_after = game.take_turn(player_two)
        self.assertEqual(Player(2, 3), player_two_after)
        self.assertEqual(6, game.roll_count)

    def test_practice_full_game(self):
        game = PracticeGame(self.player_pair)
        game.play()
        self.assertEqual(Player(9, 1000), game.players[0])
        self.assertEqual(Player(2, 745), game.players[1])
        self.assertEqual(993, game.roll_count)

    def test_dirac_game(self):
        game = DiracGame()
        self.assertEqual((444356092776315, 341960390180808), game.winning_universes(self.player_pair))


if __name__ == "__main__":
    unittest.main()
