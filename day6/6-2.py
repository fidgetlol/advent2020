#!/bin/python
with open('input') as f:
    groups = [set.intersection(*(set(b) for b in a.split('\n') if b)) for a in f.read().split('\n\n')]

print(sum(len(a) for a in groups))
