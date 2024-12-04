from utils import parse_input


def move_beam(coords, direction):
    if direction == 'right':
        coords = (coords[0], coords[1]+1)
    elif direction == 'left':
        coords = (coords[0], coords[1]-1)
    elif direction == 'up':
        coords = (coords[0]-1, coords[1])
    else:
        coords = (coords[0]+1, coords[1])

    return coords


def get_direction(tile, direction):
    # if empty space
    # keep the same direction
    if tile == '.':
        return [direction]
    
    # if mirror
    mirror = {'/': {'right': 'up', 'left': 'down', 'up': 'right', 'down': 'left'},
              '\\': {'right': 'down', 'left': 'up', 'up': 'left', 'down': 'right'}}
    if tile in '\/':
        return [mirror[tile][direction]]
    
    # if splitter
    splitter = {'|': {'right': ['up', 'down'], 'left': ['up', 'down'], 'up': ['up'], 'down': ['down']},
                '-': {'right': ['right'], 'left': ['left'], 'up': ['left', 'right'], 'down': ['left', 'right']}}
    if tile in '|-':
        return splitter[tile][direction]
    

def validate_coords(coords, x, y):
    if coords[0] < 0 or coords[0] >= y:
        return False
    if coords[1] < 0 or coords[1] >= x:
        return False
    
    return True


def part_1(contents):
    energized_tiles = set([(0,0)])
    limx = len(contents[0])
    limy = len(contents)

    beams = [(0, 0, 'right')]

    for beam in beams:
        tile = contents[beam[0]][beam[1]]
        # get direction based on tile value
        directions = get_direction(tile, beam[2])
        # update position based on each direction
        for direction in directions:
            new_coords = move_beam((beam[0], beam[1]), direction)
            # validate coordinates
            valid = validate_coords(new_coords, limx, limy)
            if valid:
                energized_tiles.add(new_coords)
                beams.append((new_coords[0], new_coords[1], direction))

    return len(energized_tiles)


def part_2(contents):
    return None


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==46, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test)
    #assert test_2_result=={}, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()