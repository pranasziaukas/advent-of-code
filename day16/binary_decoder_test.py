import unittest

from binary_decoder import Packet


class BinaryDecoderTest(unittest.TestCase):
    def test_hex_to_binary(self):
        self.assertEqual("110100101111111000101000", Packet("D2FE28")._bits)
        self.assertEqual("00111000000000000110111101000101001010010001001000000000", Packet("38006F45291200")._bits)

    def test_simple_packet_version(self):
        self.assertCountEqual([6], Packet("D2FE28").versions)

    def test_complex_packet_versions(self):
        self.assertCountEqual([4, 1, 5, 6], Packet("8A004A801A8002F478").versions)

    def test_packet_version_sum(self):
        self.assertEqual(12, sum(Packet("620080001611562C8802118E34").versions))
        self.assertEqual(23, sum(Packet("C0015000016115A2E0802F182340").versions))
        self.assertEqual(31, sum(Packet("A0016C880162017C3686B18A3D4780").versions))

    def test_literal_packet_value(self):
        self.assertEqual(2021, Packet("D2FE28").value)


if __name__ == "__main__":
    unittest.main()
