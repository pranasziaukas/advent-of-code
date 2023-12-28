class Game:
    def __init__(self, line: str) -> None:
        gid, turns = line.split(': ')
        self.id = int(gid[5:])
        self.max_red = self.max_green = self.max_blue = 0

        for turn in turns.split('; '):
            for n, color in map(str.split, turn.split(', ')):
                n = int(n)

                if color == 'red':
                    self.max_red = max(n, self.max_red)
                elif color == 'green':
                    self.max_green = max(n, self.max_green)
                else:
                    self.max_blue = max(n, self.max_blue)

    def is_allowed(self) -> bool:
        return self.max_red <= 12 and self.max_green <= 13 and self.max_blue <= 14


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2023, day=2)

    data_demo = transforms.lines(puzzle.example_data)
    assert sum(Game(x).id for x in data_demo if Game(x).is_allowed()) == 8

    data = transforms.lines(puzzle.input_data)
    games = [Game(x) for x in data]
    puzzle.answer_a = sum(game.id for game in games if game.is_allowed())
    puzzle.answer_b = sum(game.max_red * game.max_green * game.max_blue for game in games)
