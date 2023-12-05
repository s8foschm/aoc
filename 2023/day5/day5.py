class Mapping:
    def __init__(self, destination_start, source_start, length):
        self.destination_start = destination_start
        self.source_start = source_start
        self.length = length

    def __repr__(self):
        return "Individual Mapping of " + str(self.destination_start) + " " + str(self.source_start) + " " + str(
            self.length)

    def single_lookup(self, number):
        if self.source_start <= number < self.source_start + self.length:
            return self.destination_start + (number - self.source_start)
        else:
            return number


class Map:
    def __init__(self, name, mappings):
        self.name = name
        self.mappings = mappings

    def __repr__(self):
        return "Map " + self.name

    def lookup(self, number):
        for mapping in self.mappings:
            result = mapping.single_lookup(number)
            if result != number:  # assuming individual maps given do not overlap, but not checking
                # print("found and changed ", number, " to ", result)
                return result
        # print("did not change ", number)
        return number


def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()

    # parse input file
    seeds = [int(number) for number in lines[0].split(":")[1].strip().split()]
    maps = []
    buffer = []
    name = ""
    for line in lines[2:]:
        if line == "\n":
            mappings = [Mapping(int(dest), int(source), int(length)) for [dest, source, length] in buffer]
            maps.append(Map(name, mappings))
            buffer = []
            continue
        else:
            if " map:" in line:
                name = line[:-2]
            else:
                buffer.append(line.split())
    return seeds, maps


def find_locations(seeds, maps):
    locations = []
    for seed in seeds:
        value = seed
        for individual_map in maps:
            value = individual_map.lookup(value)
        locations.append(value)
    return locations


filename = "input.txt"
seeds, maps = parse_input(filename)

# find locations for seeds
# PART ONE
locations = find_locations(seeds, maps)
# print(locations)
print("Answer for part one is: ", min(locations))


# PART TWO
class Range:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def intersection(self, other):
        tmp = Range(max(self.lower, other.lower), min(self.upper, other.upper))
        return tmp if tmp.lower < tmp.upper else None

    def subtract(self, other):
        ins = self.intersection(other)
        if ins is None:
            return [Range(self.lower, self.upper)]
        elif (ins.lower, ins.upper) == (self.lower, self.upper):
            return []
        elif ins.lower == self.lower:
            return [Range(ins.upper, self.upper)]
        elif ins.upper == self.upper:
            return [Range(self.lower, ins.lower)]
        else:
            return [Range(self.lower, ins.lower), Range(ins.upper, self.upper)]

    def add(self, offset):
        return Range(self.lower + offset, self.upper + offset)


def calculate_seed_ranges(seeds):
    seed_ranges = []
    for beginning, length in zip(seeds[::2], seeds[1::2]):
        new_range = Range(beginning, length)
        seed_ranges.append(new_range)
    print(len(seed_ranges))
    return seed_ranges

class p2solver:
    def __init__(self, maps):
        self.maps = maps
        self.answer = float('inf')
    def propagate(self, r: Range, layer: int):
        if layer == len(self.maps):
            self.answer = min(self.answer, r.lower)
            return
        for dest, source, size in [(mapping.destination_start, mapping.source_start, mapping.length) for mapping in
                               self.maps[layer].mappings]:
            map_r = Range(source, source+size)
            ins = r.intersection(map_r)
            if ins is not None:
                self.propagate(ins.add(dest-source), layer+1)
                sub = r.subtract(map_r)
                if len(sub) == 0:
                    return
                r = sub[0]
                if len(sub) == 2:
                    self.propagate(sub[1], layer)
        self.propagate(r, layer+1)

filename = "input.txt"
seeds, maps = parse_input(filename)
locations = find_locations(seeds, maps)
p2 = p2solver(maps)

for i in range(0, len(seeds), 2):
    p2.propagate(Range(seeds[i], seeds[i]+seeds[i+1]), 0)

print("Answer for part two is: ", p2.answer)
