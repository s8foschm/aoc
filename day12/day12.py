# ADVENT OF CODE 2022
# https://adventofcode.com/
# Day 12
# Francesco Georg Schmitt
# https://github.com/s8foschm/aoc2022
import time
from enum import Enum
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
import networkx as nx
import matplotlib.pyplot as plt


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

    def get_neighbor_index(self, index, direction):
        rows = len(self.map)
        cols = len(self.map[0])
        if direction == Direction.WEST:
            if index % cols == 0:
                return None
            else:
                return index - 1
        elif direction == Direction.EAST:
            if index + 1 % cols == 0:
                return None
            else:
                return index + 1
        elif direction == Direction.NORTH:
            if index < cols:
                return None
            else:
                return index - cols
        elif direction == Direction.SOUTH:
            if index > cols * (rows - 1):
                return None
            else:
                return index + cols

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
                elif nB <= nA:  # not possible here because this needs to be directional
                    return StepStatus.FORWARD
                elif nA == nB + 1:
                    return StepStatus.BACKWARD
                elif nA == nB:
                    return StepStatus.SAME
                else:
                    return StepStatus.IMPOSSIBLE
        else:
            return StepStatus.IMPOSSIBLE

    def moves_possible(self, x, y):
        moves = []
        for direction in list(Direction):
            if self.move_possible(x, y, direction) != StepStatus.IMPOSSIBLE:
                moves.append(direction)
        return moves

    # dead code from an unsuccessful attempt at solving this without graphs, see below
    """def generate_matrix(self):
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
        return matrix"""

    def generate_graph(self):
        G = nx.DiGraph()
        for (x, line) in enumerate(self.map):
            for (y, element) in enumerate(line):
                G.add_node(x * len(line) + y, label=element, weight=ord(element))
        for (x, line) in enumerate(self.map):
            for (y, element) in enumerate(line):
                curr_index = x * len(line) + y
                nodeA = curr_index
                for move in self.moves_possible(x, y):
                    nodeB = self.get_neighbor_index(curr_index, move)
                    status = map.move_possible(x, y, move)
                    if status == StepStatus.FORWARD:
                        G.add_edge(curr_index, self.get_neighbor_index(curr_index, move))
                    elif status == StepStatus.BACKWARD:
                        G.add_edge(nodeB, nodeA)
                    elif status == StepStatus.SAME:
                        G.add_edge(nodeA, nodeB)
                        G.add_edge(nodeB, nodeA)
        return G


def parse_file(file):
    lines = file.readlines()
    return Heightmap([line[:-1] for line in lines])


def convert_to_matrix_format(x, y):
    new_X = x * 2
    # if new_X < 0: new_X = 0
    new_Y = y * 2
    # if new_Y < 0: new_Y = 0
    return new_X, new_Y


with (open('input.txt', 'r')) as file:
    st = time.time()
    print("Parsing file.")
    map = parse_file(file)

    print("Generating graph.")
    gr = map.generate_graph()
    nx.draw(gr, with_labels=True)
    plt.show()
    print("Generated graph with {} nodes and {} edges.".format(gr.number_of_nodes(), gr.number_of_edges()))
    original_dict = nx.get_node_attributes(gr, "label")
    reverse_dict = dict((new_val, new_key) for new_key, new_val in original_dict.items())
    print("Finding path.")
    path = nx.dijkstra_path(gr, reverse_dict.get("S"), reverse_dict.get("E"))
    path_by_letters = [original_dict.get(val) for val in path]
    print(path)
    print(path_by_letters)
    print(len(path) - 1)
    duration = time.time() - st
    print("Execution time: ", duration)
    # answer 499 is too high -> path too long

    # the following is dead code, remaining from the previous attempt of solving this without graphs, using a matrix
    # representing walls instead, which won't work because here, legal moves are not symmetric
    """matrix = map.generate_matrix()
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
    finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)
    print('operations:', runs, 'path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=end))

    print("Actual Path Length: ", (len(path) // 2))"""
