import unittest

from binary_diagnostic import Report


class BinaryDiagnosticTest(unittest.TestCase):
    def setUp(self):
        data = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]

        self.report = Report(data)

    def test_simple(self):
        self.assertEqual(22, self.report.gamma_rate)
        self.assertEqual(9, self.report.epsilon_rate)

    def test_advanced(self):
        self.assertEqual(23, self.report.oxygen_generator_rating)
        self.assertEqual(10, self.report.co2_scrubber_rating)


if __name__ == "__main__":
    unittest.main()
