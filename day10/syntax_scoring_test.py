import unittest

from syntax_scoring import get_error_score


class SyntaxScoringTest(unittest.TestCase):
    def setUp(self):
        # navigation subsystem entry, error score
        self.data = [
            ("[({(<(())[]>[[{[]{<()<>>", 0),
            ("[(()[<>])]({[<{<<[]>>(", 0),
            ("{([(<{}[<>[]}>{[]{[(<()>", 1197),
            ("(((({<>}<{<{<>}{[]{[]{}", 0),
            ("[[<[([]))<([[{}[[()]]]", 3),
            ("[{[{({}]{}}([{[{{{}}([]", 57),
            ("{<[[]]>}<{[{[{[]{()[[[]", 0),
            ("[<(<(<(<{}))><([]([]()", 3),
            ("<{([([[(<>()){}]>(<<{{", 25137),
            ("<{([{{}}[<[[[<>{}]]]>[]]", 0),
        ]

    def test_error_score(self):
        for entry, score in self.data:
            self.assertEqual(score, get_error_score(entry))


if __name__ == "__main__":
    unittest.main()
