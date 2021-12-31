from heapq import heappop, heappush
from typing import Iterator


class Burrow:
    def __init__(self, rooms: [str]) -> None:
        self.rooms = rooms
        self.room_size = sum(len(room) for room in rooms) // len(rooms)

    def find_optimal_energy(self) -> int:
        """Find optimal energy expenditure to organize amphipods into rooms."""
        state = "".join(self.rooms) + "." * 11
        final_state = "".join(x * self.room_size for x in "ABCD") + "." * 11

        heap = [(0, state)]
        state_energies = {state: 0}
        while heap:
            energy, state = heappop(heap)
            if state == final_state:
                return energy
            for n, i, j in self.get_valid_moves(state):
                next_state = self.swap(state, i, j)
                next_energy = energy + n * 10 ** "ABCD".index(state[i])
                if state_energies.get(next_state, 1 << 32) > next_energy:
                    heappush(heap, (next_energy, next_state))
                    state_energies[next_state] = next_energy

    @staticmethod
    def swap(state: str, i: int, j: int) -> str:
        """Swap state values at indices `i` and `j`."""
        if i > j:
            i, j = j, i
        return state[:i] + state[j] + state[i + 1 : j] + state[i] + state[j + 1 :]

    @staticmethod
    def walk_range(i: int, j: int) -> range:
        """Generate a range from after `i` to `j` inclusive."""
        step = -1 if i > j else 1
        return range(i + step, j + step, step)

    def get_hallway_moves(self, state: str, door) -> Iterator[tuple[int, int]]:
        """Yield distance and index to hallway spot."""
        first_door = 4 * self.room_size + 2
        doors = tuple(range(first_door, first_door + 8, 2))

        for end in (4 * self.room_size, len(state) - 1):
            for n, i in enumerate(self.walk_range(door, end)):
                if state[i] != ".":
                    break
                if i not in doors:
                    yield n + 1, i

    def get_valid_moves(self, state: str) -> Iterator[tuple[int, int, int]]:
        """Yield distance and source, destination indices."""
        for room, expect in zip(range(0, 4 * self.room_size, self.room_size), "ABCD"):
            door = 4 * self.room_size + 2 * (room // self.room_size + 1)
            for depth, cell in enumerate(state[room : room + self.room_size]):
                if cell != ".":
                    if cell != expect or any(state[room + d] != expect for d in range(depth + 1, self.room_size)):
                        for door_dist, hall in self.get_hallway_moves(state, door):
                            yield door_dist + depth + 1, room + depth, hall
                    break

        for hall in range(4 * self.room_size, len(state)):
            agent = state[hall]
            if agent != ".":
                room = "ABCD".index(agent) * self.room_size
                door = 4 * self.room_size + 2 * (room // self.room_size + 1)
                if all(state[i] == "." for i in self.walk_range(hall, door)):
                    door_dist = abs(hall - door)
                    for depth in range(self.room_size - 1, -1, -1):
                        cell = state[room + depth]
                        if cell == ".":
                            yield door_dist + depth + 1, hall, room + depth
                        elif cell != agent:
                            break


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=23)
    data = transforms.lines(puzzle.input_data)

    double_rooms = ["".join(data[y][x] for y in [2, 3]) for x in [3, 5, 7, 9]]
    small_burrow = Burrow(double_rooms)
    puzzle.answer_a = small_burrow.find_optimal_energy()

    quad_rooms = [room[0] + extra_room + room[1] for room, extra_room in zip(double_rooms, ["DD", "CB", "BA", "AC"])]
    big_burrow = Burrow(quad_rooms)
    puzzle.answer_b = big_burrow.find_optimal_energy()
