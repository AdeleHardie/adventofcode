import numpy as np
from utils import parse_input


def get_grid(contents):
    contents = [[tuple([int(i) for i in coords.split(',')]) for coords in line.split(' -> ')] for line in contents]

    max_x, max_y = 0, 0
    min_x = 1000
    for line in contents:
        for coords in line:
            if coords[0] > max_x:
                max_x = coords[0]
            if coords[1] > max_y:
                max_y = coords[1]
            if coords[0] < min_x:
                min_x = coords[0]
    grid = np.zeros((max_y+1, max_x+1), dtype=int)

    for line in contents:
        for i in range(len(line)-1):
            step, y1, y2 = 1, line[i][0], line[i+1][0]
            if y2 - y1 < 0:
                step = -1
            y2 += step
            for y in range(y1, y2, step):
                step, x1, x2 = 1, line[i][1], line[i+1][1]
                if x2 - x1 < 0:
                    step = -1
                x2 += step
                for x in range(x1, x2, step):
                    grid[x,y] = 1

    return grid[:,min_x:], (0, 500-min_x)


def check_outside(grid, pos):
    if any(pos<0) or pos[0] >= grid.shape[0] or pos[1] >= grid.shape[1]:
        return True
    else:
        return False


def add_floor(grid):
    floor = np.array([[0]*len(grid[0]),
                      [1]*len(grid[0])])

    grid = np.append(grid, floor, axis=0)

    return grid


def check_edge(grid, pos):
    if pos[1] == 0:
        return 0
    elif pos[1] == grid.shape[1]-1:
        return -1
    else:
        return 1


def add_edge(grid, idx):
    edge = np.zeros((len(grid)), int)
    edge[-1] = 1
    if idx == 0:
        grid = np.insert(grid, idx, edge, axis=1)
    else:
        grid = np.append(grid, edge.reshape(len(grid),1), axis=1)

    return grid


def falling_sand(contents, infinity=False):
    grid, sand = get_grid(contents)

    if infinity:
        grid = add_floor(grid)

    down, dleft, dright = np.array((1,0)), np.array((1,-1)), np.array((1,1))
    
    i = 0
    falling = True
    while falling and not i > 10000000:
        # initial position below source
        pos = np.array(sand)
        rested = False
        #print_grid(grid)
        while not rested:
            old_pos = pos.copy()
            for vec in [down, dleft, dright]:
                pos += vec
                # checks for grid changes
                if infinity:
                    idx = check_edge(grid, pos)
                    if idx < 1:
                        grid = add_edge(grid, idx)
                        old_pos += np.array((0, idx+1))
                        pos += np.array((0, idx+1))
                        sand = (sand[0], sand[1]+idx+1)
                else:
                    if check_outside(grid, pos):
                        falling = False
                        rested = True
                        break
                # if on grid and nothing in the way
                # adopt new position and stop checking
                if grid[tuple(pos)] == 0:
                    pos = pos
                    break
                else:
                    # move back
                    pos -= vec
            # can't move from origin
            if tuple(pos) == sand:
                i += 1
                rested = True
                falling = False
            # if no change in position then
            # no possible moves and stopped moving#
            elif tuple(old_pos) == tuple(pos) and falling:
                rested = True
                grid[tuple(pos)] = 2
                i += 1            
    
    return i
                


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))

    assert falling_sand(test) == 24, 'failed part 1 test'
    print(f'Part 1: {falling_sand(contents)}')

    assert falling_sand(test, True)== 93, 'failed part 2 test'
    print(f'Part 2: {falling_sand(contents, True)}')


if __name__ == '__main__':
    __main__()
