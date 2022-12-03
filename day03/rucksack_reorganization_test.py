import unittest

from rucksack_reorganization import split_in_half, find_common_item, get_priority


class RucksackReorganizationTest(unittest.TestCase):
    def test_split_in_half(self):
        self.assertListEqual(["a", "b"], split_in_half("ab"))
        self.assertListEqual(["ab", "cd"], split_in_half("abcd"))

    def test_find_common_item(self):
        self.assertEqual("x", find_common_item(["x", "x"]))
        self.assertEqual("c", find_common_item(["abc", "cde"]))
        self.assertEqual("B", find_common_item(["aBc", "deB"]))

    def test_get_priority(self):
        self.assertEqual(1, get_priority("a"))
        self.assertEqual(2, get_priority("b"))
        self.assertEqual(3, get_priority("c"))
        self.assertEqual(26, get_priority("z"))
        self.assertEqual(27, get_priority("A"))
        self.assertEqual(50, get_priority("X"))
        self.assertEqual(51, get_priority("Y"))
        self.assertEqual(52, get_priority("Z"))


if __name__ == "__main__":
    unittest.main()
