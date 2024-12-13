from utils import parse_input


def evaluate_equation(eq):
    # parse equation input
    expected = int(eq.split(':')[0])
    numbers = [int(num) for num in eq.split(':')[1].split()]

    return expected, numbers


def operation(num1, remaining_nums, op, expected):
    if op == '+':
        result = num1 + remaining_nums[0]
    elif op == '*':
        result = num1 * remaining_nums[0]

    # if reached end of list
    if len(remaining_nums) == 1:
        if result == expected:
            return True
        else:
            return False
    # otherwise keep going
    else:
        possible_1 = operation(result, remaining_nums[1:], '+', expected)
        if possible_1:
            return True
        possible_2 = operation(result, remaining_nums[1:], '*', expected)
    
    return possible_2


def operation2(num1, remaining_nums, op, expected):
    if op == '+':
        result = num1 + remaining_nums[0]
    elif op == '*':
        result = num1 * remaining_nums[0]
    elif op == '||':
        result = int(str(num1) + str(remaining_nums[0]))

    # if reached end of list
    if len(remaining_nums) == 1:
        if result == expected:
            return True
        else:
            return False
    # otherwise keep going
    else:
        possible_1 = operation2(result, remaining_nums[1:], '+', expected)
        if possible_1:
            return True
        possible_2 = operation2(result, remaining_nums[1:], '*', expected)
        if possible_2:
            return True
        possible_3 = operation2(result, remaining_nums[1:], '||', expected)
    
    return possible_3
    

def part_1(contents):
    total = 0

    for line in contents:
        expected, numbers = evaluate_equation(line)
        possible_1 = operation(numbers[0], numbers[1:], '+', expected)
        if possible_1:
            total += expected
            continue
        possible_2 = operation(numbers[0], numbers[1:], '*', expected)
        if possible_2:
            total += expected

    return total


def part_2(contents):
    total = 0

    for line in contents:
        expected, numbers = evaluate_equation(line)
        possible_1 = operation2(numbers[0], numbers[1:], '+', expected)
        if possible_1:
            total += expected
            continue
        possible_2 = operation2(numbers[0], numbers[1:], '*', expected)
        if possible_2:
            total += expected
            continue
        possible_3 = operation2(numbers[0], numbers[1:], '||', expected)
        if possible_3:
            total += expected

    return total


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==3749, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test)
    assert test_2_result==11387, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()