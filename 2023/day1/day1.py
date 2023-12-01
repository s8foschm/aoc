import collections
import ply.lex as lex
# PART ONE

def calculate_value(digits):
    if len(digits) == 1:
        value = digits[0] * 11
    else:
        last = digits[len(digits) - 1]
        value = digits[0] * 10 + last
    return value

with open("input.txt") as file:
    values = []
    for line in file:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(int(char))
        #print(digits)
        value = calculate_value(digits)
        #print(value)
        values.append(value)

#print("\n")
#print(values)
final_sum = sum(values)
print(final_sum)

# PART TWO
print("\n\n")

def check_number_in_text(text):
    found_numbers = []

    one_first_text_pos = text.find("one")
    one_last_text_pos = text.rfind("one")
    one_first_num_pos = text.find("1")
    one_last_num_pos = text.rfind("1")
    if one_first_text_pos != -1:
        found_numbers.append((1, one_first_text_pos))
    if one_last_text_pos != -1:
        found_numbers.append((1, one_last_text_pos))
    if one_first_num_pos != -1:
        found_numbers.append((1, one_first_num_pos))
    if one_last_num_pos != -1:
        found_numbers.append((1, one_last_num_pos))

    two_first_text_pos = text.find("two")
    two_last_text_pos = text.rfind("two")
    two_first_num_pos = text.find("2")
    two_last_num_pos = text.rfind("2")
    if two_first_text_pos != -1:
        found_numbers.append((2, two_first_text_pos))
    if two_last_text_pos != -1:
        found_numbers.append((2, two_last_text_pos))
    if two_first_num_pos != -1:
        found_numbers.append((2, two_first_num_pos))
    if two_last_num_pos != -1:
        found_numbers.append((2, two_last_num_pos))

    three_first_text_pos = text.find("three")
    three_last_text_pos = text.rfind("three")
    three_first_num_pos = text.find("3")
    three_last_num_pos = text.rfind("3")
    if three_first_text_pos != -1:
        found_numbers.append((3, three_first_text_pos))
    if three_last_text_pos != -1:
        found_numbers.append((3, three_last_text_pos))
    if three_first_num_pos != -1:
        found_numbers.append((3, three_first_num_pos))
    if three_last_num_pos != -1:
        found_numbers.append((3, three_last_num_pos))

    four_first_text_pos = text.find("four")
    four_last_text_pos = text.rfind("four")
    four_first_num_pos = text.find("4")
    four_last_num_pos = text.rfind("4")
    if four_first_text_pos != -1:
        found_numbers.append((4, four_first_text_pos))
    if four_last_text_pos != -1:
        found_numbers.append((4, four_last_text_pos))
    if four_first_num_pos != -1:
        found_numbers.append((4, four_first_num_pos))
    if four_last_num_pos != -1:
        found_numbers.append((4, four_last_num_pos))

    five_first_text_pos = text.find("five")
    five_last_text_pos = text.rfind("five")
    five_first_num_pos = text.find("5")
    five_last_num_pos = text.rfind("5")
    if five_first_text_pos != -1:
        found_numbers.append((5, five_first_text_pos))
    if five_last_text_pos != -1:
        found_numbers.append((5, five_last_text_pos))
    if five_first_num_pos != -1:
        found_numbers.append((5, five_first_num_pos))
    if five_last_num_pos != -1:
        found_numbers.append((5, five_last_num_pos))

    six_first_text_pos = text.find("six")
    six_last_text_pos = text.rfind("six")
    six_first_num_pos = text.find("6")
    six_last_num_pos = text.rfind("6")
    if six_first_text_pos != -1:
        found_numbers.append((6, six_first_text_pos))
    if six_last_text_pos != -1:
        found_numbers.append((6, six_last_text_pos))
    if six_first_num_pos != -1:
        found_numbers.append((6, six_first_num_pos))
    if six_last_num_pos != -1:
        found_numbers.append((6, six_last_num_pos))

    seven_first_text_pos = text.find("seven")
    seven_last_text_pos = text.rfind("seven")
    seven_first_num_pos = text.find("7")
    seven_last_num_pos = text.rfind("7")
    if seven_first_text_pos != -1:
        found_numbers.append((7, seven_first_text_pos))
    if seven_last_text_pos != -1:
        found_numbers.append((7, seven_last_text_pos))
    if seven_first_num_pos != -1:
        found_numbers.append((7, seven_first_num_pos))
    if seven_last_num_pos != -1:
        found_numbers.append((7, seven_last_num_pos))

    eight_first_text_pos = text.find("eight")
    eight_last_text_pos = text.rfind("eight")
    eight_first_num_pos = text.find("8")
    eight_last_num_pos = text.rfind("8")
    if eight_first_text_pos != -1:
        found_numbers.append((8, eight_first_text_pos))
    if eight_last_text_pos != -1:
        found_numbers.append((8, eight_last_text_pos))
    if eight_first_num_pos != -1:
        found_numbers.append((8, eight_first_num_pos))
    if eight_last_num_pos != -1:
        found_numbers.append((8, eight_last_num_pos))

    nine_first_text_pos = text.find("nine")
    nine_last_text_pos = text.rfind("nine")
    nine_first_num_pos = text.find("9")
    nine_last_num_pos = text.rfind("9")
    if nine_first_text_pos != -1:
        found_numbers.append((9, nine_first_text_pos))
    if nine_last_text_pos != -1:
        found_numbers.append((9, nine_last_text_pos))
    if nine_first_num_pos != -1:
        found_numbers.append((9, nine_first_num_pos))
    if nine_last_num_pos != -1:
        found_numbers.append((9, nine_last_num_pos))

    return found_numbers

def remove_duplicates(result):
    return list(set(result))

def find_and_combine_first_and_last_digit(digits):
    smallest_index = 100000
    largest_index = -1
    first = -1
    last = -1
    for element, index in digits:
        if index > largest_index:
            last, largest_index = element, index
        if index < smallest_index:
            first, smallest_index = element, index
    return first * 10 + last


with open("input.txt") as file:
    values = []
    for line in file:
        digits = remove_duplicates(check_number_in_text(line))
        values.append(find_and_combine_first_and_last_digit(digits))
    print(values)

final_sum = sum(values)
print(final_sum)