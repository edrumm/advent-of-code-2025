devices = {}
with open('day11.txt', 'r') as f:
    for ln in f:
        d = ln.split()
        devices[d[0][:-1]] = d[1:]

def traverse(dev):
    if dev == 'out':
        return 1
    return sum([traverse(d) for d in devices[dev]])

print(traverse('you'))

