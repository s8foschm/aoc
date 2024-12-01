# ADVENT OF CODE 2024
# https://adventofcode.com/
# Day 1
# Francesco Georg Schmitt
# https://github.com/s8foschm/aoc

# PARSING INPUT FILE
with open("input.txt") as file:
    l1, l2 = [], []
    for line in file:
        s = line.split()
        l1.append(int(s[0].strip()))
        l2.append(int(s[1].strip()))

# PART ONE
sl1, sl2 = sorted(l1), sorted(l2)
newlist = []
for a, b in zip(sl1, sl2):
    newlist.append(abs(a-b))
print("Part One: ", sum(newlist))

# PART TWO
sim = 0
for a in l1:
    sim += a*l2.count(a)
print("Part Two: ", sim)
