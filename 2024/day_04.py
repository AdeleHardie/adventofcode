from utils import parse_input
import numpy as np


directions = [np.array([0, 1]), # right
              np.array([0, -1]), # left
              np.array([-1, 0]), # up
              np.array([1, 0]), # down
              np.array([-1, 1]), # up right
              np.array([-1, -1]), # up left
              np.array([1, 1]), # down right
              np.array([1, -1]) # down left
              ]

diagonals = np.array([[-1, -1], [-1, 1], [1, 1], [1, -1]])


def check_coord(coords, rows, cols):
    if coords[0] < 0 or coords[1] < 0:
        return False
    if coords[0] >= rows:
        return False
    if coords[1] >= cols:
        return False
    return True


def part_1(contents):
    rows = len(contents)
    cols = len(contents[0])
    xmas_count = 0

    for row in range(rows):
        for col in range(cols):
            # only keep going if value is X
            if contents[row][col] != 'X':
                continue
            for move in directions:
                coords = np.array([row, col])
                word = contents[coords[0]][coords[1]] # start building word
                for i in range(3):
                    coords += move
                    if not check_coord(coords, rows, cols):
                        continue
                    word += contents[coords[0]][coords[1]]
                if word == 'XMAS':
                    xmas_count += 1
                    
    return xmas_count


def part_2(contents):
    rows = len(contents)
    cols = len(contents[0])
    x_mas_count = 0

    for row in range(rows):
        for col in range(cols):
            # only keep going if value is A
            if contents[row][col] != 'A':
                continue
            letters = ''
            for d in diagonals:
                coords = np.array([row, col]) + d
                if not check_coord(coords, rows, cols):
                    continue
                letters += contents[coords[0]][coords[1]]
            if letters in ['MSSM', 'MMSS', 'SSMM', 'SMMS']:
                x_mas_count += 1

    return x_mas_count


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    #assert test_1_result=={}, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test)
    assert test_2_result==9, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()