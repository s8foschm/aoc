import sys
sys.setrecursionlimit(100000) # :)

with open('input.txt') as file:
    lines = file.readlines()
    text = ''.join(lines)
#print(text)

# PART ONE
def parse(string):
    numbers = parse_accu(string, [])
    result = 0
    for (a,b) in numbers:
        result += int(a)*int(b)
    return result

def parse_accu(string, previous):
    if string == '':
        return previous
    elif string.startswith('mul'):
        return parse_mul(string[3:], previous)
    else:
        return parse_accu(string[1:], previous)

def parse_mul(string, previous):
    if string.startswith('(') and string.find(',') != -1 and string.find(')') != -1:
        numbers = string[1:].split(')')[0].split(',')
        if not all(number.isnumeric() for number in numbers):
            return parse_accu(string[1:], previous)
        else:
            #print('Mul', numbers)
            rest = ''.join(string.split(')',1 )[1:])
            previous.append((numbers[0], numbers[1]))
            return parse_accu(rest, previous)
    else:
        return parse_accu(string[1:], previous)

print("Part One: ", parse(text))

# PART TWO
def parse_new(string):
    numbers = parse_accu_new(string, [], True)
    result = 0
    for (a,b) in numbers:
        result += int(a)*int(b)
    return result

def parse_accu_new(string, previous, active):
    if string == '':
        return previous
    elif string.startswith('do()'):
        return parse_accu_new(string[4:], previous, True)
    elif string.startswith('don\'t()'):
        return parse_accu_new(string[7:], previous, False)
    elif string.startswith('mul'):
        return parse_mul_new(string[3:], previous, active)
    else:
        return parse_accu_new(string[1:], previous, active)

def parse_mul_new(string, previous, active):
    if string.startswith('(') and string.find(',') != -1 and string.find(')') != -1:
        numbers = string[1:].split(')')[0].split(',')
        if not all(number.isnumeric() for number in numbers):
            return parse_accu_new(string[1:], previous, active)
        else:
            #print('Mul', numbers, active)
            rest = ''.join(string.split(')', 1)[1:])
            if active:
                previous.append((numbers[0], numbers[1]))
            return parse_accu_new(rest, previous, active)
    else:
        return parse_accu_new(string[1:], previous, active)

print("Part Two: ", parse_new(text))