class SeaCucumberGrid:
    def __init__(self, initial_state: [str]) -> None:
        self.state = initial_state
        self.width = len(initial_state[0])
        self.height = len(initial_state)

        self.steps = 0

    def evolve(self, steps: int = 1) -> None:
        """Evolve the grid of sea cucumbers."""
        if steps <= 0:
            return

        # Phase 1 - east direction
        state_next = []
        for segment in self.state:
            if segment[self.width - 1] + segment[0] == ">.":
                # Use placeholder values for the edge case.
                segment = "x" + segment[1 : self.width - 1] + "y"
            state_next += [segment.replace(">.", ".>").replace("y", ".").replace("x", ">")]

        # Transpose the state.
        self.state = ["".join(i) for i in zip(*state_next)]

        # Phase 2 - south direction
        state_next = []
        for segment in self.state:
            if segment[self.height - 1] + segment[0] == "v.":
                segment = "x" + segment[1 : self.height - 1] + "y"
            state_next += [segment.replace("v.", ".v").replace("y", ".").replace("x", "v")]

        # Transpose the state (again).
        self.state = ["".join(i) for i in zip(*state_next)]

        self.steps += 1
        self.evolve(steps - 1)

    def converge(self) -> None:
        """Converge until sea cucumbers are no longer moving."""
        old_state = self.state[:]
        while True:
            self.evolve()
            if all(this == that for this, that in zip(self.state, old_state)):
                break
            old_state = self.state[:]


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=25)
    data = transforms.lines(puzzle.input_data)
    grid = SeaCucumberGrid(data)
    grid.converge()
    puzzle.answer_a = grid.steps
