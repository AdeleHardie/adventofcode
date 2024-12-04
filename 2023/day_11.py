from utils import parse_input


def expand_space(map):
    map = [[val for val in line] for line in map]

    # expand columns
    empty_cols = []
    extended_map = [line.copy() for line in map]
    for col in range(len(map[0])):
        empty = all([line[col]=='.' for line in map])
        if empty:
            for line2 in extended_map:
                line2.insert(col+len(empty_cols), '.')
            empty_cols.append(col)
    # expand rows
    fully_extended_map = []
    for line in extended_map:
        empty = all([line[i]=='.' for i in range(len(line))])
        fully_extended_map.append(line)
        if empty:
            fully_extended_map.append(line)

    return fully_extended_map


def part_1(contents):
    # get the expanded map
    expanded = expand_space(contents)

    # get positions of galaxies
    galaxies = []
    for y in range(len(expanded)):
        for x in range(len(expanded[0])):
            if expanded[y][x] == '#':
                galaxies.append((y, x))

    # calculate distances
    distances = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            g1 = galaxies[i]
            g2 = galaxies[j]
            distance = abs(g2[0]-g1[0]) + abs(g2[1]-g1[1])
            distances.append(distance)

    return sum(distances)


def part_2(contents, expansion):
    expansion = expansion-1
    # instead of expanding the whole space, just modify galaxy coordinates

    # find all gaps
    empty_cols = []
    for col in range(len(contents[0])):
        if all([line[col]=='.' for line in contents]):
            empty_cols.append(col)
    empty_rows = []
    for row in range(len(contents)):
        if all([val=='.' for val in contents[row]]):
            empty_rows.append(row)

    # find galaxies
    # and change coordinates
    galaxies = []
    for y in range(len(contents)):
        for x in range(len(contents[0])):
            if contents[y][x] == '#':
                # find how many expansion gaps
                # before galaxy coordinates
                y_gaps = 0
                for gap_coord in empty_rows:
                    if gap_coord < y:
                        y_gaps += 1
                    else:
                        break
                x_gaps = 0
                for gap_coord in empty_cols:
                    if gap_coord < x:
                        x_gaps += 1
                    else:
                        break
                # modify coordinates by gaps x expansion
                galaxies.append((y+(y_gaps*expansion), x+(x_gaps*expansion)))

    # calculate distances
    distances = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            g1 = galaxies[i]
            g2 = galaxies[j]
            distance = abs(g2[0]-g1[0]) + abs(g2[1]-g1[1])
            distances.append(distance)

    return sum(distances)


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==374, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test, 100)
    assert test_2_result==8410, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents, 1000000))


if __name__ == '__main__':
    __main__()