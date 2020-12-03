#!/bin/python
with open('input') as f:
    grid = f.read().split('\n')

x = 0
c = 0

for line in grid[:-1]:  # last line empty
    if line[x] == '#':
        c += 1
    x += 3
    x %= len(line)

print(c)
