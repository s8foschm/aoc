filename = "input.txt"

with open(filename) as file:
    lines = [line.strip("\n") for line in file.readlines()]

# PART ONE

# find chars and respective positions
chars = {}
width, height = len(lines[0]), len(lines)
# print(width, height)
for line_index, line in enumerate(lines):
    for col_index, char in enumerate(line):
        if char != "." and not char.isdigit():
            chars.update({(line_index, col_index): char})
# print(chars)

# find numbers
# part numbers are not unique, so a list needs to be used instead of a dictionary
numbers = []
for line_index, line in enumerate(lines):
    temp_number, temp_positions = [], []
    for col_index, char in enumerate(line):
        if char.isdigit():
            # append digits to temp number
            temp_number.append(char)
            temp_positions.append((line_index, col_index))
        else:
            # assemble number if no digits are left
            if temp_number:
                number = int(''.join(temp_number))
                numbers.append([number, temp_positions])
                temp_number, temp_positions = [], []
        # assemble digits if number is left
        if col_index == len(line) - 1 and temp_number:
            number = int(''.join(temp_number))
            numbers.append([number, temp_positions])
            temp_number, temp_positions = [], []


# print(numbers)

def get_neighbors(positions):
    neighbors = []
    for row, column in positions:
        # vertical
        if row > 0:
            neighbors.append((row - 1, column))
        if row < height - 1:
            neighbors.append((row + 1, column))
        # horizontal
        if column > 0 and (row, column - 1) not in positions:
            neighbors.append((row, column - 1))
        if column < width - 1 and (row, column + 1) not in positions:
            neighbors.append((row, column + 1))
        # diagonal
        if row > 0 and column > 0:
            neighbors.append((row - 1, column - 1))
        if row > 0 and column < width - 1:
            neighbors.append((row - 1, column + 1))
        if row < height - 1 and column > 0:
            neighbors.append((row + 1, column - 1))
        if row < height - 1 and column < width - 1:
            neighbors.append((row + 1, column + 1))
    return list(set(neighbors))


# every number that is adjacent to a symbol is a part number
part_numbers = []
for number, occupied_positions in numbers:
    curr_neighbors = get_neighbors(occupied_positions)
    for neighbor in curr_neighbors:
        if neighbor in chars:
            part_numbers.append(number)
            # this following break statement ensures that even numbers adjacent to multiple symbols are only counted once
            break
# duplicates cannot be removed from part numbers because they are not necessarily unique

# print(part_numbers)
print(sum(part_numbers))

# PART TWO
# a gear is a "*" symbol adjacent to exactly two numbers
# the gear ratio is the product of these two numbers

# find gears
stars = []
for line_index, line in enumerate(lines):
    for col_index, char in enumerate(line):
        if char == "*":
            stars.append((line_index, col_index))
# find adjacent numbers
gears, ratios = {}, []
for row, column in stars:
    star_neighbors = get_neighbors([(row, column)])
    neighboring_numbers = []
    found_positions = []
    for star_neighbor in star_neighbors:
        for number, occupied_positions in numbers:
            if star_neighbor in occupied_positions and (list(set(found_positions) & set(occupied_positions)) == []):
                found_positions = found_positions + occupied_positions
                neighboring_numbers.append(number)
            if len(neighboring_numbers) == 2:
                gears.update({(row, column): neighboring_numbers})
                neighboring_numbers = []
                found_positions = []
                break
print(gears)

final_values = []
for (row, column), ratios in gears.items():
    assert(len(ratios) == 2)
    value = ratios[0] * ratios[1]
    final_values.append(value)

print(sum(final_values))
