from utils import parse_input


def scan(contents, l):
    l = l - 1
    for i in range(len(contents[0])):
        if i < l:
            continue
        packet = contents[0][i-l:i+1]
        if len(packet) == len(set(packet)):
            return i+1


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))

    assert scan(test, 4) == 7, 'failed part 1 test'
    print(f'Part 1: {scan(contents, 4)}')

    assert scan(test, 14) == 19, 'failed part 2 test'
    print(f'Part 2: {scan(contents, 14)}')


if __name__ == '__main__':
    __main__()
