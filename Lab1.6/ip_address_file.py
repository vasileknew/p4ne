import glob
import re
import ipaddress

files = glob.glob('c:\\p\\*')

list1 = []

for fls in files:
    with open(fls) as f:
        for line in f:
            if re.match("^ ip address ([0-9.]+) ([0-9.]+)", line):
                string = re.match("^ ip address ([0-9.]+) ([0-9.]+)", line)
                list1.append(ipaddress.IPv4Address(str(string.group(1))))


list2 = list(set(list1))

for i in list2:
    print(i)
