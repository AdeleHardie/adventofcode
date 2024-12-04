from utils import parse_input


def part_1(contents):
    list1 = [int(line.split()[0]) for line in contents]
    list2 = [int(line.split()[1]) for line in contents]

    list1.sort()
    list2.sort()

    distances = 0

    for i, j in zip(list1, list2):
        distances += abs(i-j)

    return distances


def part_2(contents):
    similarity = 0

    cache = {}

    list1 = [int(line.split()[0]) for line in contents]
    list2 = [int(line.split()[1]) for line in contents]

    for i in list1:
        if i not in cache:
            in_list2 = 0
            for j in list2:
                if j == i:
                    in_list2 += 1
            cache[i] = i * in_list2
        similarity += cache[i]

    return similarity


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==11, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test)
    assert test_2_result==31, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()