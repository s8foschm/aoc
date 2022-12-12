# ADVENT OF CODE 2022
# https://adventofcode.com/
# Day 12
# Francesco Georg Schmitt
# https://github.com/s8foschm/aoc2022
from enum import Enum
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement


class StepStatus(Enum):
    IMPOSSIBLE = 1
    FORWARD = 2
    BACKWARD = 3
    SAME = 4

    @property
    def __repr__(self):
        if self == 1:
            return "Impossible"
        elif self == 2:
            return "Forward"
        elif self == 3:
            return "Backward"
        elif self == 4:
            return "Same"


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    @property
    def __repr__(self):
        if self == 1:
            return "North"
        elif self == 2:
            return "EAST"
        elif self == 3:
            return "EAST"
        elif self == 4:
            return "WEST"


class Heightmap:
    def __init__(self, lines):
        self.map = lines
        for (y, line) in enumerate(lines):
            for (x, char) in enumerate(line):
                if char == "S":
                    self.start = (x, y)
                elif char == "E":
                    self.target = (x, y)

    def __repr__(self):
        template = '{0.map} {0.start} {0.target}'
        return template.format(self)

    def get(self, x, y):
        return self.map[x][y]

    def get_neighbor(self, x, y, direction):
        if direction == Direction.WEST:
            if y == 0:
                return None
            else:
                return self.map[x][y - 1]
        elif direction == Direction.EAST:
            if y >= len(self.map[0]) - 1:
                return None
            else:
                return self.map[x][y + 1]
        elif direction == Direction.NORTH:
            if x == 0:
                return None
            else:
                return self.map[x - 1][y]
        elif direction == Direction.SOUTH:
            if x >= len(self.map) - 1:
                return None
            else:
                return self.map[x + 1][y]

    def get_neighbors(self, x, y):
        neighbors = []
        for direction in list(Direction):
            if self.get_neighbor(x, y, direction):
                neighbors.append((self.get_neighbor(x, y, direction), direction))
        return neighbors
        # return [(self.get_neighbor(x, y, direction), direction) for direction in list(Direction)]

    def move_possible(self, x, y, direction):
        current = self.get(x, y)
        neighbor = self.get_neighbor(x, y, direction)
        if neighbor:
            nA, nB = ord(current), ord(neighbor)
            if nA == 69:  # E
                if nB == 122:  # z
                    return StepStatus.BACKWARD
                else:
                    return StepStatus.IMPOSSIBLE
            elif nB == 69:  # E
                if nA == 122:  # z
                    return StepStatus.FORWARD
                else:
                    return StepStatus.IMPOSSIBLE
            elif nA == 83:  # S
                if nB == 97:  # a
                    return StepStatus.FORWARD
                else:
                    return StepStatus.IMPOSSIBLE
            elif nB == 83:  # S
                return StepStatus.IMPOSSIBLE
            else:
                if nB == nA + 1:
                    return StepStatus.FORWARD
                elif nB == nA - 1:
                    return StepStatus.BACKWARD
                elif nA == nB:
                    return StepStatus.SAME
                else:
                    return StepStatus.IMPOSSIBLE

    def generate_matrix(self):
        matrix = []
        for (x, line) in enumerate(self.map[:-1]):
            matrix_line = []
            for (y, element) in enumerate(line):
                matrix_line.append(1)
                if self.move_possible(x, y, Direction.EAST) == StepStatus.IMPOSSIBLE:
                    matrix_line.append(0)
                else:
                    matrix_line.append(1)
            matrix.append(matrix_line[:-1])
            matrix_line = []
            for (y, element) in enumerate(line):
                if self.move_possible(x, y, Direction.SOUTH) == StepStatus.IMPOSSIBLE:
                    matrix_line.append(0)
                else:
                    matrix_line.append(1)
                matrix_line.append(0)
            matrix.append(matrix_line[:-1])
        matrix_line = []
        last_line = self.map[-1]
        for (y, element) in enumerate(last_line):
            matrix_line.append(1)
            if self.move_possible(len(self.map) - 1, y, Direction.EAST) == StepStatus.IMPOSSIBLE:
                matrix_line.append(0)
            else:
                matrix_line.append(1)
        matrix.append(matrix_line[:-1])
        return matrix


def parse_file(file):
    lines = file.readlines()
    return Heightmap([line[:-1] for line in lines])

def convert_to_matrix_format(x, y):
    new_X = x * 2
    # if new_X < 0: new_X = 0
    new_Y = y * 2
    # if new_Y < 0: new_Y = 0
    return new_X, new_Y

with (open('test_input.txt', 'r')) as file:
    map = parse_file(file)
    matrix = map.generate_matrix()
    print(len(matrix), len(matrix[0]))
    #for line in matrix:
    #    print(line)
    print(map.start, map.target)

    grid = Grid(matrix=matrix)
    new_start_X, new_start_Y = convert_to_matrix_format(map.start[0], map.start[1])
    new_end_X, new_end_Y = convert_to_matrix_format(map.target[0], map.target[1])
    start = grid.node(new_start_X, new_start_Y)
    end = grid.node(new_end_X, new_end_Y)
    print(new_start_X, new_start_Y)
    print(new_end_X, new_end_Y)
    #
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)
    print('operations:', runs, 'path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=end))

    print("Actual Path Length: ", (len(path) // 2))
