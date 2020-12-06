#!/bin/python
def toBin(s):
    s = s.replace('F','0')
    s = s.replace('B','1')
    s = s.replace('L','0')
    s = s.replace('R','1')
    return int(s, 2)

def main():
    with open('input') as f:
        seats = [map(toBin,(a[:7],a[7:])) for a in f.readlines()]


    seats = set(a*8+b for a,b in seats)
    for seat in seats:
        if seat+1 not in seats:
            print(seat+1)
            return

if __name__ == '__main__':
    main()
