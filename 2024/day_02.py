from utils import parse_input


def check(levels):
    # check if decreasing
    diff = levels[1]-levels[0]
    if diff < 0:
        direction = -1
    else:
        direction = 1
    
    for i in range(len(levels)-1):
        diff = (levels[i+1]-levels[i])*direction # make positive if decreasing
        # check for magnitude
        if diff > 3 or diff == 0:
            return True
        # check for direction
        if diff < 0:
            return True
        
    return False


def part_1(contents, dampener):
    safe = 0

    for line in contents:
        # get all numbers
        levels = [int(val) for val in line.split()]
        failed = check(levels)
        
        if not failed:
            safe +=1
        elif dampener:
            for i in range(0, len(levels)):
                new_levels = levels[:i] + levels[i+1:]
                failed = check(new_levels)
                if not failed:
                    safe += 1
                    break

    return safe


def part_2(contents):
    return None


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test, 0)
    assert test_1_result==2, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents, 0))

    test_2_result = part_1(test, 1)
    assert test_2_result==4, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_1(contents, 1))


if __name__ == '__main__':
    __main__()