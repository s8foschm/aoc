input = "/home/francescos/aoc/2025/day1/input.txt"

moves =  []

with open(input) as file:
    for line in file:
        direction = line[0]
        number = int(line[1:])
        #print(direction, number)
        if direction == "R":
            moves.append(number)
        elif direction == "L":
            moves.append(-number)
        else:
            raise ValueError

# ========
# PART ONE
# ========

position = 50
zeroes = 0
for move in moves:
    # mod 100 gives potentially negative result. add another 100 and do mod 100 again gives the correct result.
    position = ((position + move) % 100 + 100) % 100
    if position == 0:
        zeroes += 1
print("Part One answer: ", zeroes)

# ========
# PART TWO
# ========

position = 50
zeroes = 0
for move in moves:
    print("next move: ", position, move)
    newposition = (position + move) % 100
    if move > 0:
        passes_during = move // 100 # passing a 0 during a move multiple times (move > 100)
        move = move % 100
    elif move < 0:
        passes_during = (- move) // 100 # move < -100
        move = (move % 100) - 100
    else:
        passes_during = 0
    print("passed 0 during move {} times".format(passes_during))
    zeroes += passes_during
    if (position + move > 100) or (position != 0 and position + move < 0): # passing a 0 during the move (move < 100)
        print("passed 0")
        zeroes += 1
    if newposition == 0: # ending on a 0 after a move
            print("stopped at 0")
            zeroes += 1
    oldposition = position
    position = newposition
    print("move: {}, from {} to {}".format(move, oldposition, position))
        
print("Part Two answer: ", zeroes)
