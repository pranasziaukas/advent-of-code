import unittest

from polymer_insertion import Polymer


class PolymerInsertionTest(unittest.TestCase):
    def setUp(self):
        rules_raw = [
            "CH -> B",
            "HH -> N",
            "CB -> H",
            "NH -> C",
            "HB -> C",
            "HC -> B",
            "HN -> C",
            "NN -> C",
            "BH -> H",
            "NC -> B",
            "NB -> B",
            "BN -> B",
            "BB -> N",
            "BC -> B",
            "CC -> N",
            "CN -> C",
        ]
        initial_sequence = "NNCB"
        rules = Polymer.parse_rules(rules_raw)
        self.polymer = Polymer(initial_sequence, rules)

    def test_initial(self):
        element_counts = self.polymer.get_element_counts()
        self.assertEqual(4, element_counts.total())
        self.assertEqual(1, element_counts["B"])
        self.assertEqual(1, element_counts["C"])
        self.assertEqual(2, element_counts["N"])

    def test_length_after_5_steps(self):
        self.polymer.evolve(5)
        element_counts = self.polymer.get_element_counts()
        self.assertEqual(97, element_counts.total())

    def test_after_10_steps(self):
        self.polymer.evolve(10)
        element_counts = self.polymer.get_element_counts()
        self.assertEqual(3073, element_counts.total())
        self.assertEqual(1749, element_counts["B"])
        self.assertEqual(298, element_counts["C"])
        self.assertEqual(161, element_counts["H"])
        self.assertEqual(865, element_counts["N"])

    def test_after_40_steps(self):
        self.polymer.evolve(40)
        element_counts = self.polymer.get_element_counts()
        self.assertEqual(2192039569602, element_counts["B"])
        self.assertEqual(3849876073, element_counts["H"])


if __name__ == "__main__":
    unittest.main()
