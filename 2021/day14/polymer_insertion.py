from collections import Counter

Rules = dict[str, str]


class Polymer:
    def __init__(self, initial_sequence: str, rules: Rules) -> None:
        self.rules = rules
        self.pair_counts = Counter()
        for n in range(len(initial_sequence) - 1):
            self.pair_counts[initial_sequence[n] + initial_sequence[n + 1]] += 1
        # the last element will be under-counted when transforming pairs into elements
        self.last_element = initial_sequence[-1]

    def evolve(self, steps: int) -> None:
        new_pair_counts = Counter()
        for pair, count in self.pair_counts.items():
            middle_element = self.rules[pair]
            new_pair_counts[pair[0] + middle_element] += count
            new_pair_counts[middle_element + pair[1]] += count
        self.pair_counts = new_pair_counts

        if steps > 1:
            self.evolve(steps - 1)

    def get_element_counts(self) -> Counter[str]:
        element_counts = Counter([self.last_element])
        for pair, count in self.pair_counts.items():
            element_counts[pair[0]] += count
        return element_counts

    @staticmethod
    def parse_rules(rules_raw: list[str]) -> Rules:
        rules = {}
        for rule_raw in rules_raw:
            sequence, element = rule_raw.split(" -> ")
            rules[sequence] = element
        return rules


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=14)
    data = transforms.lines(puzzle.input_data)

    sequence_rules_separator = data.index("")
    polymer = Polymer(data[0], Polymer.parse_rules(data[sequence_rules_separator + 1 :]))

    # most common element count minus least common element count after 10 steps
    polymer.evolve(10)
    element_counts_after_10 = polymer.get_element_counts().most_common()
    puzzle.answer_a = element_counts_after_10[0][1] - element_counts_after_10[-1][1]

    # same after 40 steps, so 30 steps remaining
    polymer.evolve(30)
    element_counts_after_40 = polymer.get_element_counts().most_common()
    puzzle.answer_b = element_counts_after_40[0][1] - element_counts_after_40[-1][1]
