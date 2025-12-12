from math import prod

with open('day12.txt', 'r') as f:
    lines = f.read().split('\n')

present_size = [sum(ln.count('#') for ln in lines[i:i+3]) for i in range(1, 27, 5)]

count = 0
for ln in lines[30:]:
    delim = ln.index(':')  # sanity check: probably could be hardcoded as ln[:5] since most areas seem to consist of 2*2-digit numbers
    max_area = prod([int(n) for n in ln[:delim].split('x')])
    presents = [int(n) for n in ln[delim+1:].split()]
    if max_area - sum(presents[i] * present_size[i] for i in range(6)) >= 0:
        count += 1

print(count)
