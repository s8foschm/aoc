import re


class Stacks:

    def __init__(self):
        # self.stacks: list[list[str]] = [[], [], [], []]
        self.stacks: list[list[str]] = [[], [], [], [], [], [], [], [], [], []]

    def is_empty(self, index):
        return len(self.stacks[index]) == 0

    def add_element(self, index, element):
        if element != "":
            self.stacks[index].insert(0, element)

    def append_element(self, index, element):
        if element != "":
            self.stacks[index].append(element)

    def remove_element(self, index):
        if self.is_empty(index):
            return ""
        else:
            return self.stacks[index].pop(0)

    def get_stacks(self):
        return self.stacks

    def remove_numbers(self):
        for stack in self.stacks:
            if stack != []:
                stack.pop()

    def read_line(self, line):
        split = [(line[i:i + 4]) for i in range(0, len(line), 4)]
        for (index, element) in enumerate(split):
            if element == "    ":
                continue
            self.append_element(index, element[1])

    def move_element(self, origin, target):
        self.add_element(target, self.remove_element(origin))

    def move_elements(self, amount, origin, target):
        # move the elements to a buffer stack first, reversing the order
        for i in range(0, amount):
            self.move_element(origin, 9)
        # then, move the elements to the actual target stack
        # reversing the order again, therefore recreating the original order
        for i in range(0, amount):
            self.move_element(9, target)


def read_stacks(file, stacks):
    for line in file:
        if line != "\n":
            stacks.read_line(line)
        else:
            break
    stacks.remove_numbers()


def read_ops(file):
    instructions = []
    for line in file:
        if line[len(line) - 1] == "\n":
            line = line[:len(line) - 1]  # remove \n
        instruction = re.split(" ", line)
        instruction.pop(0)  # remove words
        instruction.pop(1)
        instruction.pop(2)
        instructions.append(instruction)
    return instructions


def nice_output(stacks):
    output = ""
    for list in stacks.get_stacks():
        if list != []:
            output = output + list[0]
    return output


with open('input.txt', 'r') as file:
    # read stacks
    stacks = Stacks()
    read_stacks(file, stacks)
    # read instructions
    instructions = read_ops(file)

    # apply changes
    for [amount, origin, target] in instructions:
        stacks.move_elements(int(amount), int(origin) - 1, int(target) - 1)

    # print the output the puzzle is asking for
    print(nice_output(stacks))
