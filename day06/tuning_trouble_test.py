import unittest

from tuning_trouble import find_marker


class TuningTroubleTest(unittest.TestCase):
    def test_find_marker_default(self):
        self.assertEqual(4, find_marker("abcde"))
        self.assertEqual(5, find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz"))
        self.assertEqual(6, find_marker("nppdvjthqldpwncqszvftbrmjlhg"))
        self.assertEqual(10, find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
        self.assertEqual(11, find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))

    def test_find_marker_14(self):
        self.assertEqual(19, find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", length=14))
        self.assertEqual(23, find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", length=14))
        self.assertEqual(23, find_marker("nppdvjthqldpwncqszvftbrmjlhg", length=14))
        self.assertEqual(29, find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", length=14))
        self.assertEqual(26, find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", length=14))


if __name__ == "__main__":
    unittest.main()
