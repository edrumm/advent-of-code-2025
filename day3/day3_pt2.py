# Helper func to join 2 numerical values, eg 9, 8 -> 98
def join(a, b):
    return int(f'{a}{b}')


total = 0
with open('day3.txt', 'r') as f:
    for line in f:
        b = [int(n) for n in [*line.rstrip()]]
        i, jolts, n_bat = 0, 0, 12
        while n_bat > 0:
            n = len(b)
            buf = b[i:n-n_bat+1]
            jolts = join(jolts, max(buf))
            n_bat -= 1
            i = i + 1 + b[i:].index(max(buf))
        total += jolts
print(total)

