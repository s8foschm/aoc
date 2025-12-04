input = "/home/francescos/aoc/2025/day2/input.txt"

# ==========
# READ INPUT
# ==========

ranges =  []

with open(input) as file:
    contents = file.read().splitlines()[0].split(",") # file contains only one line
    for element in contents:
        numbers = element.split("-")
        lower, upper = int(numbers[0]), int(numbers[1])
        ranges.append((lower, upper))

# ========
# PART ONE
# ========

invalid_ids = []

def check_number(number):
    chars = len(str(number))
    if chars % 2 == 0:
        upper_half = number // (10 ** (chars/2))
        lower_half = number % (10 ** (chars/2))
        return (upper_half == lower_half)
    return False

def check_range(lower, upper):
    for i in range(lower, upper+1):
        if check_number(i):
            invalid_ids.append(i)
    return invalid_ids

invalid_ids_overall = []
for lower, upper in ranges:
    invalid_ids_overall.extend(check_range(lower, upper))

#print(invalid_ids_overall)
print("Part One Answer: ", sum(invalid_ids_overall))

# ========
# PART TWO
# ========

invalid_ids = []

def check_number_2(number):
    chars = len(str(number))
    invalid_internal = set()
    for i in range(1, (chars//2)+1):
        segments = [int(str(number)[k:k+i]) for k in range(0, len(str(number)), i)]
        if all(x == segments[0] for x in segments): #  if all segments are equal (or equal to the first one)
            invalid_internal.add(number)
    return invalid_internal

def check_range_2(lower, upper):
    for i in range(lower, upper+1):
        if check_number_2(i):
            invalid_ids.append(i)
    return invalid_ids

for lower, upper in ranges:
    invalid_ids_overall = set()
    current = set(check_range_2(lower, upper))
    invalid_ids_overall = invalid_ids_overall.union(current)

print("Part Two Answer: ", sum(list(invalid_ids_overall)))