def find_marker(buffer: str, length=4) -> int:
    for n in range(length - 1, len(buffer)):
        if len(set(buffer[n - k] for k in range(length))) == length:
            return n + 1
    raise ValueError("Marker not found!")


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2022, day=6)

    data_demo = transforms.lines(puzzle.example_data)[0]
    assert find_marker(data_demo) == 7

    data = transforms.lines(puzzle.input_data)[0]
    puzzle.answer_a = find_marker(data)
    puzzle.answer_b = find_marker(data, length=14)
