import unittest

from paper_fold import Sheet


class PaperFoldTest(unittest.TestCase):
    def setUp(self):
        data = [
            "6,10",
            "0,14",
            "9,10",
            "0,3",
            "10,4",
            "4,11",
            "6,0",
            "6,12",
            "4,1",
            "0,13",
            "10,12",
            "3,4",
            "3,0",
            "8,4",
            "1,10",
            "2,14",
            "8,10",
            "9,0",
        ]

        self.sheet = Sheet(data)
        self.folds = [
            {"axis": "y", "value": 7},
            {"axis": "x", "value": 5},
        ]

    def test_size_no_folds(self):
        self.assertEqual(18, len(self.sheet))

    def test_size_one_fold(self):
        self.sheet.fold(**self.folds[0])
        self.assertEqual(17, len(self.sheet))

    def test_size_all_folds(self):
        for fold in self.folds:
            self.sheet.fold(**fold)
        self.assertEqual(16, len(self.sheet))


if __name__ == "__main__":
    unittest.main()
