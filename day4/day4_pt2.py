import numpy as np

filter = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

with open('day4.txt', 'r') as f:
    grid = np.array([[1 if x == '@' else 0 for x in row.strip()] for row in f])
    removed, total = 0, 0
    while True:
        grid = np.pad(grid, pad_width=1, mode='constant', constant_values=0)
        h_grid, w_grid = grid.shape
        h_filter, w_filter = filter.shape
        h_conv = h_grid - h_filter + 1
        w_conv = w_grid - w_filter + 1
        conv = np.zeros((h_conv, w_conv))
        for i in range(h_conv):
            for j in range(w_conv):
                shape = grid[i:i+h_filter, j:j+w_filter]
                conv[i, j] = np.sum(shape * filter)
        conv = np.logical_and(grid[1:-1, 1:-1], conv < 4).astype(int)
        removed = np.sum(conv)
        total += removed
        if removed == 0:
            break
        grid = grid[1:-1, 1:-1] - conv
print(total)

