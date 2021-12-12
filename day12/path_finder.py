from collections import defaultdict

Connection = str
Connections = list[Connection]

START = "start"
END = "end"


def get_full_path_count(connections: Connections) -> int:
    neighbors = defaultdict(set)
    for connection in connections:
        x, y = connection.split("-")
        neighbors[x].add(y)
        neighbors[y].add(x)

    paths = {(START, y) for y in neighbors[START]}
    len_paths = len(paths)
    while True:
        for path in paths.copy():
            for y in neighbors[path[-1]]:
                if y.islower() and y in path:
                    continue
                paths.add(path + (y,))

        # complete the exploration if no new paths exist
        if len_paths == len(paths):
            break
        len_paths = len(paths)

    return sum(1 for path in paths if path[0] == START and path[-1] == END)


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=12)
    data = transforms.lines(puzzle.input_data)

    puzzle.answer_a = get_full_path_count(data)
