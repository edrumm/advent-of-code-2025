with open('day9.txt', 'r') as f:
    tiles = [tuple(map(int, ln.split(','))) for ln in f.readlines()]

a_max, n = 0, len(tiles)
for i in range(n):
    x1, y1 = tiles[i]
    for j in range(i + 1,n):
        x2, y2 = tiles[j]
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        a_max = max(a_max, area)

print(a_max)

