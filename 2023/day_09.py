from utils import parse_input


def next_in_sequence(numbers):
    # find all the differences
    differences = []
    for i in range(len(numbers)-1):
        differences.append(numbers[i+1]-numbers[i])
    
    # check if all 0
    if not all([val==0 for val in differences]):
        differences = next_in_sequence(differences)
    numbers.append(differences[-1]+numbers[-1])
    return numbers


def previous_in_sequence(numbers):
    # find all the differences
    differences = []
    for i in range(len(numbers)-1):
        differences.append(numbers[i+1]-numbers[i])
    
    # check if all 0
    if not all([val==0 for val in differences]):
        differences = previous_in_sequence(differences)
    numbers.insert(0, numbers[0]-differences[0])
    return numbers


def part_1(contents):
    values = []
    for line in contents:
        numbers = [int(val) for val in line.split()]
        next_value = next_in_sequence(numbers)[-1]
        values.append(next_value)

    return sum(values)


def part_2(contents):
    values = []
    for line in contents:
        numbers = [int(val) for val in line.split()]
        previous_value = previous_in_sequence(numbers)[0]
        values.append(previous_value)

    return sum(values)


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==114, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test)
    assert test_2_result==2, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()