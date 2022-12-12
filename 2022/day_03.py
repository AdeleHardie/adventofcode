from utils import parse_input


def item_value(item):
    if ord(item) > 90:
        return ord(item) - 96
    else:
        return ord(item) - 38


def priority_1(contents):
    total_priority = 0
    for line in contents:
        num_items = len(line) // 2
        for value in line[:num_items]:
            if value in line[num_items:]:
                total_priority += item_value(value)
                break

    return total_priority


def priority_2(contents):
    total_priority = 0
    
    i = 0
    for line in contents[::3]:
        for value in line:
            if value in contents[i+1] and value in contents[i+2]:
                total_priority += item_value(value)
                break
        i += 3

    return total_priority


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    assert priority_1(test) == 157, 'failed part 1 test'
    print(f'Part 1: {priority_1(contents)}')
    assert priority_2(test) == 70, 'failed part 2 test'
    print(f'Part 1: {priority_2(contents)}')


if __name__ == '__main__':
    __main__()