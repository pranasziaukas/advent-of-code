import unittest

from device_space import parse


class DeviceSpaceTest(unittest.TestCase):
    def test_parse(self):
        data = [
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k",
        ]

        directory_sizes = {
            "/": 48381165,
            "/a/e": 584,
            "/a": 94853,
            "/d": 24933642,
        }

        self.assertDictEqual(directory_sizes, parse(data))


if __name__ == "__main__":
    unittest.main()
