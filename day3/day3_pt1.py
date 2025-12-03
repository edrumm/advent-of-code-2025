# Helper func to join 2 numerical values, eg 9, 8 -> 98
def join(a, b):
    return int(f'{a}{b}')


total = 0
with open('day3.txt', 'r') as f:
    for line in f:
        b = [int(n) for n in [*line.rstrip()]]
        n = len(b)
        max_jolts = 0
        for i in range(n - 1):
            for j in range(i, n - 1):
                max_jolts = max(max_jolts, join(b[i], b[j+1]))
        total += max_jolts
print(total)

