def parse_input(filename):
    lines = []
    with open(filename) as file:
        lines = file.readlines()
    return lines


def get_starting_position(maze):
    for row, line in enumerate(maze):
        for column, element in enumerate(line):
            if element == "^":
                return row, column, "UP"
            if element == "v":
                return row, column, "DOWN"
            if element == ">":
                return row, column, "LEFT"
            if element == "<":
                return row, column, "RIGHT"


def turn_right(direction):
    match direction:
        case "UP":
            return "RIGHT"
        case "RIGHT":
            return "DOWN"
        case "DOWN":
            return "LEFT"
        case "LEFT":
            return "UP"
        case _:
            raise ValueError


def get_next_position(direction, position, dimensions):
    row, column = position
    total_rows, total_columns = dimensions
    match direction:
        case "UP":
            if row > 0:
                return row - 1, column
            else:
                return row, column
        case "DOWN":
            if row < total_rows - 1:
                return row + 1, column
            else:
                return row, column
        case "LEFT":
            if column > 0:
                return row, column - 1
            else:
                return row, column
        case "RIGHT":
            if column < total_columns - 1:
                return row, column + 1
            else:
                return row, column
        case _:
            raise ValueError


def get_next_element(grid, direction, position, dimensions):
    row, column = get_next_position(direction, position, dimensions)
    return row, column, grid[row][column]


def walk(grid, position, direction, dimensions):
    new_row, new_column, new_element = get_next_element(grid, direction, position, dimensions)
    if (new_row, new_column) == position:
        # position hasn't changed because we're at the edge of the board
        return grid, position, direction, dimensions, True
    elif new_element == "." or new_element == "^" or new_element == "v" or new_element == ">" or new_element == "<":
        return grid, (new_row, new_column), direction, dimensions, False
    elif new_element == "#":
        return grid, position, turn_right(direction), dimensions, False


grid = parse_input("input.txt")
dimensions = len(grid), len(grid[0].strip())
start_row, start_column, direction = get_starting_position(grid)
done = False
position = start_row, start_column
step = 0
positions = [position]
while not done:
    # print(step, position)
    grid, position, direction, dimensions, done = walk(grid, position, direction, dimensions)
    positions.append(position)
    step += 1
positions = list(set(positions))
print("Part One: ", len(positions))
