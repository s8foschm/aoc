# ADVENT OF CODE 2022
# https://adventofcode.com/
# Day 8
# Francesco Georg Schmitt
# https://github.com/s8foschm/aoc2022


# UTILS
def read_file(file):
    lines = file.readlines()
    rows, cols = len(lines), len(lines[0]) - 1
    grid = [[0] * cols] * rows
    for (index, line) in enumerate(lines):
        grid[index] = [*line][:-1]
    return grid, rows, cols


def get_way_to_edge(grid, x, y, rows, cols, direction):
    way = []
    if x > rows or y > cols:
        raise ValueError
    if direction == 'NORTH':
        for i in range(x - 1, -1, -1):
            way.append((i, y))
        return way
    elif direction == 'SOUTH':
        for i in range(x + 1, rows, 1):
            way.append((i, y))
        return way
    elif direction == 'WEST':
        for i in range(y - 1, -1, -1):
            way.append((x, i))
        return way
    elif direction == 'EAST':
        for i in range(y + 1, cols, 1):
            way.append((x, i))
        return way
    else:
        raise ValueError("Unknown direction!", direction)


def get_values(grid, path):
    values = []
    for (x, y) in path:
        values.append(grid[x][y])
    return values


def visible_direction(grid, x, y, rows, cols, direction):
    values = get_values(grid, get_way_to_edge(grid, x, y, rows, cols, direction))
    for val in values:
        if val >= grid[x][y]:
            return False
    return True


def visible(grid, x, y, rows, cols):
    if x == 0 or y == 0 or x == rows or y == rows:
        return True
    else:
        return visible_direction(grid, x, y, rows, cols, 'NORTH') or \
               visible_direction(grid, x, y, rows, cols, 'SOUTH') or \
               visible_direction(grid, x, y, rows, cols, 'WEST') or \
               visible_direction(grid, x, y, rows, cols, 'EAST')


def scenic_score(grid, x, y, rows, cols):
    dist_north = view_distance_single_direction(grid, x, y, rows, cols, 'NORTH')
    dist_south = view_distance_single_direction(grid, x, y, rows, cols, 'SOUTH')
    dist_west = view_distance_single_direction(grid, x, y, rows, cols, 'WEST')
    dist_east = view_distance_single_direction(grid, x, y, rows, cols, 'EAST')
    return dist_north * dist_south * dist_west * dist_east


def view_distance_single_direction(grid, x, y, rows, cols, direction):
    values = get_values(grid, get_way_to_edge(grid, x, y, rows, cols, direction))
    trees = 1
    height = grid[x][y]
    total = True
    for val in values:
        if val >= height:
            total = False
            break
        else:
            trees = trees + 1
    if total:  # if you can see until the edge, remove one because the edge itself is not a tree
        trees = trees - 1
    return trees


# PART ONE
def count_visible(grid, rows, cols):
    count = 0
    for i in range(rows):
        for j in range(cols):
            if visible(grid, i, j, rows, cols):
                count = count + 1
    return count


# PART TWO
def find_highest_scenic_score(grid, rows, cols):
    top_score = 0
    for i in range(rows):
        for j in range(cols):
            if scenic_score(grid, i, j, rows, cols) > top_score:
                top_score = scenic_score(grid, i, j, rows, cols)
    return top_score


# MAIN
with open('input.txt', 'r') as file:
    grid, rows, cols = read_file(file)

    print(count_visible(grid, rows, cols))

    print(find_highest_scenic_score(grid, rows, cols))
