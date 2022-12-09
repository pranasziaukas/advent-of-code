import unittest

from rope_bridge import Rope


class RopeBridgeTest(unittest.TestCase):
    def test_rope_seen1(self):
        instructions = [
            ("R", 4),
            ("U", 4),
            ("L", 3),
            ("D", 1),
            ("R", 4),
            ("D", 1),
            ("L", 5),
            ("R", 2),
        ]
        rope = Rope()
        for instruction in instructions:
            rope.move(instruction)
        self.assertEqual(13, len(rope.seen1))

    def test_rope_seen9(self):
        instructions = [
            ("R", 5),
            ("U", 8),
            ("L", 8),
            ("D", 3),
            ("R", 17),
            ("D", 10),
            ("L", 25),
            ("U", 20),
        ]
        rope = Rope()
        for instruction in instructions:
            rope.move(instruction)
        self.assertEqual(36, len(rope.seen9))


if __name__ == "__main__":
    unittest.main()
