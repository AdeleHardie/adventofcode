from numpy import array as np_array
from utils import parse_input


vectors = {'U': np_array((1,0)), 'D': np_array((-1,0)), 'L': np_array((0,-1)), 'R': np_array((0,1))}


def check_tail(head, tail):
    dist = head-tail
    if all(abs(dist)>0) and any(abs(dist)>1):
        move = np_array([i//abs(i) for i in dist])
    elif any(abs(dist)>1):
        move = []
        for i in dist:
            if abs(i) > 1:
                i = i//abs(i)
            move.append(i)
        move = np_array(move)
    else:
        move = np_array((0,0))
    return move


def go(moves, rope_len):
    rope = [np_array((0,0)) for _ in range(rope_len)]
    tail_positions = set()

    for move in moves:
        direction = move.split()[0]
        steps = int(move.split()[1])
        for _ in range(steps):
            rope[0] += vectors[direction]
            for i in range(1, rope_len):
                rope[i] += check_tail(rope[i-1], rope[i])
            tail_positions.add(str(rope[-1]))

    return len(tail_positions)


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    assert go(test, 2) == 13, 'failed part 1 test'
    print(f'Part 1: {go(contents, 2)}')
    assert go(test, 10) == 1, 'failed part 2 test'
    print(f'Part 2: {go(contents, 10)}')


if __name__ == '__main__':
    __main__()
