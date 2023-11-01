import unittest

from supply_stacks import Command, Stock


class SupplyStacksTest(unittest.TestCase):
    def setUp(self):
        self.data = {1: ["N", "Z"], 2: ["D", "C", "M"], 3: ["P"]}

    def test_stock(self):
        stock = Stock(self.data)
        self.assertEqual("NDP", stock.get_top())
        stock.do(Command(1, 2, 1))
        self.assertEqual("DCP", stock.get_top())
        stock.do(Command(3, 1, 3))
        self.assertEqual("CZ", stock.get_top())
        stock.do(Command(2, 2, 1))
        self.assertEqual("MZ", stock.get_top())
        stock.do(Command(1, 1, 2))
        self.assertEqual("CMZ", stock.get_top())

    def test_stock_reversed(self):
        stock = Stock(self.data, reverse=False)
        self.assertEqual("NDP", stock.get_top())
        stock.do(Command(1, 2, 1))
        self.assertEqual("DCP", stock.get_top())
        stock.do(Command(3, 1, 3))
        self.assertEqual("CD", stock.get_top())
        stock.do(Command(2, 2, 1))
        self.assertEqual("CD", stock.get_top())
        stock.do(Command(1, 1, 2))
        self.assertEqual("MCD", stock.get_top())


if __name__ == "__main__":
    unittest.main()
