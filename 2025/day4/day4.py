input = "/home/francescos/aoc/2025/day4/input.txt"

# ==========
# READ INPUT
# ==========

with open(input) as file:
    lines = [line.strip() for line in file.readlines()]

# clean up input
clean = []
for line in lines:
    l = []
    for char in list(line):
        if char == ".":
            l.append(0)
        elif char == "@":
            l.append(1)
        else:
            raise ValueError
    clean.append(l)

# ========
# PART ONE
# ========

def get_adjacent(grid, x, y):
    adj = []
    max_x, max_y = len(grid)-1, len(grid[0])-1
    if x > 0:
        adj.append(grid[x-1][y]) # UP
    if x < max_x:
        adj.append(grid[x+1][y]) # DOWN
    if y > 0:
        adj.append(grid[x][y-1]) # LEFT
    if y < max_y:
        adj.append(grid[x][y+1]) # RIGHT
    if x > 0 and y > 0:
        adj.append(grid[x-1][y-1]) # UP LEFT
    if x > 0 and y < max_y:
        adj.append(grid[x-1][y+1]) # UP RIGHT
    if x < max_x and y > 0:
        adj.append(grid[x+1][y-1]) # DOWN LEFT
    if x < max_x and y < max_y:
        adj.append(grid[x+1][y+1]) # DOWN RIGHT
    return adj

def valid(grid, x, y):
    adj = get_adjacent(grid, x, y)
    return (adj.count(1) < 4) and (grid[x][y] == 1)

valid_count = 0
for x in range(len(clean)):
    for y in range(len(clean[0])):
        if valid(clean, x, y):
            valid_count += 1
print("Part One Answer: ", valid_count)

# ========
# PART TWO
# ========

def list_removable(grid):
    removable = []
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if valid(grid, x, y):
                removable.append((x, y))
    return removable

def has_removable(grid):
    return list_removable(grid) != []

def remove_removable(grid, removable):
    removed_individual = 0
    for x,y in removable:
        grid[x][y] = 0
        removed_individual += 1
    return grid, removed_individual

grid = clean
removed = 0
while has_removable(grid):
    removable = list_removable(grid)
    grid, removed_ind = remove_removable(grid, removable)
    removed += removed_ind

print("Part 2 answer: ", removed)
