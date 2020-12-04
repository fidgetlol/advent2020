#!/bin/python
from re import search

def check_for(substrs, string):
    for substr in substrs:
        if not search(substr, string):
            return False        
    return True

with open('input') as f:
    input = f.read().split('\n\n')

fields = [r'byr:(19[2-9]\d|200[0-2])([ \n]|$)',r'iyr:20(1\d|20)([ \n]|$)',r'eyr:20(2\d|30)([ \n]|$)',
          r'hgt:((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)([ \n]|$)',r'hcl:#[0-9a-f]{6}([ \n]|$)',
          r'ecl:(amb|blu|brn|gry|grn|hzl|oth)([ \n]|$)',r'pid:\d{9}([ \n]|$)']
print(len([pp for pp in input if check_for(fields, pp)]))
