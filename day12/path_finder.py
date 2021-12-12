from collections import defaultdict, deque

Connection = str
Links = defaultdict[str, set[str]]

START = "start"
END = "end"


def parse_links(connections: list[Connection]) -> Links:
    """Parse cave links from raw connection values."""
    links = defaultdict(set)
    for connection in connections:
        x, y = connection.split("-")
        links[x].add(y)
        links[y].add(x)
    # should not return to the start cave
    for caves in links.values():
        caves.discard(START)
    # should not go anywhere from the end cave
    links[END] = set()
    return links


def get_path_count(links: Links, double_visit: bool = False) -> int:
    """Explore all routes and return the number of distinct paths between START and END."""
    path_count = 0
    queue = deque([START, y] for y in links[START])

    while queue:
        path = queue.pop()
        for y in links[path[-1]]:
            if y == END:
                path_count += 1
                continue
            if y.islower() and y in path:
                lower_path = [x for x in path if x.islower()]
                # proceed only if double visit is allowed and has not been exhausted
                if not double_visit or len(lower_path) != len(set(lower_path)):
                    continue
            queue.append(path + [y])

    return path_count


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=12)
    data = parse_links(transforms.lines(puzzle.input_data))
    puzzle.answer_a = get_path_count(data)
    puzzle.answer_b = get_path_count(data, double_visit=True)
