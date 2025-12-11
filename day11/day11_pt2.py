from functools import cache

devices = {}
with open('day11.txt', 'r') as f:
    for ln in f:
        d = ln.split()
        devices[d[0][:-1]] = d[1:]

@cache
def traverse(src_dev, tgt_dev):
    if not src_dev:
        return 0
    elif src_dev == tgt_dev:
        return 1
    return sum([traverse(d, tgt_dev) for d in devices.get(src_dev, [])])

print(traverse('svr', 'fft') * traverse('fft', 'dac') * traverse('dac','out'))

