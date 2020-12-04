#!/bin/python
def check_for(substrs, string):
    for substr in substrs:
        if substr not in string:
            return False
    return True

with open('input') as f:
    input = f.read().split('\n\n')

fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
print(len([pp for pp in input if check_for(fields, pp)]))
