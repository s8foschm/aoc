# ADVENT OF CODE 2022
# https://adventofcode.com/
# Day 11
# Francesco Georg Schmitt
# https://github.com/s8foschm/aoc2022
import time
import threading
import numpy as np


class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.activity = 0

    def __repr__(self):
        return 'Monkey ' + str(self.operation) + ' ' + str(self.test)

    def start_thread(self, monkeys, factor):
        t = threading.Thread(target=self.take_round(monkeys, factor))
        t.start()
        return t

    def take_round(self, monkeys, management_factor, modulo):
        items = self.items
        throwing_list = []
        for (index, item) in enumerate(self.items):
            new_items = self.items
            # print("Monkey inspects item: ", items[index])
            # monkey picks up the item, modulo keeps the number manageable
            items[index] = self.operation.execute(item) % modulo
            self.activity = self.activity + 1
            # print("Worry level increased: ", items[index])
            items[index] = items[index] // management_factor  # monkey doesn't drop the item
            # print("Worry level decreased: ", items[index])
            target = self.test.execute(items[index])
            # print("Item ", index, " of value ", items[index], " to be thrown to ", target)
            throwing_list.append((index, target))
        # must iterate over the list from back to front otherwise indexes get messed up
        for (index, target) in throwing_list[::-1]:
            # print("Item " , index, " of value ", items[index], " is thrown to ", target)
            self.throw(index, self.items, target, monkeys)

    def throw(self, index, itemlist, aim, monkeys):
        monkeys[aim].catch(itemlist.pop(index))

    def catch(self, value):
        self.items.append(value)


class Operation:
    def __init__(self, operation, amount):
        self.operation = operation
        self.amount = amount

    def __repr__(self):
        return 'Op' + self.operation + str(self.amount)

    def execute(self, value):
        # print(self)
        if self.operation == "*":
            if self.amount == "old":
                return value * value
            else:
                self.amount = int(self.amount)  # throws an AssertionError if the input file is invalid
                return value * self.amount
        elif self.operation == "+":
            self.amount = int(self.amount)  # throws an AssertionError if the input file is invalid
            return value + self.amount
        else:
            raise ValueError("Invalid Operation")


class Test:
    def __init__(self, condition, true_consequence, false_consequence):
        self.condition = condition  # int
        self.true_consequence = true_consequence  # int
        self.false_consequence = false_consequence  # int

    def __repr__(self):
        return "Test: " + str(self.condition) + " " + str(self.true_consequence) + " " + str(self.false_consequence)

    def execute(self, value):
        if self.check_condition(value):
            return self.true_consequence
        else:
            return self.false_consequence

    def check_condition(self, value):
        return value % self.condition == 0


def read_file(file):
    lines = file.readlines()

    monkeys_input = [lines[x:x + 7] for x in range(0, len(lines), 7)]
    monkeys = []
    for monkey in monkeys_input:
        starting_items_str = monkey[1][18:-1]
        starting_items = list(map(int, starting_items_str.split(", ")))
        operation_str = monkey[2][19:-1]
        operation_list = operation_str.split(" ")[1:]
        operation = Operation(operation_list[0], operation_list[1])
        test_str = monkey[3][21:-1]
        true_str = monkey[4][29:-1]
        false_str = monkey[5][30:-1]
        test = Test(int(test_str), int(true_str), int(false_str))
        monkeys.append(Monkey(starting_items, operation, test))
    assert (len(monkeys) == len(monkeys_input))
    return monkeys


# PART ONE
with(open('input.txt', 'r')) as file:
    monkeys = read_file(file)

st = time.time()
common_modulo = np.lcm.reduce([monkey.test.condition for monkey in monkeys])
for i in range(20):
    # print("Round ", i + 1)
    for (index, monkey) in enumerate(monkeys):
    #    print("Monkey ", index)
         monkey.take_round(monkeys, 3, common_modulo)
    # for (index, monkey) in enumerate(monkeys):
    #     print("Monkey ", index, " activity: ", monkey.activity)
    #     print("Monkey ", index, " items: ", monkey.items)
    # print("\n")

activities = [monkey.activity for monkey in monkeys]
activities.sort()
print(activities)
res = activities[-1] * activities[-2]
print("Level of Monkey Business: ", res)
duration = time.time() - st
print("Execution time: ", duration)

# PART TWO
with(open('input.txt', 'r')) as file:
    monkeys = read_file(file)
st = time.time()
common_modulo = np.lcm.reduce([monkey.test.condition for monkey in monkeys])
for i in range(10000):
    #print("Round ", i + 1)
    for monkey in monkeys:
        monkey.take_round(monkeys, 1, common_modulo)
activities = [monkey.activity for monkey in monkeys]
print(activities)
activities.sort()
res = activities[-1] * activities[-2]
print("Level of Monkey Business: ", res)
duration = time.time() - st
print("Execution time: ", duration)

# TESTING
# with(open('test_input.txt', 'r')) as file:
#     monkeys = read_file(file)
# st = time.time()
# common_modulo = np.lcm.reduce([monkey.test.condition for monkey in monkeys])
