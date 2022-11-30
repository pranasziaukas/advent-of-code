import unittest

from image_enhancement import Point, Image


class ImageEnhancementTest(unittest.TestCase):
    def setUp(self):
        light_codes_raw = [
            "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#.",
            ".#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..",
            "#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....",
            "#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####",
            ".#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.",
            "#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..",
            "#.##.#....##..#.####....##...##..#...#......#.#.......#.......##",
            "..####..#...#.#.#...##..#.#..###..#####........#..####......#..#",
        ]

        light_codes = {n for n, value in enumerate("".join(light_codes_raw)) if value == "#"}

        pixels_raw = [
            "#..#.",
            "#....",
            "##..#",
            "..#..",
            "..###",
        ]

        pixels = {Point(x, y) for y, line in enumerate(pixels_raw) for x, value in enumerate(line) if value == "#"}

        self.image = Image(light_codes, pixels)

    def test_pixels_step_0(self):
        self.assertEqual(10, len(self.image))

        result = "\n".join(
            [
                "#..#.",
                "#....",
                "##..#",
                "..#..",
                "..###",
            ]
        )
        self.assertEqual(result, str(self.image))

    def test_pixels_step_1(self):
        self.image.enhance()
        self.assertEqual(24, len(self.image))

        result = "\n".join(
            [
                ".##.##.",
                "#..#.#.",
                "##.#..#",
                "####..#",
                ".#..##.",
                "..##..#",
                "...#.#.",
            ]
        )
        self.assertEqual(result, str(self.image))

    def test_pixels_step_2(self):
        self.image.enhance(steps=2)
        self.assertEqual(35, len(self.image))

        result = "\n".join(
            [
                ".......#.",
                ".#..#.#..",
                "#.#...###",
                "#...##.#.",
                "#.....#.#",
                ".#.#####.",
                "..#.#####",
                "...##.##.",
                "....###..",
            ]
        )
        self.assertEqual(result, str(self.image))

    def test_pixels_step_50(self):
        self.image.enhance(steps=50)
        self.assertEqual(3351, len(self.image))

    def test_infinite_pixels(self):
        # An alternating grid of infinite lit pixels.
        self.image.light_codes.add(0)
        self.image.light_codes.discard(511)

        for n in range(1, 5):
            self.image.enhance()
            if n % 2 == 0:
                self.assertLess(0, len(self.image))
            else:
                with self.assertRaises(OverflowError):
                    len(self.image)


if __name__ == "__main__":
    unittest.main()
