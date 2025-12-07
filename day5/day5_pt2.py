with open('day5.txt', 'r') as f:
    ranges = [tuple(map(int, l.split('-'))) for l in f.read().split('\n\n')[0].splitlines()]

count = 0
ranges, merged = sorted(ranges, key=lambda x: x[0]), []

for lo, hi in ranges:
    if not merged or lo > merged[-1][1]:
        merged.append(list((lo, hi)))
    else:
        merged[-1][1] = max(merged[-1][1], hi)

for r in merged:
    count += 1 + r[1] - r[0]

print(count)
