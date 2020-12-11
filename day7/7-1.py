#!/bin/python
from collections import defaultdict
from re import findall

def contains(graph, start, query, checked=set()):
    if 'no other' in graph[start]:
        return False
    elif query in graph[start]:
        return True
    else:
        return any([contains(graph, s, query, checked) for s in graph[start]])
        print('ERR')

with open('input') as f:
    rules = f.readlines()

ruleGraph = defaultdict(set)

for rule in rules:
    bags = findall('\w+ \w+(?= bag)', rule)
    ruleGraph[bags[0]] = set(bags[1:])


answer = [a for a in ruleGraph.keys() if contains(ruleGraph, a, 'shiny gold')]
print(answer)
print(len(answer))
