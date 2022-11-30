import unittest

from path_finder import get_path_count, parse_links


class PathFinderTest(unittest.TestCase):
    def setUp(self):
        connections_catalog = {
            "small": [
                "start-A",
                "start-b",
                "A-c",
                "A-b",
                "b-d",
                "A-end",
                "b-end",
            ],
            "medium": [
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
            ],
            "large": [
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
            ],
        }

        self.links_catalog = {label: parse_links(connections) for label, connections in connections_catalog.items()}

    def test_single_visits(self):
        self.assertEqual(10, get_path_count(self.links_catalog["small"]))
        self.assertEqual(19, get_path_count(self.links_catalog["medium"]))
        self.assertEqual(226, get_path_count(self.links_catalog["large"]))

    def test_double_visits(self):
        self.assertEqual(36, get_path_count(self.links_catalog["small"], double_visit=True))
        self.assertEqual(103, get_path_count(self.links_catalog["medium"], double_visit=True))
        self.assertEqual(3509, get_path_count(self.links_catalog["large"], double_visit=True))


if __name__ == "__main__":
    unittest.main()
