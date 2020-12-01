with open('input') as f:
    nums = set(map(int, f.readlines()))

for n in nums:
    r =  2020 - n
    for n2 in nums:
        if 2020 - (n + n2) in nums:
            print(n * n2 * (2020-(n+n2)))
            quit()
