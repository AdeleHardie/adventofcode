from utils import parse_input
from itertools import combinations
import timeit


def generate_combinations(springs, conditions, cache={}):
    # if reach no more springs and no more conditions, return 1
    if len(springs) == 0 and len(conditions) == 0:
        return 1
    
    # if no more springs but conditions unsatisfied, return 0
    if len(springs) == 0 and len(conditions) > 0:
        return 0
    
    # if all conditions satisied, but broken springs leftover
    # also return 0
    if len(conditions) == 0:
        if '#' in springs:
            return 0
        else:
            return 1
        
    if (springs, conditions) in cache:
        return cache[(springs, conditions)]

    totals = 0

    # if the spring is . or unknown, treat as . and continue
    if springs[0] == '.' or springs[0] == '?':
        totals += generate_combinations(springs[1:], conditions, cache)
    
    # also
    # if spring is # or unknown, treat as #
    # and check if a valid path to continue
    if springs[0] == '#' or springs[0] == '?':
        # make sure there are no gaps (.) in the stretch the length of conditions
        # and the one after is a gap or ? to end the continuous line of #
        # and that the required length fits
        if len(springs) >= conditions[0] and '.' not in springs[:conditions[0]]:
            if conditions[0] == len(springs):
                # can validly continue after skipping this section of broken springs
                # plus the gap
                totals += generate_combinations(springs[conditions[0]+1:], conditions[1:], cache)
            elif springs[conditions[0]] in '.?':
                totals += generate_combinations(springs[conditions[0]+1:], conditions[1:], cache)

    cache[(springs, conditions)] = totals
    return totals


def part_1(contents):
    valid_combinations = 0
    for line in contents:
        springs, conditions = line.split()
        conditions = tuple([int(val) for val in conditions.split(',')])
        valid_combinations += generate_combinations(springs, conditions)
        
    return valid_combinations


def part_2(contents):
    valid_combinations = 0

    for line in contents:
        springs, conditions = line.split()
        springs = '?'.join([springs]*5) # expand the springs
        conditions = tuple([int(val) for val in conditions.split(',')*5]) # expand and convert the conditions
        valid_combinations += generate_combinations(springs, conditions)

    return valid_combinations


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==21, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test)
    assert test_2_result==525152, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()