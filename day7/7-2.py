#!/bin/python
from re import findall

def total(graph, start):
    if 'no' == graph[start][0][0]:
        return 1
    return 1 + sum(int(a)*total(graph, b) for a,b in graph[start])

with open('testin') as f:
    rules = f.readlines()

ruleGraph = {}

for rule in rules:
    bags = findall('(?:\d )?\w+ \w+(?= bag)', rule)
    ruleGraph[bags[0]] = [a.split(' ',1) for a in bags[1:]]

print(total(ruleGraph, 'dark blue'))

