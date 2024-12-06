# ADVENT OF CODE 2024
# https://adventofcode.com/
# Day 4
# Francesco Georg Schmitt
# https://github.com/s8foschm/aoc


def count_word_occurrences(grid, woßrd):
    rows = len(grid)
    cols = len(grid[0])

    # Directions: (dx, dy)
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Diagonal Down-Right
        (1, -1),  # Diagonal Down-Left
        (-1, 1),  # Diagonal Up-Right
        (-1, -1)  # Diagonal Up-Left
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_direction(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_direction(x, y, dx, dy):
                    count += 1  # Count this occurrence

    return count


def count_x_mas(grid):
    count = 0
    for n_row, row in enumerate(grid):
        for n_col, col in enumerate(row):
            if col == "A":
                if 1 <= n_row <= len(grid) - 2 and 1 <= n_col <= len(grid[0]) - 2:
                    # check pattern:
                    # M.S
                    # .A.
                    # M.S
                    if grid[n_row - 1][n_col - 1] == grid[n_row + 1][n_col - 1] == "M" and grid[n_row - 1][n_col + 1] == \
                            grid[n_row + 1][n_col + 1] == "S":
                        count += 1
                    # check pattern:
                    # M.M
                    # .A.
                    # S.S
                    if grid[n_row - 1][n_col - 1] == grid[n_row - 1][n_col + 1] == "M" and grid[n_row + 1][n_col - 1] == \
                            grid[n_row + 1][n_col + 1] == "S":
                        count += 1
                    # check pattern:
                    # S.M
                    # .A.
                    # S.M
                    if grid[n_row - 1][n_col - 1] == grid[n_row + 1][n_col - 1] == "S" and grid[n_row - 1][n_col + 1] == \
                            grid[n_row + 1][n_col + 1] == "M":
                        count += 1
                    # check pattern:
                    # S.S
                    # .A.
                    # M.M
                    if grid[n_row - 1][n_col - 1] == grid[n_row - 1][n_col + 1] == "S" and grid[n_row + 1][n_col - 1] == \
                            grid[n_row + 1][n_col + 1] == "M":
                        count += 1
    return count


def parse_file(name):
    content = []
    with open(name) as file:
        lines = file.readlines()
        for line in lines:
            curr_line = []
            for char in line.strip():
                curr_line.append(char)
            content.append(curr_line)
    return content


content = parse_file("input.txt")
print("Part One: ", count_word_occurrences(content, 'XMAS'))
print("Part Two: ", count_x_mas(content))
