
filenames = []

with open('carfnames.txt', 'r') as f:
    fname1 = f.read()
    filenames.append(fname1)

list1 = filenames[0].split('\n')

dat = []

for fn in list1:
    if len(fn) > 2:
        with open(fn,'r') as f:
            st = f.read()
            if len(st) > 2:
                dat.append(st)

master = []

for d in dat:
    list2 = d.split('\n')
    master = master + list2

master.sort()

for m in master:
    if len(m) > 2:
        print(m)


