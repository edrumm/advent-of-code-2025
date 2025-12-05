with open('day5.txt', 'r') as f:
    lines = f.read().split('\n\n')
    ranges = [tuple(map(int, l.split('-'))) for l in lines[0].splitlines()]
    ids = [int(l) for l in lines[1].splitlines()]

count = 0

for id in ids:
    for rng in ranges:
        lo, hi = rng
        if lo <= id <= hi:
            count += 1
            break
        
print(count)
