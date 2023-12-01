# ADVENT OF CODE 2022
# https://adventofcode.com/
# Day 6
# Francesco Georg Schmitt
# https://github.com/s8foschm/aoc2022


# ========== PART ONE ==========
def same(a, b, c, d):
    return a == b or a == c or a == d or b == c or b == d or c == d


with open('input.txt', 'r') as file:
    line = file.readline()
    chars = [*line]

    for (ind, cha) in enumerate(chars):
        if not (same(cha, chars[ind + 1], chars[ind + 2], chars[ind + 3])):
            print(ind + 4)
            break


# ========== PART TWO ==========
def flexible_same(l):
    known = []
    for s in l:
        if s in known:
            return True
        else:
            known.append(s)
    return False


with open('input.txt', 'r') as file:
    line = file.readline()
    chars = [*line]

    for (ind, cha) in enumerate(chars):
        if not (flexible_same(chars[ind:ind+14])):
            print(ind+14)
            break