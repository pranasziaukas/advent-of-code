import unittest

from foo import bar


class FooTest(unittest.TestCase):
    def setUp(self):
        self.data = 0

    def test_simple(self):
        self.assertEqual(0, bar(self.data))


if __name__ == "__main__":
    unittest.main()
