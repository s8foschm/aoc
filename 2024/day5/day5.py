def parse_rules(rules_block):
    rules = []
    for line in rules_block:
        number1, number2 = int(line.split('|')[0]), int(line.split('|')[1])
        rules.append((number1, number2))
    return rules


def parse_updates(updates_block):
    updates = []
    for line in updates_block:
        numbers = [int(number) for number in line.split(',')]
        updates.append(numbers)
    return updates


def parse_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        rules, updates = [], []
        firstblock = True
        for line in lines:
            if line == "\n":
                firstblock = False
                continue
            if firstblock == True:
                rules.append(line.strip())
            else:
                updates.append(line.strip())
        return parse_rules(rules), parse_updates(updates)


def check_single_rule_respected(rule, updates):
    first_number, second_number = rule
    if first_number in updates and second_number in updates:
        return updates.index(first_number) < updates.index(second_number)
    else:
        # if both numbers are not in the update, the rule is immediately considered respected
        return True


rules, updates = parse_file('input.txt')
count = 0
all_respected_middle = []
for update in updates:
    all_respected = True
    for rule in rules:
        if not check_single_rule_respected(rule, update):
            all_respected = False
    if all_respected:
        count += 1
        mid_index = int((len(update) - 1) / 2)
        all_respected_middle.append(update[mid_index])
print('Part One: ', sum(all_respected_middle))


def swap_rule(rule, update):
    first_number, second_number = rule
    if check_single_rule_respected(rule, update):
        return update
    else:
        # swap two numbers if a rule is not respected
        a, b = update.index(first_number), update.index(second_number)
        update[a], update[b] = update[b], update[a]
        #print("swapped {} and {} because of rule {}", a, b, rule)
        return update

changed_updates = []
for update in updates:
    respected_rules = {rule: False for rule in rules}
    changed = False
    while False in respected_rules.values():
        for rule in rules:
            if not check_single_rule_respected(rule, update):
                swap_rule(rule, update)
                changed = True
            else:
                respected_rules.update({rule: True})
    if changed:
        changed_updates.append(update)

all_changed_middle = []
for update in changed_updates:
    mid_index = int((len(update) - 1) / 2)
    all_changed_middle.append(update[mid_index])
print("Part Two: ", sum(all_changed_middle))