#!/bin/python
def product(*args):
    x = 1
    for y in args:
        x *= y
    return x

with open('input') as f:
    grid = f.read().split('\n')

xs = [1,3,5,7,1]
ys = [1,1,1,1,2]

trees = []

for xinc, yinc in zip(xs, ys):
    x = 0
    y = 0
    
    c = 0
    
    while y < len(grid)-1:
        if grid[y][x] == '#':
            c += 1
        x += xinc
        x %= len(grid[y])
        y += yinc
    trees.append(c)

print(product(*trees))
