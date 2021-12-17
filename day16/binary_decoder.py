class Bits(str):
    def __int__(self) -> int:
        return int(self, 2)


class Packet:
    def __init__(self, hex_str: str) -> None:
        self._bits = bin(int(hex_str, 16))[2:]
        while len(self._bits) % 4:
            self._bits = "0" + self._bits
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
            chunks_remaining = self._get() == "1"
            literal_bits += self._get(4)
        return int(literal_bits, 2)

    def _read_nested_values(self) -> [int]:
        """Read nested packets."""
        values = []
        length_type_id = self._get()
        if length_type_id == "0":
            end_position = int(self._get(15)) + self._position
            while self._position < end_position:
                values.append(self._read())
        elif length_type_id == "1":
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
            self._read_nested_values()
            # TODO: operators
            result = 0
        return result


if __name__ == "__main__":
    from aocd import models, transforms

    puzzle = models.Puzzle(year=2021, day=16)
    data = transforms.lines(puzzle.input_data)[0]
    packet = Packet(data)
    puzzle.answer_a = sum(packet.versions)
