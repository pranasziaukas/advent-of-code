from math import prod


class Bits(str):
    def __int__(self) -> int:
        return int(self, 2) if self else 0


class Packet:
    type_operators = {
        0: lambda x: sum(x),
        1: lambda x: prod(x),
        2: lambda x: min(x),
        3: lambda x: max(x),
        5: lambda x: 1 if x[0] > x[1] else 0,
        6: lambda x: 1 if x[0] < x[1] else 0,
        7: lambda x: x[0] == x[1],
    }

    def __init__(self, hex_str: str) -> None:
        binary_str = bin(int(hex_str, 16))[2:]
        self._bits = binary_str.rjust(4 * len(hex_str), "0")
        self._position = 0

        self.versions = []
        self.value = self._read()

    def _get(self, length: int = 1) -> Bits:
        """Consume the next bits of given length."""
        bits_to_get = self._bits[self._position : self._position + length]
        self._position += length
        return Bits(bits_to_get)

    def _read_literal_value(self) -> int:
        """Read the literal value as defined in the protocol."""
        literal_bits = ""
        chunks_remaining = True
        while chunks_remaining:
            chunks_remaining = int(self._get()) == 1
            literal_bits += self._get(4)
        return int(literal_bits, 2)

    def _read_nested_values(self) -> [int]:
        """Read nested packets."""
        values = []
        length_type_id = int(self._get())
        if length_type_id == 0:
            end_position = int(self._get(15)) + self._position
            while self._position < end_position:
                values.append(self._read())
        elif length_type_id == 1:
            for _ in range(int(self._get(11))):
                values.append(self._read())
        return values

    def _read(self):
        """Read a single packet."""
        self.versions.append(int(self._get(3)))
        packet_type_id = int(self._get(3))
        if packet_type_id == 4:
            result = self._read_literal_value()
        else:
            result = Packet.type_operators[packet_type_id](self._read_nested_values())
        return result


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=16)
    data = transforms.lines(puzzle.input_data)[0]
    packet = Packet(data)
    puzzle.answer_a = sum(packet.versions)
    puzzle.answer_b = packet.value
