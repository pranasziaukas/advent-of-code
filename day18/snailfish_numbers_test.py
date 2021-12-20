import unittest

from snailfish_numbers import SnailfishNumber


class SnailfishNumberTest(unittest.TestCase):
    def test_identity(self):
        self.assertEqual(SnailfishNumber("[[1,2],[[3,4],5]]"), SnailfishNumber("[[1,2],[[3,4],5]]"))

    def test_elementary_addition(self):
        self.assertEqual(SnailfishNumber("[[1,2],[[3,4],5]]"), SnailfishNumber("[1,2]") + SnailfishNumber("[[3,4],5]"))

    def test_explode_only(self):
        self.assertEqual(SnailfishNumber("[[[[0,9],2],3],4]"), SnailfishNumber("[[[[[9,8],1],2],3],4]"))
        self.assertEqual(SnailfishNumber("[7,[6,[5,[7,0]]]]"), SnailfishNumber("[7,[6,[5,[4,[3,2]]]]]"))
        self.assertEqual(SnailfishNumber("[[6,[5,[7,0]]],3]"), SnailfishNumber("[[6,[5,[4,[3,2]]]],1]"))
        self.assertEqual(
            SnailfishNumber("[[3,[2,[8,0]]],[9,[5,[7,0]]]]"), SnailfishNumber("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
        )

    def test_full_reduce(self):
        self.assertEqual(
            SnailfishNumber("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"),
            SnailfishNumber("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"),
        )

    def test_multiple_addition(self):
        number4 = SnailfishNumber("[[[[1,1],[2,2]],[3,3]],[4,4]]")
        number5 = SnailfishNumber("[[[[3,0],[5,3]],[4,4]],[5,5]]")
        self.assertEqual(number5, number4 + SnailfishNumber("[5,5]"))
        number6 = SnailfishNumber("[[[[5,0],[7,4]],[5,5]],[6,6]]")
        self.assertEqual(number6, number5 + SnailfishNumber("[6,6]"))

    def test_list_addition(self):
        numbers = [
            SnailfishNumber(x)
            for x in [
                "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
                "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
                "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
                "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
                "[7,[5,[[3,8],[1,4]]]]",
                "[[2,[2,2]],[8,[8,1]]]",
                "[2,9]",
                "[1,[[[9,3],9],[[9,0],[0,7]]]]",
                "[[[5,[7,4]],7],1]",
                "[[[[4,2],2],6],[8,7]]",
            ]
        ]

        self.assertEqual(
            SnailfishNumber("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"), sum(numbers[1:], start=numbers[0])
        )

    def test_magnitude(self):
        self.assertEqual(143, len(SnailfishNumber("[[1,2],[[3,4],5]]")))
        self.assertEqual(1384, len(SnailfishNumber("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")))
        self.assertEqual(445, len(SnailfishNumber("[[[[1,1],[2,2]],[3,3]],[4,4]]")))
        self.assertEqual(791, len(SnailfishNumber("[[[[3,0],[5,3]],[4,4]],[5,5]]")))
        self.assertEqual(1137, len(SnailfishNumber("[[[[5,0],[7,4]],[5,5]],[6,6]]")))
        self.assertEqual(3488, len(SnailfishNumber("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")))

    def test_addition_magnitude(self):
        numbers = [
            SnailfishNumber(x)
            for x in [
                "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
                "[[[5,[2,8]],4],[5,[[9,9],0]]]",
                "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
                "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
                "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
                "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
                "[[[[5,4],[7,7]],8],[[8,3],8]]",
                "[[9,3],[[9,9],[6,[4,9]]]]",
                "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
                "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
            ]
        ]
        result = SnailfishNumber("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]")
        self.assertEqual(result, sum(numbers[1:], start=numbers[0]))
        self.assertEqual(4140, len(result))


if __name__ == "__main__":
    unittest.main()
