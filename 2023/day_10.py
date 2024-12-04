from utils import parse_input
import numpy as np


coordinates = {'up': np.array([-1, 0]), 'down': np.array([1, 0]),'left': np.array([0, -1]), 'right': np.array([0, +1])}


def find_start(contents):
    for y in range(len(contents)):
            for x in range(len(contents[0])):
                if contents[y][x] == 'S':
                    return np.array([y, x])


def find_second(contents, start):
    connecting = {'up': ['|', '7', 'F'], 'down': ['|', 'L', 'J'], 'left': ['-', 'L', 'F'], 'right': ['-', 'J', '7']}   
    for direction in coordinates:
        next = start + coordinates[direction]
        try:
            pipe = contents[next[0]][next[1]]
            if pipe in connecting[direction] or pipe == 'S':
                return next, direction
        except:
            continue


def next_step(contents, start, direction):
    pipe_directions = {'|': {'up':'up', 'down': 'down'}, '-': {'left': 'left', 'right':'right'},
                       'L': {'down': 'right', 'left': 'up'}, 'J': {'right': 'up', 'down': 'left'},
                       '7': {'right': 'down', 'up': 'left'}, 'F': {'up': 'right', 'left': 'down'}}
    pipe = contents[start[0]][start[1]]
    new_direction = pipe_directions[pipe][direction]
    next = start + coordinates[new_direction]

    return next, new_direction


def part_1(contents):
    # find starting point
    start = find_start(contents)
    next, direction = find_second(contents, start)

    # walk the loop
    loop = [start, next]
    while contents[next[0]][next[1]] != 'S':
        next, direction = next_step(contents, next, direction)
        loop.append(next)

    return (len(loop)-1)//2
            

def part_2(contents, s):
    # find starting point
    start = find_start(contents)
    next, direction = find_second(contents, start)

    # generate new empty map
    new_map = [['.']*len(contents[0]) for i in range(len(contents))]
    new_map[next[0]][next[1]] = contents[next[0]][next[1]]

    # walk the loop
    # and add pipes to new map
    while contents[next[0]][next[1]] != 'S':
        next, direction = next_step(contents, next, direction)
        new_map[next[0]][next[1]] = contents[next[0]][next[1]]
    new_map[start[0]][start[1]] = s

    tiles_inside = 0
    for y in range(len(new_map)):
        inside = False # start every line outside
        for x in range(len(new_map[0])):
            tile = new_map[y][x]
            # if part of pipe loop
            # change inside/outside
            if tile in '|JL':
                if inside:
                    inside = False
                else:
                    inside = True
            # otherwise add to inside if currently inside
            elif tile == '.' and inside:
                tiles_inside += 1

    return tiles_inside


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    #assert test_1_result=={}, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test, 'F')
    assert test_2_result==1, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents, 'L'))

    #reddit()


if __name__ == '__main__':
    __main__()