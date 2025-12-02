with open('day2.txt', 'r') as f:
    ids = f.read().split(',')
total = 0
for id in ids:
    lo, hi = tuple(int(x) for x in id.split('-') if x)
    for num in range(lo, hi+1):
        n_str = str(num)
        n_len = len(n_str)
        for block in range(1, n_len // 2 + 1):
            reps = n_len // block
            if n_str[:block] * reps == n_str:
                total += num
                break
print(total)

