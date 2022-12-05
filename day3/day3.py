# ADVENT OF CODE 2022
# https://adventofcode.com/
# Day 3
# Francesco Georg Schmitt
# https://github.com/s8foschm/aoc2022


scores = {
	"a": 1,
	"b": 2,
	"c": 3,
	"d": 4,
	"e": 5,
	"f": 6,
	"g": 7,
	"h": 8,
	"i": 9,
	"j": 10,
	"k": 11,
	"l": 12,
	"m": 13,
	"n": 14,
	"o": 15,
	"p": 16,
	"q": 17,
	"r": 18,
	"s": 19,
	"t": 20,
	"u": 21,
	"v": 22,
	"w": 23,
	"x": 24,
	"y": 25,
	"z": 26,
	"A": 27,
	"B": 28,
	"C": 29,
	"D": 30,
	"E": 31,
	"F": 32,
	"G": 33,
	"H": 34,
	"I": 35,
	"J": 36,
	"K": 37,
	"L": 38,
	"M": 39,
	"N": 40,
	"O": 41,
	"P": 42,
	"Q": 43,
	"R": 44,
	"S": 45,
	"T": 46,
	"U": 47,
	"V": 48,
	"W": 49,
	"X": 50,
	"Y": 51,
	"Z": 52

}

def common(a, b, c = None):
	if (c == None):
		return [value for value in a if value in b]
	else:
		return [value for value in a if value in common(b, c)]

# ========== PART ONE ==========

score = 0

with open('input.txt', 'r') as file:
	for line in file:
		score += scores[common([*(line[slice(0, len(line)//2)])], [*(line[slice(len(line)//2, len(line))])])[0]]

print("Score part I: ", score)


# ========== PART TWO ==========

score = 0
with open('input.txt', 'r') as file:
	# always read 3 lines at once using a counter
	ct = 0
	curr_group = []
	total_groups = []
	for line in file:
		if ct < 3:
			curr_group.append(line[:-1])
			ct += 1
		else:
			total_groups.append(curr_group)
			ct = 0
			curr_group = []
			curr_group.append(line[:-1])
			ct += 1
	total_groups.append(curr_group)
	curr_group = []
	#print(total_groups)

	for group in total_groups:
		if len(group) == 3:
			[a,b,c] = group
		else:
			raise ValueError("groups need to be 3 elves")
		common_char = common(*[a], *[b], *[c])[0]
		score += scores[common_char]
		#print(common_char)
print("Score part II: ", score)