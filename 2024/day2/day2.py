# ADVENT OF CODE 2024
# https://adventofcode.com/
# Day 2
# Francesco Georg Schmitt
# https://github.com/s8foschm/aoc

def read_file(name):
    lines = []
    with open(name) as file:
        for line in file:
            numbers = [int((element.strip())) for element in line.split()]
            lines.append(numbers)
    return lines

# PART ONE
def check_safe(numbers):
    inc_dec = check_increasing_decreasing(numbers)
    if inc_dec == "n":
        return False
    else:
        return check_distances(numbers)


def check_increasing_decreasing(numbers):
    if numbers[0] < numbers[1]:
        # increasing
        for i in range(2, len(numbers)):
            if numbers[i] < numbers[i - 1]:
                return "n"
        return "i"
    else:
        # decreasing
        for i in range(2, len(numbers)):
            if numbers[i] > numbers[i - 1]:
                return "n"
        return "d"


def check_distances(numbers):
    for i in range(0, len(numbers) - 1):
        dist = abs(numbers[i] - numbers[i + 1])
        if not (1 <= dist <= 3):
            return False
    return True

lines = read_file('input.txt')
safe_levels = 0
for line in lines:
    if check_safe(line): safe_levels += 1
print("Part One: ", safe_levels)

# PART TWO
def pop_without_modifying(original_list, index=-1):
    return original_list[:index] + original_list[index + 1:]


def check_dampened_safe(numbers):
    for i in range(0, len(numbers)):
        new_numbers = pop_without_modifying(numbers, i)
        if check_safe(new_numbers):
            return True
    return False

lines = read_file('input.txt')
safe_levels_with_pop = 0
for line in lines:
    if check_dampened_safe(line): safe_levels_with_pop += 1
print("Part Two: ", safe_levels_with_pop)