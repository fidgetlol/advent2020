#!/bin/python
with open('input') as f:
    groups = [set(a.replace('\n','')) for a in f.read().split('\n\n')]

print(sum(len(a) for a in groups))
