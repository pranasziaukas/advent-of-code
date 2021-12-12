import unittest

from path_finder import get_path_count


class PathFinderTest(unittest.TestCase):
    def setUp(self):
        self.connections_small = [
            "start-A",
            "start-b",
            "A-c",
            "A-b",
            "b-d",
            "A-end",
            "b-end",
        ]

        self.connections_medium = [
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

        self.connections_large = [
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

    def test_single_visits(self):
        self.assertEqual(10, get_path_count(self.connections_small))
        self.assertEqual(19, get_path_count(self.connections_medium))
        self.assertEqual(226, get_path_count(self.connections_large))

    def test_double_visits(self):
        self.assertEqual(36, get_path_count(self.connections_small, double_visit=True))
        self.assertEqual(103, get_path_count(self.connections_medium, double_visit=True))
        self.assertEqual(3509, get_path_count(self.connections_large, double_visit=True))


if __name__ == "__main__":
    unittest.main()
