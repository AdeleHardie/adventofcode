from utils import parse_input


def parse_races(contents, race_num):
    if race_num == 'multi':
        time = [int(val) for val in contents[0].split(':')[1].split()]
        distance = [int(val) for val in contents[1].split(':')[1].split()]
    elif race_num == 'single':
        time = [int(contents[0].split(':')[1].replace(' ', ''))]
        distance = [int(contents[1].split(':')[1].replace(' ', ''))]

    return time, distance


def part_1(contents, race_num):
    time, distance = parse_races(contents, race_num)

    combinations = []

    for t, d in zip(time, distance):
        d += 0.001 # add correction to win race
        sqrt = t**2 - (4*d)
        v1 = (-t + sqrt**0.5)/(-2)
        v2 = (-t - sqrt**0.5)/(-2)

        max_time = int(max(v1,v2))
        min_time = int(min(v1,v2))

        combinations.append(max_time-min_time)

    margin = 1
    for val in combinations:
        margin *= val

    return margin     


def part_2(contents):
    return None


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test, 'multi')
    assert test_1_result==288, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents, 'multi'))

    test_2_result = part_1(test, 'single')
    assert test_2_result==71503, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_1(contents, 'single'))


if __name__ == '__main__':
    __main__()