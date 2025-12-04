input = "/home/francescos/aoc/2025/day3/test_input.txt"

from itertools import combinations
import time

start = time.time()

# ==========
# READ INPUT
# ==========

numbers = []

with open(input) as file:
    for line in file:
        numbers.append(int(line))

# ========
# PART ONE
# ========

def find_largest_jolt(number):
    digits = [int(digit) for digit in list(str(number))]
    largest = 0
    for i, d1 in enumerate(digits):
        for j, d2 in enumerate(digits[i+1:]):
            jolt = d1*10 + d2
            if jolt > largest:
                largest = jolt
    return largest

largest = []
for number in numbers:
    largest.append(find_largest_jolt(number))
print("Part One Answer: ", sum(largest))

# ========
# PART TWO
# ========

# joltages are now 12 digits long instead of 2.

def find_largest_k_jolt(number, k):

    digits = str(number)
    max_subnumber = 0
    for comb in combinations(digits, k):
        current_subnumber = int("".join(comb))
        if current_subnumber > max_subnumber:
            max_subnumber = current_subnumber

    return max_subnumber



largest = []
k = 12
amount = len(numbers)
for index, number in enumerate(numbers):
    print("working part 2 on numer {} of {}".format(index+1, amount))
    largest.append(find_largest_k_jolt(number, k))
#print(largest)
print("Part Two Answer: ", sum(largest))

end = time.time()
print(f"Total runtime: {end - start} seconds")
