import unittest

from submarine import Submarine


class SubmarineTest(unittest.TestCase):
    def setUp(self):
        self.data = [
            ("forward", 5),
            ("down", 5),
            ("forward", 8),
            ("up", 3),
            ("down", 8),
            ("forward", 2),
        ]

    def test_simple(self):
        submarine = Submarine()
        submarine.control(self.data)
        self.assertEqual(150, submarine.horizontal_position * submarine.depth)


if __name__ == "__main__":
    unittest.main()
