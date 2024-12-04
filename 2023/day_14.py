from utils import parse_input


def tilt_vertically(rocks, direction):
    if direction == 'north':
        rows = [i for i in range(len(rocks))]
        modifier = 1
    else:
        rows = [i for i in range(len(rocks)-1, -1, -1)]
        modifier = -1
    cols = len(rocks[0])

    for i in range(cols):
        # keep track of last rock
        last = rows[0] - modifier
        # go over rocks
        for j in rows:
            if rocks[j][i] == 'O':
                # move the rock next to last rock
                last += modifier
                rocks[last][i] = 'O'
                # update current spot to empty
                # if different from new rock spot
                if j != last:
                    rocks[j][i] = '.'
            # treat square rocks as obstacles
            elif rocks[j][i] == '#':
                last = j

    return rocks


def tilt_horizontally(rocks, direction):
    if direction == 'west':
        cols = [i for i in range(len(rocks[0]))]
        modifier = 1
    else:
        cols = [i for i in range(len(rocks[0])-1, -1, -1)]
        modifier = -1
    rows = len(rocks)

    for i in range(rows):
        last = cols[0] - modifier
        for j in cols:
            if rocks[i][j] == 'O':
                last += modifier
                rocks[i][last] = 'O'
                if j != last:
                    rocks [i][j] = '.'
            elif rocks[i][j] == '#':
                last = j
    
    return rocks


def calc_load(rocks):
    rows = len(rocks)
    cols = len(rocks[0])

    total_load = 0

    for row in range(rows):
        for col in range(cols):
            if rocks[row][col] == 'O':
                total_load += rows-row

    return total_load


def find_pattern(values):
    discards = [i for i in range(1000)]
    lengths = [i for i in range(5, 1000)]
    min_repeats = 50
    
    for discard in discards:
        for length in lengths:
            new_values = values[discard:]
            pattern = new_values[:length]
            found = 0
            for i in range(0, len(new_values), length):
                to_check = new_values[i:i+length]
                if to_check == pattern:
                    found += 1
                else:
                    break
            if found >= min_repeats:
                return discard, pattern

    return None


def part_1(contents):
    contents = [[rock for rock in line] for line in contents]
    updated_rocks = tilt_vertically(contents, 'north')
    load = calc_load(updated_rocks)

    return load


def part_2(contents, ncycles):
    contents = [[rock for rock in line] for line in contents]
    last_rocks = contents
    loads = []

    for i in range(min(ncycles, 51000)):
        updated_rocks = tilt_vertically(last_rocks, 'north')
        updated_rocks = tilt_horizontally(updated_rocks, 'west')
        updated_rocks = tilt_vertically(updated_rocks, 'south')
        updated_rocks = tilt_horizontally(updated_rocks, 'east')
        last_rocks = updated_rocks
        loads.append(calc_load(updated_rocks))

    if ncycles < 51000:
        return loads[-1]

    # check for pattern after 51000 cycles
    discard, pattern = find_pattern(loads)
    last_cycle = (ncycles-discard)%len(pattern)
        
    return pattern[last_cycle-1]


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==136, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test, 1000000000)
    assert test_2_result==64, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents, 1000000000))


if __name__ == '__main__':
    __main__()