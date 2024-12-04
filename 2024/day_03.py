from utils import parse_input


def part_1(contents):
    mul = 0
    # split input
    contents = contents[0].split('mul(')

    for entry in contents:
        # remove second bracket
        if ')' not in entry:
            continue
        numbers = entry.split(')')[0]

        # split into numbers
        if ',' not in numbers:
            continue
        numbers = numbers.split(',')

        # check only 2 parts
        if len(numbers) != 2:
            continue
        # check both numbers
        if not (numbers[0].isnumeric() and numbers[1].isnumeric()):
            continue

        mul += int(numbers[0]) * int(numbers[1])

    return mul


def part_2(contents):
    mul = 0
    # split input
    contents = contents[0].split('mul(')

    enabled = True
    change = True
    for entry in contents:
        # apply previous change
        enabled = change
        # check if needs to get changed at the end
        if 'do()' in entry:
            change = True
        elif "don't()" in entry:
            change = False

        # if disabled, continue to the next
        if not enabled:
            continue
        # remove second bracket
        if ')' not in entry:
            continue
        numbers = entry.split(')')[0]

        # split into numbers
        if ',' not in numbers:
            continue
        numbers = numbers.split(',')

        # check only 2 parts
        if len(numbers) != 2:
            continue
        # check both numbers
        if not (numbers[0].isnumeric() and numbers[1].isnumeric()):
            continue

        mul += int(numbers[0]) * int(numbers[1])

    return mul


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==161, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test)
    assert test_2_result==48, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()