# ADVENT OF CODE 2022
# https://adventofcode.com/
# Day 10
# Francesco Georg Schmitt
# https://github.com/s8foschm/aoc2022
from abc import abstractmethod, ABC
import re


class Data:
    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.values = [1]

    def add_cycle(self, amount):
        self.cycle = self.cycle + amount

    def set_x(self, amount):
        self.x = self.x + amount

    def get_x(self):
        return self.x

    def print(self):
        print("Cycle: ", self.cycle, ", X: ", self.x)


class Instruction:
    @abstractmethod
    def getDuration(self):
        pass

    @abstractmethod
    def execute(self, data):
        pass


class NoOpInstruction(Instruction, ABC):
    def __repr__(self):
        return "NoOpInstruction"

    def getDuration(self):
        return 1

    def execute(self, data):
        # print('NoOp execute')
        data.values.append(data.get_x())
        data.add_cycle(self.getDuration())


class AddInstruction(Instruction, ABC):
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return "AddInstruction(%d)" % self.amount

    def getDuration(self):
        return 2

    def execute(self, data):
        # print('Add execute')
        data.values.append(data.get_x())
        data.set_x(self.amount)
        data.add_cycle(self.getDuration())
        data.values.append(data.get_x())


class Sprite:
    def __init__(self):
        self.position = "###....................................."

    def __repr__(self):
        return self.position

    def move(self, amount):
        if amount > 0:
            s = [*self.position]
            for (index, c) in enumerate(s):
                if c == ".":
                    continue
                elif c == "#":
                    for i in range(amount):
                        s[index] = "."
                        s[index + 3] = "#"
                        index = index + 1
                    break
        else:
            s = [*self.position]
            rs = s[::-1]
            for (index, c) in enumerate(rs):
                if c == ".":
                    continue
                elif c == "#":
                    for i in range(-amount):
                        rs[index] = "."
                        rs[index + 3] = "#"
                        index = index + 1
                    break
            s = rs[::-1]
        self.position = "".join(s)

    def update(self, position):
        preliminary = ["."]*40
        if position>1:
            preliminary[position-1] = "#"
        preliminary[position] = "#"
        if position<39:
            preliminary[position+1] = "#"
        self.position = "".join(preliminary)

    def cover(self, i):
        return self.position[i]=="#"


class CRT:
    def __init__(self):
        self.lines = ["", "", "", "", "", ""]
        self.mask = Sprite()

    def __repr__(self):
        return "\n".join(self.lines)

    def draw(self, values):
        for (index, line) in enumerate(self.lines):
            self.lines[index] = self.draw_line(index, values)

    def draw_line(self, index, values):
        prelim_line = []
        for i in range(40):
            self.mask.update(values[index*40+i])
            if self.mask.cover(i):
                prelim_line.append("#")
            else:
                prelim_line.append(" ")
        return "".join(prelim_line)



def read_file(file):
    instructions = []
    for line in file:
        if line == 'noop\n':
            instructions.append(NoOpInstruction())
        elif re.match("addx -?[0-9]+\n$", line):
            amount = int(line.split(' ')[1])
            instructions.append(AddInstruction(amount))
        else:
            raise SyntaxError('Invalid input file', line)
    return instructions


with (open('input.txt', 'r')) as file:
    instructions = read_file(file)

data = Data()
for instr in instructions:
    instr.execute(data)

# PART ONE
total = 0
for (index, value) in enumerate(data.values):
    if (index + 20) % 40 == 0:
        val = index * data.values[index - 2]
        total = total + val
print("Sum of the signal strengths: ", total)

# PART TWO

c = CRT()
c.draw(data.values)
print(c)
print("Result: BPJAZGAP")