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
        self.is_bingo = False

    def _is_marked(self, property_name: str, filter_value: int) -> bool:
        return all(
            board_value.is_marked for board_value in self.board if getattr(board_value, property_name) == filter_value
        )

    def is_marked_row(self, board_value: BoardValue) -> bool:
        return self._is_marked("y", board_value.y)

    def is_marked_column(self, board_value: BoardValue) -> bool:
        return self._is_marked("x", board_value.x)

    def mark(self, value: int) -> None:
        for board_value in self.board:
            if board_value.value == value:
                board_value.is_marked = True
                if self.is_marked_column(board_value) or self.is_marked_row(board_value):
                    self.is_bingo = True

    def score(self) -> int:
        return sum(board_value.value for board_value in self.board if not board_value.is_marked)


class BingoGame:
    def __init__(self, boards: list[Board]) -> None:
        self.boards = boards
        self.bingo_count = 0
        self.latest_bingo_board = None

    def mark(self, value: int) -> None:
        for board in self.boards:
            if board.is_bingo:
                # Already bingo, skip.
                continue
            board.mark(value)
            if board.is_bingo:
                self.bingo_count += 1
                self.latest_bingo_board = board


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=4)
    data = transforms.lines(puzzle.input_data)

    lottery_values = [int(x) for x in data[0].split(",")]
    boards_data = []
    for n in range(2, len(data), 6):
        # Inefficient, but it works.
        boards_data.append([[int(x) for x in row.split()] for row in data[n : n + 5]])
    bingo_game = BingoGame([Board(board_data) for board_data in boards_data])
    for called_value in lottery_values:
        bingo_game.mark(called_value)
        if bingo_game.bingo_count == 1:
            puzzle.answer_a = called_value * bingo_game.latest_bingo_board.score()
            break
    for called_value in lottery_values:
        bingo_game.mark(called_value)
        if bingo_game.bingo_count == len(bingo_game.boards):
            puzzle.answer_b = called_value * bingo_game.latest_bingo_board.score()
            break
