import unittest

from syntax_scoring import get_score, Type


class SyntaxScoringTest(unittest.TestCase):
    def setUp(self):
        # navigation subsystem entry, error score
        self.data = [
            ("[({(<(())[]>[[{[]{<()<>>", None, 288957),
            ("[(()[<>])]({[<{<<[]>>(", None, 5566),
            ("{([(<{}[<>[]}>{[]{[(<()>", 1197, None),
            ("(((({<>}<{<{<>}{[]{[]{}", None, 1480781),
            ("[[<[([]))<([[{}[[()]]]", 3, None),
            ("[{[{({}]{}}([{[{{{}}([]", 57, None),
            ("{<[[]]>}<{[{[{[]{()[[[]", None, 995444),
            ("[<(<(<(<{}))><([]([]()", 3, None),
            ("<{([([[(<>()){}]>(<<{{", 25137, None),
            ("<{([{{}}[<[[[<>{}]]]>[]]", None, 294),
        ]

    def test_error_score(self):
        for entry, error_value, _ in self.data:
            score = get_score(entry)
            if error_value:
                self.assertEqual(Type.ERROR, score.type)
                self.assertEqual(error_value, score.value)

    def test_incomplete_score(self):
        for entry, _, incomplete_value in self.data:
            score = get_score(entry)
            if incomplete_value:
                self.assertEqual(Type.INCOMPLETE, score.type)
                self.assertEqual(incomplete_value, score.value)


if __name__ == "__main__":
    unittest.main()
