from ast import literal_eval
from utils import parse_input


def comp_nums(x, y):
    if x > y:
        return False
    elif x < y:
        return True
    else:
        return None


def comp_lists(a, b):
    result = None
    for x, y in zip(a, b):
        if isinstance(x, int) and isinstance(y, int):
            result = comp_nums(x, y)
        elif isinstance(x, int):
            result = comp_lists([x], y)
        elif isinstance(y, int):
            result = comp_lists(x, [y])
        else:
            result = comp_lists(x, y)
        if result is not None:
            break
    if result is None:
        if len(a) < len(b):
            result = True
        elif len(b) < len(a):
            result = False
    return result


def comp_parsels(contents):
    idx_sum = 0
    results = []
    i = 0
    while i<len(contents)-1:
        p1 = literal_eval(contents[i])
        p2 = literal_eval(contents[i+1])
        result = comp_lists(p1, p2)
        results.append(result)
        if result:
            idx_sum += (i // 3)+1
        i += 3
    
    return idx_sum


def sort_parsels(contents):
    contents = [literal_eval(line) for line in contents if line != '']
    # add divider packets
    contents += [[[2]], [[6]]]

    for i in range(len(contents)):
        already_sorted = True
        for j in range(len(contents)-i-1):
            if not comp_lists(contents[j], contents[j+1]): # if not in order
                contents[j], contents[j+1] = contents[j+1], contents[j] # swap
                already_sorted = False
        if already_sorted:
            break

    p1 = 0
    p2 = 0
    for i, val in enumerate(contents):
        if val == [[2]]:
            p1 = i+1
        elif val == [[6]]:
            p2 = i+1

    return p1*p2


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    
    assert comp_parsels(test) == 13, 'failed part 1 test'
    print(f'Part 1: {comp_parsels(contents)}')

    assert sort_parsels(test) == 140, 'failed part 2 test'
    print(f'Part 2: {sort_parsels(contents)}')


if __name__ == '__main__':
    __main__()
