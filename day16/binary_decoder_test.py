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

    def test_simple_packet_value(self):
        self.assertEqual(2021, Packet("D2FE28").value)

    def test_complex_packet_value(self):
        self.assertEqual(3, Packet("C200B40A82").value)
        self.assertEqual(54, Packet("04005AC33890").value)
        self.assertEqual(7, Packet("880086C3E88112").value)
        self.assertEqual(9, Packet("CE00C43D881120").value)
        self.assertEqual(1, Packet("D8005AC2A8F0").value)
        self.assertEqual(0, Packet("F600BC2D8F").value)
        self.assertEqual(0, Packet("9C005AC2F8F0").value)
        self.assertEqual(1, Packet("9C0141080250320F1802104A08").value)


if __name__ == "__main__":
    unittest.main()
