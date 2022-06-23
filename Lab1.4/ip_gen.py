import random
import ipaddress


# net1 = ipaddress.IPv4Network((random.randint(0x0b000000, 0xdf000000), random.randint(8, 24)), strict=False)
# print(net1)
class Networkgen(ipaddress.IPv4Network):
    def __init__(self, l_min=8, l_max=24):
        ipaddress.IPv4Network.__init__(self, (random.randint(0x0b000000, 0xdf000000), random.randint(l_min, l_max)), strict=False)

    def key_value(self):
        return int(self.network_address) + (int(self.netmask) << 32)

    def regular(self):
        return self.is_global or not (self.is_private or self.is_loopback or self.is_reserved or self.is_multicast)

def sortlist(x):
    return x.key_value()

list = []


while len(list) < 10:
    n1 = Networkgen()
    if n1.regular():
        list.append(n1)


for i in sorted(list, key=sortlist):
    print(i)

