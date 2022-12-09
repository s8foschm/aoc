# ADVENT OF CODE 2022
# https://adventofcode.com/
# Day 9
# Francesco Georg Schmitt
# https://github.com/s8foschm/aoc2022

def read_file(file):
    instructions = []
    for line in file:
        [direction, amount] = line.split(' ')
        for i in range(0, int(amount)):
            instructions.append(direction)
    return instructions


def move_head(instruction, headPosition):
    x, y = headPosition
    if instruction == 'R':
        return x + 1, y
    elif instruction == 'L':
        return x - 1, y
    elif instruction == 'U':
        return x, y + 1
    elif instruction == 'D':
        return x, y - 1
    else:
        raise ValueError('Illegal instruction: ', instruction)


def move_tail(headPosition, tailPosition, tailVisited):
    # keeps the tail at its position or moves it in one direction
    headX, headY = headPosition
    tailX, tailY = tailPosition
    vis = tailVisited.copy()
    if touching(headPosition, tailPosition):
        vis.add(tailPosition)
        return tailPosition, vis
    elif headX == tailX:
        assert (abs(headY - tailY) <= 2), "tail was not moved correctly previously"
        if headY > tailY:
            newTailPos = tailX, tailY + 1
        else:
            newTailPos = tailX, tailY - 1
    elif headY == tailY:
        assert (abs(headX - tailX) <= 2), "tail was not moved correctly previously"
        if headX > tailX:
            newTailPos = tailX + 1, tailY
        else:
            newTailPos = tailX - 1, tailY
    else:
        newTailPos = move_tail_diag(headPosition, tailPosition)
    vis.add(newTailPos)
    return newTailPos, vis


def move_tail_diag(headPosition, tailPosition):
    # moves the tail if the head is off by 2 in a direction and 1 in another
    assert not (touching(headPosition, tailPosition)), 'Should not land in diagonally move method'
    headX, headY = headPosition
    tailX, tailY = tailPosition
    if headX == tailX + 1 and headY == tailY + 2:
        return tailX + 1, tailY + 1
    elif headX == tailX + 1 and headY == tailY - 2:
        return tailX + 1, tailY - 1
    elif headX == tailX + 2 and headY == tailY + 1:
        return tailX + 1, tailY + 1
    elif headX == tailX + 2 and headY == tailY - 1:
        return tailX + 1, tailY - 1
    elif headX == tailX - 1 and headY == tailY + 2:
        return tailX - 1, tailY + 1
    elif headX == tailX - 1 and headY == tailY - 2:
        return tailX - 1, tailY - 1
    elif headX == tailX - 2 and headY == tailY + 1:
        return tailX - 1, tailY + 1
    elif headX == tailX - 2 and headY == tailY - 1:
        return tailX - 1, tailY - 1
    else:
        return move_tail_diag_2(headPosition, tailPosition)


def move_tail_diag_2(headPosition, tailPosition):
    # moves the tail if the head is diagonally off by 2
    headX, headY = headPosition
    tailX, tailY = tailPosition
    if headX == tailX + 2 and headY == tailY + 2:
        return tailX + 1, tailY + 1
    elif headX == tailX + 2 and headY == tailY - 2:
        return tailX + 1, tailY - 1
    elif headX == tailX - 2 and headY == tailY + 2:
        return tailX - 1, tailY + 1
    elif headX == tailX - 2 and headY == tailY - 2:
        return tailX - 1, tailY - 1
    else:
        raise ValueError("Tail was moved incorrectly previously.", headPosition, tailPosition)


def touching(headPosition, tailPosition):
    headX, headY = headPosition
    tailX, tailY = tailPosition
    return (abs(headX - tailX) <= 1) and (abs(headY - tailY) <= 1)


def move_tails(headPosition, tails, visited):
    tai, vis = move_tail(headPosition, tails[0], visited[0])
    tails[0] = tai
    visited[0].update(vis)
    for (index, position) in enumerate(tails[1:]):
        tai1, vis1 = move_tail(tails[index], position, visited[index + 1])
        tails[index + 1] = tai1
        visited[index + 1].update(vis1)
    return tails, visited


with(open('input.txt', 'r')) as file:
    instructions = read_file(file)

    # PART ONE
    headPosition = 0, 0
    tailPosition = 0, 0

    tailVisited = set()

    for inst in instructions:
        headPosition = move_head(inst, headPosition)
        tailPosition, tailVisited = move_tail(headPosition, tailPosition, tailVisited)
    print("Amount of locations visited by the tail: ", len(tailVisited))

    # PART TWO
    headPosition = 0, 0
    tails = [(0, 0)] * 9

    # apparently using [set()] * 9 links the sets so that they cannot have different values
    visited = [set(), set(), set(), set(), set(), set(), set(), set(), set()]

    for inst in instructions:
        headPosition = move_head(inst, headPosition)
        tails, visited = move_tails(headPosition, tails, visited)

    print("Amount of locations visited by the last member of the 9 long tail: ", len(visited[8]))
