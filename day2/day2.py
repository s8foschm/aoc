# ========== PART ONE ==========

# base scores: rock - 1, paper - 2, scissors - 3
# result scores: loss - 0, draw - 3, win - 6

file = open('input.txt', 'r')
score = 0

for line in file:
	opp_play = line[0]
	own_play = line[2]

	if (opp_play == 'A'): # opponent plays rock
		if (own_play == 'X'): # player plays rock
			score += 4 # rock, draw
		elif (own_play == 'Y'): # player plays paper
			score += 8 # paper, win
		elif (own_play == 'Z'): # player plays scissors
			score += 3 # scissors, loss
		else:
			raise TypeError("Invalid Input")
	elif (opp_play == 'B'): # opponent plays paper
		if (own_play == 'X'): # player plays rock
			score += 1 # rock, loss
		elif (own_play == 'Y'): # player plays paper
			score += 5 # paper, draw
		elif (own_play == 'Z'): # player plays scissors
			score += 9 # scissors, win
		else:
			raise TypeError("Invalid Input")
	elif (opp_play == 'C'): # opponent plays scissors
		if (own_play == 'X'): # player plays rock
			score += 7 # rock, win
		elif (own_play == 'Y'): # player plays paper
			score += 2 # paper, loss
		elif (own_play == 'Z'): # player plays scissors
			score += 6 # scissors, draw
		else:
			raise TypeError("Invalid Input")
	else:
		raise TypeError("Invalid Input")

print("Score part I: ", score)

file.close()

# ========== PART TWO ==========

# X - lose, Y - draw, Z - win
# base scores: rock - 1, paper - 2, scissors - 3
# result scores: loss - 0, draw - 3, win - 6

file = open('input.txt', 'r')
score = 0

for line in file:
	opp_play = line[0]
	own_play = line[2]

	if (opp_play == 'A'): # opp rock
		if (own_play == 'X'): # lose -> scissors
			score += 3 # scissors, loss
		elif (own_play == 'Y'): # draw -> rock
			score += 4 # rock, draw
		elif (own_play == 'Z'): # win -> paper
			score += 8 # paper, win
		else:
			raise TypeError("Invalid Input")
	elif (opp_play == 'B'): # opp paper
		if (own_play == 'X'): # lose -> rock
			score += 1 # rock, loss
		elif (own_play == 'Y'): # draw -> paper
			score += 5 # paper, draw
		elif (own_play == 'Z'): # win -> scissors
			score += 9 # scissors, win
		else:
			raise TypeError("Invalid Input")
	elif (opp_play == 'C'): # opp scissors
		if (own_play == 'X'): # lose -> paper
			score += 2 # paper, loss
		elif (own_play == 'Y'): # draw -> scissors
			score += 6 # scissors, draw
		elif (own_play == 'Z'): # win -> rock
			score += 7 # rock, win
		else:
			raise TypeError("Invalid Input")
	else:
		raise TypeError("Invalid Input")

print("Score Part II: ", score)

file.close()