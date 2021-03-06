#!/bin/python
from re import split

with open('input') as f:
    lines = f.readlines()

c = 0

for line in lines:
    rule, line = line.split(':')
    low, high, char = split('[- ]',rule)
    i = line.count(char)
    if (line[int(low)] == char) != (line[int(high)] == char):
        c += 1

print(c)
