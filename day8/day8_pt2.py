from scipy.cluster.hierarchy import DisjointSet
from itertools import combinations
from math import sqrt, prod


# Helper func - return the 3D euclidean distance between 2 points
def dist3d(p1, p2):
    x1, y1, z1 = p1; x2, y2, z2 = p2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


with open('day8.txt', 'r') as f:
   boxes = [tuple(map(int, ln.split(','))) for ln in f.readlines()]

distances = sorted(combinations(boxes, 2), key=lambda x: dist3d(*x))
ds = DisjointSet(boxes)

for d in distances:
    ds.merge(*d)
    if ds.n_subsets == 1:
        total = prod(next(zip(*d)))
        break

print(total)

