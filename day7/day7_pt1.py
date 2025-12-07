with open('day7.txt', 'r') as f:
    grid = f.readlines()

splits = 0
beams = {grid[0].index('S')}
for row in grid[1:]:
    next_beams = set()
    for b in beams:
        if row[b] == '^':
            next_beams.add(b - 1)
            next_beams.add(b + 1)
            splits += 1
        else:
            next_beams.add(b)
    beams = next_beams

print(splits)
