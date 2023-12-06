import numpy as np

file = "input.txt"

with open(file) as file:
    lines = file.readlines()
times, distances = list(map(int, lines[0].split()[1:])), list(map(int, lines[1].split()[1:]))

races = []

# PART ONE
for time, distance in zip(times, distances):
    race_options_total = []
    for time_held in range(time+1):
        speed = time_held
        time_traveled = time - time_held
        distance_traveled = speed * time_traveled
        race_options_total.append((time_held, distance_traveled))
    races.append(race_options_total)

#print(races)

possibilities = []
options = []
for index, race in enumerate(races):
    possibilities_individual = 0
    for (time, distance) in race:
        record = distances[index]
        if distance > record:
            possibilities_individual += 1
            options.append((time, distance))
    possibilities.append(possibilities_individual)
#print(possibilities)
print("Answer for Part One is: ",np.prod(possibilities))

# PART TWO
time, record = int(''.join(lines[0].split()[1:])), int(''.join(lines[1].split()[1:]))
#print(time, record)

race_options_total = []
for time_held in range(time+1):
    speed = time_held
    time_traveled = time - time_held
    distance_traveled = speed * time_traveled
    race_options_total.append((time_held, distance_traveled))
print(len(race_options_total), " options calculated")
#print(race_options_total)

possibilities = []
options = []
possibilities_individual = 0
for time, distance in race_options_total:
    if distance > record:
        possibilities_individual += 1
        options.append((time, distance))
#print(possibilities)
print("Answer for Part Two is: ", possibilities_individual)