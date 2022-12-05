# ADVENT OF CODE 2022
# https://adventofcode.com/
# Day 1
# Francesco Georg Schmitt
# https://github.com/s8foschm/aoc2022


file = open('input.txt', 'r')

# remember individual elves in a list, write total calories for that elf into current position in the list
index = 0
elves = [0]

for line in file:
	if line=='\n':
		# go to the next elf
		index +=1
		elves.append(0)
	else:
		# add number to current elf
		line = line[:len(line)] # remove \n in the end of the line
		elves[index] += int(line)

file.close()

# ========== PART ONE ==========
# find index and amount of largest element in list
max = 0
ind = 0
for index, amount in enumerate(elves):
	if amount>max:
		max = amount
		ind = index

print ("index with highest calories: ", index, ", amount of calories: ", max)

# ========== PART TWO ==========
# find the top three elves, and add the number of calories they are carrying
sorted_elves = sorted(enumerate(elves), key=lambda x: x[1], reverse=True)

total_amount = sorted_elves[0][1]+sorted_elves[1][1]+sorted_elves[2][1]

print ("added amount of the highest three calories: ", total_amount)