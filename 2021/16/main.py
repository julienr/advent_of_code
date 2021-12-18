import binascii

#line = 'D2FE28'
#line = '38006F45291200'
#line = 'EE00D40C823060'
#line = '8A004A801A8002F478'
#line = '620080001611562C8802118E34'
#line = 'C0015000016115A2E0802F182340'
#line = 'A0016C880162017C3686B18A3D4780'
#line = open('input').read().strip()
s = ''.join([str(bin(int(c, 16)))[2:].zfill(4) for c in line])

print(s)

class Packet:
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id

    def __repr__(self):
        return self.__str__()


class LiteralPacket(Packet):
    def __init__(self, version, type_id, value):
        super().__init__(version, type_id)
        self.value = value

    def __str__(self):
        return 'literal(version=%d, type_id=%d, value=%d)' % (self.version,
                self.type_id, self.value)

    def sum_versions(self):
        return self.version


class OperatorPacket(Packet):
    def __init__(self, version, type_id, sub_packets):
        super().__init__(version, type_id)
        self.sub_packets = sub_packets

    def __str__(self):
        return 'operator(version=%d, type_id=%d, sub_packets=\n  %s)' % (
                self.version, self.type_id,
                '\n  '.join([str(p) for p in self.sub_packets])
        )

    def sum_versions(self):
        return self.version + sum(p.sum_versions() for p in self.sub_packets)


def parse_packet(s):
    version = int(s[:3], 2)
    type_id = int(s[3:6], 2)
    if type_id == 4:
        concat = ''
        i = 6
        while True:
            concat += s[i+1:i+5]
            if s[i] == '0':
                i += 5
                break
            i += 5
            assert i < len(s)
        return LiteralPacket(version, type_id, int(concat, 2)), i
    else:
        length_type_bit = s[6]
        sub_packets = []
        if length_type_bit == '0':
            total_length = int(s[7:7+15], 2)
            i = 7 + 15
            while True:
                packet, offset = parse_packet(s[i:])
                i += offset
                sub_packets.append(packet)
                if i >= 7 + 15 + total_length:
                    break
        else:
            num_packets = int(s[7:7+11], 2)
            i = 7 + 11
            for j in range(num_packets):
                packet, offset = parse_packet(s[i:])
                i += offset
                sub_packets.append(packet)
        return OperatorPacket(version, type_id, sub_packets), i

packet, i = parse_packet(s)
print(str(packet))
print('sum versions: ', packet.sum_versions())
