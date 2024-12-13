from utils import parse_input


def find_guard(contents):
    for i in range(len(contents)):
        for j in range(len(contents[0])):
            if contents[i][j] == '^':
                return (i, j)
            

def position_valid(position, rows, cols):
    if position[0] < 0 or position[1] < 0:
        return False
    if position[0] >= rows or position[1] >= cols:
        return False
    return True


def part_1(contents):
    rows = len(contents)
    cols = len(contents[0])
    # find starting position
    position = find_guard(contents)
    # set up directions
    # rotating by 90 degrees
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    d_idx = 0

    # walk the map
    visited = set()
    while True:
        visited.add(position)
        d = directions[d_idx]
        # find possible new position
        new_position = (position[0]+d[0], position[1]+d[1])
        # if encounter obstacle
        # only update direction
        if not position_valid(new_position, rows, cols):
            break
        if contents[new_position[0]][new_position[1]] == '#':
            d_idx = (d_idx+1)%4
        # otherwise update position
        else:
            position = new_position

    return visited

def update_map(map, coords):
    new_map = [line for line in map]
    new_map[coords[0]] = new_map[coords[0]][:coords[1]] + '#' + new_map[coords[0]][coords[1]+1:]
    return new_map


def part_2(contents, visited, cutoff):
    rows = len(contents)
    cols = len(contents[0])
    # find starting position
    position = find_guard(contents)
    visited.remove(position) # cannot place obstruction where guard starts?
    # set up directions
    # rotating by 90 degrees
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    d_idx = 0

    obstructions = 0

    # only worth checking obstructions
    # in path
    for coords in visited:
        # ignore existing obstructions
        if contents[coords[0]][coords[1]] == '#':
            continue
        # reset for a new walk
        i = 0
        d_idx = 0
        position = find_guard(contents)
        # place potential obstruction
        new_map = update_map(contents, coords)
        # try and walk the new map
        while i < cutoff:
            d = directions[d_idx]
            # find possible new position
            new_position = (position[0]+d[0], position[1]+d[1])
            # if encounter obstacle
            # only update direction
            if not position_valid(new_position, rows, cols):
                break
            if new_map[new_position[0]][new_position[1]] == '#':
                d_idx = (d_idx+1)%4
            # otherwise update position
            else:
                position = new_position
            i += 1
        # if cutoff number of moves was reached, assume that guard was stuck
        if i == cutoff:
            obstructions += 1


    return obstructions


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert len(test_1_result)==41, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    part_1_result = part_1(contents)
    print(len(part_1_result))

    test_2_result = part_2(test, test_1_result, 1000)
    assert test_2_result==6, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents, part_1_result, 10000))


if __name__ == '__main__':
    __main__()