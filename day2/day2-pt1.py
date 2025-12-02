ids = []
with open('day2.txt', 'r') as f:
    ids = f.read().split(',')
total = 0
for id in ids:
    lo, hi = tuple(int(x) for x in id.split('-') if x)
    for num in range(lo, hi+1):
        n_str = str(num)
        half = len(n_str) // 2
        if n_str[:half] == n_str[half:]:           
            total += num
print(total)

