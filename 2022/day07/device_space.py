from collections import defaultdict


def parse(lines: [str]) -> {str: int}:
    sizes = defaultdict(int)
    stack = []
    for line in lines:
        match line.split():
            case [_, _, "/"]:
                stack = []
            case [_, _, ".."]:
                stack.pop()
            case [_, _, x]:
                stack.append(x)
            case [a, _] if a.isdigit():
                for i in range(len(stack) + 1):
                    path = "/" + "/".join(stack[:i])
                    sizes[path] += int(a)
    return sizes


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2022, day=7)

    # No demo data provided

    directory_sizes = parse(transforms.lines(puzzle.input_data))
    puzzle.answer_a = sum(size for size in directory_sizes.values() if size <= 1e5)

    threshold = directory_sizes["/"] - 4e7
    puzzle.answer_b = min(size for size in directory_sizes.values() if size > threshold)
