from functools import cache


with open('day7.txt', 'r') as f:
    grid = f.readlines()

@cache
def traverse(i, j):
    if i == len(grid) - 1:
        return 1
    i += 1
    if grid[i][j] == '^':
        return traverse(i, j-1) + traverse(i, j+1)
    else:
        return traverse(i, j)


print(traverse(1, grid[0].index('S')))
