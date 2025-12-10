from collections import deque
from itertools import combinations

class Machine:
    def __init__(self, lights, buttons, jolts):
        self.lights = lights
        self.buttons = buttons
        self.jolts = jolts

machines = []
with open('day10.txt', 'r') as f:
    for ln in f:
        m = ln.rstrip().split(' ')
        l = m[0][1:-1].replace('.', '0').replace('#', '1')
        b = []
        for button in m[1:-1]:
            bits = len(l)*['0']
            for i in [int(x) for x in button[1:-1].split(',')]:
                bits[i] = '1'
            b.append(int(''.join(bits), base=2))
        l = int(l, base=2)
        j = list(map(int, m[-1][1:-1].split(',')))
        machines.append(Machine(l, b, j))

count = 0
for machine in machines:
    init = 0
    visited = {init}
    queue = deque([(init, 0)])
    while queue:
        prev, n = queue.popleft()
        if prev == machine.lights:
            count += n
            break
        for b in machine.buttons:
            xor = prev ^ b
            if xor not in visited:
                visited.add(xor)
                queue.append((xor, n + 1))

print(count)

