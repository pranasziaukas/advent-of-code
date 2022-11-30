import unittest

from digit_segments import parse_entry, DigitDecoder


class DigitSegmentsTest(unittest.TestCase):
    def setUp(self):
        self.data = [
            ("be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe", 8394),
            ("edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc", 9781),
            ("fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg", 1197),
            ("fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb", 9361),
            ("aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea", 4873),
            ("fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb", 8418),
            ("dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe", 4548),
            ("bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef", 1625),
            ("egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb", 8717),
            ("gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce", 4315),
        ]

    def test_1478_count(self):
        result = 0
        for entry, _ in self.data:
            _, digits = parse_entry(entry)
            result += sum(1 for digit in digits if len(digit) in [2, 4, 3, 7])
        self.assertEqual(26, result)

    def test_decoder_map(self):
        entry = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
        patterns, digits = parse_entry(entry)
        decoder = DigitDecoder(patterns)

        pattern_values = [8, 5, 2, 3, 7, 9, 6, 4, 0, 1]
        for pattern, value in zip(patterns, pattern_values):
            self.assertEqual(value, decoder.digits_to_int([pattern]))
        self.assertEqual(5353, decoder.digits_to_int(digits))

    def test_decoder_values(self):
        for entry, digits_int in self.data:
            patterns, digits = parse_entry(entry)
            decoder = DigitDecoder(patterns)
            self.assertEqual(digits_int, decoder.digits_to_int(digits))


if __name__ == "__main__":
    unittest.main()
