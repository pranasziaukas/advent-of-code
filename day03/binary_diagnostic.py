from typing import Callable, Tuple, Union

Bit = str
Bits = Union[Bit, Tuple[Bit]]

INVERTER = {str(n): str(1 - n) for n in range(2)}


def invert(bits: Bits) -> Bits:
    return "".join(INVERTER[x] for x in bits)


def most_popular_bit(bits: Bits) -> Bit:
    return sorted(bits)[len(bits) // 2]


def least_popular_bit(bits: Bits) -> Bit:
    return invert(most_popular_bit(bits))


class Report:
    def __init__(self, readings: list[str]) -> None:
        self.readings = readings

        gamma_bits = "".join(most_popular_bit(bits) for bits in zip(*readings))
        self.gamma_rate = int(gamma_bits, 2)
        self.epsilon_rate = int(invert(gamma_bits), 2)

        def find_reading(criteria: Callable[[Bits], Bit]) -> Bits:
            current_readings = self.readings
            position_bits = list(zip(*current_readings))
            for n in range(len(position_bits)):
                required_bit = criteria(position_bits[n])
                current_readings = [reading for reading in current_readings if reading[n] == required_bit]
                if len(current_readings) == 1:
                    break
                position_bits = list(zip(*current_readings))
            return current_readings[0]

        self.oxygen_generator_rating = int(find_reading(most_popular_bit), 2)
        self.co2_scrubber_rating = int(find_reading(least_popular_bit), 2)


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=3)
    data = transforms.lines(puzzle.input_data)

    report = Report(data)
    puzzle.answer_a = report.gamma_rate * report.epsilon_rate
    puzzle.answer_b = report.oxygen_generator_rating * report.co2_scrubber_rating
