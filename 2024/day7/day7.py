operations = ["MUL", "ADD"]


def parse_file(filename):
    contents = {}
    with open(filename) as file:
        for line in file.readlines():
            score, numbers_str = int(line.split(":")[0].strip()), line.split(":")[1].strip()
            numbers = [int(num) for num in numbers_str.split()]
            contents[score] = numbers
    return contents

def calculate_possible_combinations(numbers):
    scores = [numbers[0]]
    for i in range(len(numbers)-1):
        curr_number = numbers[i]
        next_number = numbers[i+1]
        new_inter = []
        for inter in scores:
            new_inter.append(inter * next_number)
            new_inter.append(inter + next_number)
        scores = new_inter
    return scores


def check_number(score, numbers):
    options = calculate_possible_combinations(numbers)
    return score in options


file = parse_file("input.txt")
reached_goals = []
for goal, numbers in file.items():
    #print(goal, numbers)
    #print(check_number(goal, numbers))
    if check_number(goal, numbers):
        reached_goals.append(goal)
    #print("\n")
print("Part One: ", sum(reached_goals))