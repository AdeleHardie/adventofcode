from utils import parse_input


def reflections(pattern):
    columns = len(pattern[0])
    rows = len(pattern)
    # vertical reflection
    # check left to right
    for i in range(columns-1):
        idx1 = i
        idx2 = i+1
        col1 = [pattern[row][idx1] for row in range(rows)]
        col2 = [pattern[row][idx2] for row in range(rows)]
        # if columns are equal
        # keep expanding
        if col1 == col2:
            while col1 == col2 and idx1 >= 0 and idx2 < columns:
                idx1 -= 1
                idx2 += 1
                try:
                    col1 = [pattern[row][idx1] for row in range(rows)]
                    col2 = [pattern[row][idx2] for row in range(rows)]
                except:
                    break
            # check that reached the end of pattern on at least one edge
            if idx1 == -1 or idx2 == columns:
                return i+1, 'vertical', i

    # horizontal reflection
    # check top to bottom
    for i in range(rows-1):
        idx1 = i
        idx2 = i+1
        row1 = pattern[idx1]
        row2 = pattern[idx2]
        # if rows are equal
        # keep expanding
        if row1 == row2:
            while row1 == row2 and idx1 >= 0 and idx2 < rows:
                idx1 -= 1
                idx2 += 1
                try:
                    row1 = pattern[idx1]
                    row2 = pattern[idx2]
                except:
                    break
            # check that reached edge of pattern
            if idx1 == -1 or idx2 == rows:
                return (i+1)*100, 'horizontal', i


def reflections_corrected(pattern, previous):
    columns = len(pattern[0])
    rows = len(pattern)
    # vertical reflection
    # check left to right
    for i in range(columns-1):
        # check if previously identified
        if previous[0] == 'vertical' and previous[1] == i:
            continue

        idx1 = i
        idx2 = i+1
        col1 = [pattern[row][idx1] for row in range(rows)]
        col2 = [pattern[row][idx2] for row in range(rows)]
        # set to track 1 difference fix
        fixed = False
        # if columns are equal
        # keep expanding
        if col1 == col2 or (sum([col1[j]!=col2[j] for j in range(rows)])==1 and not fixed):
            while (col1 == col2 or (sum([col1[j]!=col2[j] for j in range(rows)])==1 and not fixed)) and idx1 >= 0 and idx2 < columns:
                # set that 1 difference was already ignored
                if sum([col1[j]!=col2[j] for j in range(rows)])==1:
                    fixed = True
                idx1 -= 1
                idx2 += 1
                try:
                    col1 = [pattern[row][idx1] for row in range(rows)]
                    col2 = [pattern[row][idx2] for row in range(rows)]
                except:
                    break
            # check that reached the end of pattern on at least one edge
            if idx1 == -1 or idx2 == columns:
                return i+1

    # horizontal reflection
    # check top to bottom
    for i in range(rows-1):
        # check if previously identified
        if previous[0] == 'horizontal' and previous[1] == i:
            continue

        idx1 = i
        idx2 = i+1
        row1 = pattern[idx1]
        row2 = pattern[idx2]
        # set to track 1 difference fix
        fixed = False
        # if rows are equal
        # keep expanding
        if row1 == row2 or (sum([row1[j]!=row2[j] for j in range(columns)])==1 and not fixed):
            while (row1 == row2 or (sum([row1[j]!=row2[j] for j in range(columns)])==1 and not fixed)) and idx1 >= 0 and idx2 < rows:
                # set that 1 difference was already ignored
                if sum([row1[j]!=row2[j] for j in range(columns)])==1:
                    fixed = True
                idx1 -= 1
                idx2 += 1
                try:
                    row1 = pattern[idx1]
                    row2 = pattern[idx2]
                except:
                    break
            # check that reached edge of pattern
            if idx1 == -1 or idx2 == rows:
                return (i+1)*100


    return None


def part_1(contents):
    contents.append('') # add a line to initiate the last pattern parsing
    pattern = []
    summary = 0
    reflection_lines = []
    for line in contents:
        # if empty line, means end of pattern
        # so find the reflection in the pattern
        # and add the appropriate amount to summary
        if line == '':
            value, orientation, idx = reflections(pattern)
            summary += value
            reflection_lines.append((orientation, idx))
            pattern = []
        # otherwise keep building the pattern
        else:
            pattern.append(line)

    return summary, reflection_lines


def part_2(contents, reflection_lines):
    pattern = []
    summary = 0
    pattern_idx = 0

    for line in contents:
        if line == '':
            summary += reflections_corrected(pattern, reflection_lines[pattern_idx])
            pattern = []
            pattern_idx += 1
        else:
            pattern.append(line)
    return summary


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result, test_reflection_lines = part_1(test)
    assert test_1_result==405, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    part_1_val, reflection_lines = part_1(contents)
    print(part_1_val)

    test_2_result = part_2(test, test_reflection_lines)
    #assert test_2_result==400, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents, reflection_lines))


if __name__ == '__main__':
    __main__()