def parse_file(filename):
    with open(filename) as file:
        lines = file.readlines()
    games = []
    for line in lines:
        game = []
        contents = line.split(":")[1].strip(" ").strip("\n").split(";")
        for draw in contents:
            curr_draw = {}
            elements = draw.split(",")
            for element in elements:
                element_stripped_sep = element.strip().split(" ")
                amount = int(element_stripped_sep[0])
                color = element_stripped_sep[1]
                curr_draw.update({color: amount})
            game.append(curr_draw)
        games.append(game)
    return games

def find_maximums(game):
    red_max, green_max, blue_max = 0, 0, 0
    for draw in game:
        if "red" in draw:
            red = draw["red"]
            if red > red_max:
                red_max = red
        if "green" in draw:
            green = draw["green"]
            if green > green_max:
                green_max = green
        if "blue" in draw:
            blue = draw["blue"]
            if blue > blue_max:
                blue_max = blue
    return red_max, green_max, blue_max

file = "input.txt"
red_max_allowed = 12
green_max_allowed = 13
blue_max_allowed = 14

our_games = parse_file(file)
found_maximums = []
for game in our_games:
    maximums = find_maximums(game)
    found_maximums.append(maximums)

# PART ONE
valid_indices = []
invalid_indices = []
for index, (red_max, green_max, blue_max) in enumerate(found_maximums):
    if red_max > red_max_allowed or green_max > green_max_allowed or blue_max > blue_max_allowed:
        invalid_indices.append(index+1)
    else:
        valid_indices.append(index+1)

print(sum(valid_indices))

# PART TWO
# found_maximums from before basically already solves most of this exercise

powers = [red * green * blue for red, green, blue in found_maximums]
print(sum(powers))
