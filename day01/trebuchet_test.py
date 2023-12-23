import unittest

from trebuchet import find_line_number


class TrebuchetTest(unittest.TestCase):
    def test_simple(self):
        for line, number in [
            ("1abc2", 12),
            ("pqr3stu8vwx", 38),
            ("a1b2c3d4e5f", 15),
            ("treb7uchet", 77),
        ]:
            self.assertEqual(number, find_line_number(line))

    def test_advanced(self):
        for line, number in [
            ("two1nine", 29),
            ("eightwothree", 83),
            ("abcone2threexyz", 13),
            ("xtwone3four", 24),
            ("4nineeightseven2", 42),
            ("zoneight234", 14),
            ("7pqrstsixteen", 76),
        ]:
            self.assertEqual(number, find_line_number(line))


if __name__ == "__main__":
    unittest.main()
