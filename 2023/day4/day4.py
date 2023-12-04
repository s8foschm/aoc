filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()


def get_numbers_from_line(line):
    numbers = line.split(":")[1].strip().split("|")
    winning_numbers = [int(number) for number in numbers[0].strip().split()]
    found_numbers = [int(number) for number in numbers[1].strip().split()]
    return winning_numbers, found_numbers


# PART ONE
def calculate_score(winning_numbers, found_numbers):
    score = 0
    for number in found_numbers:
        if number in winning_numbers:
            if score == 0:
                score = 1
            else:
                score = 2 * score
    return score


scores = []

for line in lines:
    winning_numbers, found_numbers = get_numbers_from_line(line)
    score = calculate_score(winning_numbers, found_numbers)
    scores.append(score)

# print(scores)
print("Answer for Part One is: ", sum(scores))


# PART TWO
def count_winning_numbers(winning_numbers, found_numbers):
    count = 0
    for number in found_numbers:
        if number in winning_numbers:
            count += 1
    return count


matching_numbers_counts = []
for line in lines:
    winning_numbers, found_numbers = get_numbers_from_line(line)
    matching_numbers_counts.append(count_winning_numbers(winning_numbers, found_numbers))


card_amounts = [1 for i in range(len(matching_numbers_counts))]
for index in range(len(card_amounts)):
    number = card_amounts[index]
    match = matching_numbers_counts[index]
    for i in range(1, match + 1):
        for j in range(1, number + 1):
            if index + i < len(card_amounts):
                card_amounts[index + i] += 1

print("Answer for Part Two is: ", sum(card_amounts))