import socket
import struct
import binascii

class udpHeader:
    def __init__(self, sport, dport, length, checksum):
        self.sport = sport  # Source Port
        self.dport = dport  # Destination Port
        self.length = length    # UDP packets length
        self.checksum = checksum    # 2 Byte checksum

    # Pack UDP header
    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!4H', self.sport, self.dport,
                              self.length, self.checksum)
        return packed

    # Unpack UDP header
    def unpack_Udphdr(buffer):
        unpacked = struct.unpack('!4H', buffer[:20])
        return unpacked

    def getSrcPort(unpacked):
        return unpacked[0]

    def getDstPort(unpacked):
        return unpacked[1]

    def getLength(unpacked):
        return unpacked[2]

    def getChecksum(unpacked):
        return unpacked[3]

# Define Udphdr class and pack_Udphdr() function
udp = udpHeader(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = udpHeader.unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)
print('Source Port: {} Destination Port: {} Length {} Checksum: {}'
      .format(udpHeader.getSrcPort(unpacked_udphdr),
              udpHeader.getDstPort(unpacked_udphdr),
              udpHeader.getLength(unpacked_udphdr),
              udpHeader.getChecksum(unpacked_udphdr)))