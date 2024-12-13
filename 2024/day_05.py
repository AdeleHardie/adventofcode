from utils import parse_input


def parse_rules(rule_input):
    rules = []
    updates = []

    for line in rule_input:
        if '|' in line:
            rules.append(line.split('|'))
        elif ',' in line:
            updates.append(line.split(','))

    return rules, updates


def find_rules(rules, update):
    relevant_rules = {}

    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if rule[0] not in relevant_rules:
                relevant_rules[rule[0]] = [rule[1]]
            else:
                relevant_rules[rule[0]].append(rule[1])

    return relevant_rules


def check_pages(update, relevant_rules):
    for i in range(len(update)):
        page = update[i]
        after = update[i+1:]
        # continue if page doesn't have rules
        if page not in relevant_rules:
            continue
        # check that all pages that need to be after this one
        # are in the after list
        if not all([idx in after for idx in relevant_rules[page]]):
            return False
    
    return True


def find_correct_middle(update, relevant_rules):
    num_pages = len(update)
    middle_point = num_pages//2

    for page, afters in relevant_rules.items():
        if len(afters) == middle_point:
            return int(page)


def part_1(contents):
    rules, updates = parse_rules(contents)

    middle_sum = 0

    for update in updates:
        relevant_rules = find_rules(rules, update)
        if check_pages(update, relevant_rules):
            middle_sum += int(update[len(update)//2])

    return middle_sum


def part_2(contents):
    rules, updates = parse_rules(contents)

    middle_sum = 0

    for update in updates:
        relevant_rules = find_rules(rules, update)
        if not check_pages(update, relevant_rules):
            middle_sum += find_correct_middle(update, relevant_rules)

    return middle_sum


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    #assert test_1_result=={}, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test)
    assert test_2_result==123, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()