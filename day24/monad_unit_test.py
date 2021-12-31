import unittest

from monad_unit import Monad


class FooTest(unittest.TestCase):
    def setUp(self):
        instructions = [
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 1",
            "add x 12",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 4",
            "mul y x",
            "add z y",
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 1",
            "add x 11",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 11",
            "mul y x",
            "add z y",
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 1",
            "add x 13",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 5",
            "mul y x",
            "add z y",
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 1",
            "add x 11",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 11",
            "mul y x",
            "add z y",
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 1",
            "add x 14",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 14",
            "mul y x",
            "add z y",
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 26",
            "add x -10",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 7",
            "mul y x",
            "add z y",
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 1",
            "add x 11",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 11",
            "mul y x",
            "add z y",
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 26",
            "add x -9",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 4",
            "mul y x",
            "add z y",
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 26",
            "add x -3",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 6",
            "mul y x",
            "add z y",
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 1",
            "add x 13",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 5",
            "mul y x",
            "add z y",
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 26",
            "add x -5",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 9",
            "mul y x",
            "add z y",
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 26",
            "add x -10",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 12",
            "mul y x",
            "add z y",
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 26",
            "add x -4",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 14",
            "mul y x",
            "add z y",
            "inp w",
            "mul x 0",
            "add x z",
            "mod x 26",
            "div z 26",
            "add x -5",
            "eql x w",
            "eql x 0",
            "mul y 0",
            "add y 25",
            "mul y x",
            "add y 1",
            "mul z y",
            "mul y 0",
            "add y w",
            "add y 14",
            "mul y x",
            "add z y",
        ]
        self.monad = Monad(instructions)

    def test_maximum(self):
        self.assertEqual(92915979999498, self.monad.maximize())

    def test_minimum(self):
        self.assertEqual(21611513911181, self.monad.minimize())


if __name__ == "__main__":
    unittest.main()
