import unittest

from camp_cleanup import contains, overlaps


class CampCleanupTest(unittest.TestCase):
    def test_contains(self):
        self.assertEqual(True, contains(((1, 2), (0, 2))))
        self.assertEqual(True, contains(((1, 1), (1, 1))))
        self.assertEqual(True, contains(((1, 3), (1, 2))))
        self.assertEqual(False, contains(((1, 2), (2, 3))))
        self.assertEqual(False, contains(((4, 4), (1, 2))))
        self.assertEqual(False, contains(((1, 2), (5, 6))))

    def test_overlaps(self):
        self.assertTrue(overlaps(((1, 3), (3, 4))))
        self.assertTrue(overlaps(((1, 3), (2, 2))))
        self.assertTrue(overlaps(((1, 3), (0, 1))))
        self.assertFalse(overlaps(((1, 3), (4, 5))))
        self.assertFalse(overlaps(((1, 3), (5, 5))))


if __name__ == "__main__":
    unittest.main()
