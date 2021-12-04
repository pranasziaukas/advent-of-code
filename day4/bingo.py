from dataclasses import dataclass


@dataclass
class BoardValue:
    value: int
    x: int
    y: int
    is_marked: bool = False


class Board:
    def __init__(self, raw_board: list[list[int]]) -> None:
        self.board = [BoardValue(value, x, y) for y, values in enumerate(raw_board) for x, value in enumerate(values)]

    def mark(self, value: int) -> bool:
        for board_value in self.board:
            if board_value.value == value:
                board_value.is_marked = True
                if all(
                    neighbor_value.is_marked for neighbor_value in self.board if neighbor_value.x == board_value.x
                ) or all(
                    neighbor_value.is_marked for neighbor_value in self.board if neighbor_value.y == board_value.y
                ):
                    return True
        return False

    def sum_unmarked(self) -> int:
        return sum(board_value.value for board_value in self.board if not board_value.is_marked)


class BingoGame:
    def __init__(self, boards: list[Board]) -> None:
        self.boards = boards
        self.winner = None

    def mark(self, value: int) -> bool:
        for board in self.boards:
            if board.mark(value):
                self.winner = board
                return True
        return False


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=4)
    data = transforms.lines(puzzle.input_data)

    lottery_values = [int(x) for x in data[0].split(",")]
    boards_data = []
    for n in range(2, len(data), 6):
        # Inefficient, but it works.
        boards_data.append([[int(x) for x in row.split()] for row in data[n : n + 5]])
    boards = [Board(board_data) for board_data in boards_data]
    bingo_game = BingoGame(boards)
    for value in lottery_values:
        if bingo_game.mark(value):
            puzzle.answer_a = value * bingo_game.winner.sum_unmarked()
