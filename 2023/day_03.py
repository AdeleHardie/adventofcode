from utils import parse_input


def part_1(contents):
    numbers = []
    lims = [len(contents[0]), len(contents)]
    for i, line in enumerate(contents):
        line += '.'
        number = []
        for j, char in enumerate(line):
            # assemble number
            if char.isnumeric():
                number.append(j)
            else:
                # if reached end of number
                # check if it is a part number
                if len(number) > 0:
                    part_number = False
                    for y in range(i-1, i+2):
                        for x in range(number[0]-1, number[-1]+2):
                            # check if coordinates on schematic
                            if 0<=x<lims[0] and 0<=y<lims[1]:
                                # check if a symbol
                                if contents[y][x] != '.' and not contents[y][x].isnumeric():
                                    part_number = True
                    if part_number:
                        numbers.append(int(line[number[0]:number[-1]+1]))
                    number = []

    return sum(numbers)


def part_2(contents):
    gears = {}
    lims = [len(contents[0]), len(contents)]
    for i, line in enumerate(contents):
        line += '.'
        number = []
        for j, char in enumerate(line):
            # assemble number
            if char.isnumeric():
                number.append(j)
            else:
                # if reached end of number
                # check if it is a part number
                if len(number) > 0:
                    part_number = False
                    for y in range(i-1, i+2):
                        for x in range(number[0]-1, number[-1]+2):
                            # check if coordinates on schematic
                            if 0<=x<lims[0] and 0<=y<lims[1]:
                                # check if a symbol
                                if contents[y][x] != '.' and not contents[y][x].isnumeric():
                                    part_number = True
                                    # check if that symbol is *
                                    if contents[y][x] == '*':
                                        if (x, y) not in gears:
                                            gears[(x, y)] = [int(line[number[0]:number[-1]+1])]
                                        else:
                                            gears[(x, y)].append(int(line[number[0]:number[-1]+1]))
                    number = []
    
    # check all gears
    ratios = []
    for gear, numbers in gears.items():
        if len(numbers) == 2:
            ratios.append(numbers[0]*numbers[1])
    
    return sum(ratios)


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==4361, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test)
    assert test_2_result==467835, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()