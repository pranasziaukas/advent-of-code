import unittest

from path_finder import get_full_path_count


class PathFinderTest(unittest.TestCase):
    def setUp(self):
        self.data = 0

    def test_small(self):
        connections = [
            "start-A",
            "start-b",
            "A-c",
            "A-b",
            "b-d",
            "A-end",
            "b-end",
        ]
        self.assertEqual(10, get_full_path_count(connections))

    def test_medium(self):
        connections = [
            "dc-end",
            "HN-start",
            "start-kj",
            "dc-start",
            "dc-HN",
            "LN-dc",
            "HN-end",
            "kj-sa",
            "kj-HN",
            "kj-dc",
        ]
        self.assertEqual(19, get_full_path_count(connections))

    def test_large(self):
        connections = [
            "fs-end",
            "he-DX",
            "fs-he",
            "start-DX",
            "pj-DX",
            "end-zg",
            "zg-sl",
            "zg-pj",
            "pj-he",
            "RW-he",
            "fs-DX",
            "pj-RW",
            "zg-RW",
            "start-pj",
            "he-WI",
            "zg-he",
            "pj-fs",
            "start-RW",
        ]
        self.assertEqual(226, get_full_path_count(connections))


if __name__ == "__main__":
    unittest.main()
