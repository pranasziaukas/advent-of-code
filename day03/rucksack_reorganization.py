def parse(raw_data: str) -> [[str]]:
    return [[x[: len(x) // 2], x[len(x) // 2 :]] for x in raw_data.splitlines()]


def find_common_item(item_list: [str]) -> str:
    return set.intersection(*[set(items) for items in item_list]).pop()


def get_priority(item: str) -> int:
    if "a" <= item <= "z":
        priority = ord(item) - ord("a") + 1
    else:
        priority = ord(item) - ord("A") + 27
    return priority


if __name__ == "__main__":
    from aocd import models

    puzzle = models.Puzzle(year=2022, day=3)

    data_demo = parse(puzzle.example_data)
    assert sum(get_priority(find_common_item(x)) for x in data_demo) == 157

    data = parse(puzzle.input_data)
    puzzle.answer_a = sum(get_priority(find_common_item(x)) for x in data)
