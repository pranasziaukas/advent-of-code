def split_in_halves(item_list: [str]) -> [(str, str)]:
    return [(items[: len(items) // 2], items[len(items) // 2 :]) for items in item_list]


def group_in_threes(item_list: [str]) -> [(str, str, str)]:
    return list(zip(*[iter(item_list)] * 3))


def find_common_item(item_packs: (str, ...)) -> str:
    return set.intersection(*(set(items) for items in item_packs)).pop()


def get_priority(item: str) -> int:
    if "a" <= item <= "z":
        priority = ord(item) - ord("a") + 1
    else:
        priority = ord(item) - ord("A") + 27
    return priority


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2022, day=3)

    data_demo = transforms.lines(puzzle.example_data)
    assert sum(get_priority(find_common_item(x)) for x in split_in_halves(data_demo)) == 157
    assert sum(get_priority(find_common_item(x)) for x in group_in_threes(data_demo)) == 70

    data = transforms.lines(puzzle.input_data)
    puzzle.answer_a = sum(get_priority(find_common_item(x)) for x in split_in_halves(data))
    puzzle.answer_b = sum(get_priority(find_common_item(x)) for x in group_in_threes(data))
