#!/bin/python
def toBin(s):
    s = s.replace('F','0')
    s = s.replace('B','1')
    s = s.replace('L','0')
    s = s.replace('R','1')
    return int(s, 2)

with open('input') as f:
    seats = [map(toBin,(a[:7],a[7:])) for a in f.readlines()]

print(max(a*8+b for a,b in seats))
