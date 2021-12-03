import unittest

from binary_diagnostic import Report


class BinaryDiagnosticTest(unittest.TestCase):
    def setUp(self):
        self.data = [
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

    def test_simple(self):
        report = Report(self.data)
        self.assertEqual(22, report.gamma_rate)
        self.assertEqual(9, report.epsilon_rate)


if __name__ == "__main__":
    unittest.main()
