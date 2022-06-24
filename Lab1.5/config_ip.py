import glob

files = glob.glob('c:\\p\\*')

list1 = set()

for fls in files:
    with open(fls) as f:
        for line in f:
            if line.find("ip address") == 1:
                list1.add(line[11:])

list2 = list(set(list1))

for i in list2:
    print(i)
