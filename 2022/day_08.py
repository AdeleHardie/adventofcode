from numpy import array as np_array, zeros
from utils import parse_input


def check_visible(grid):
    visible = set()

    # rows
    for i in range(len(grid)):
        max_height = -1
        for j in range(len(grid[0])):
            height = grid[i,j]
            coords = str([i,j])
            if height > max_height:
                max_height = height
                visible.add(coords)              
        # reverse
        max_height = -1
        for j in range(len(grid[0])-1, -1, -1):
            height = grid[i,j]
            coords = str([i,j])
            if height > max_height:
                max_height = height
                visible.add(coords)

    # columns
    for j in range(len(grid[0])):
        max_height = -1
        for i in range(len(grid)):
            height = grid[i,j]
            coords = str([i,j])
            if height > max_height:
                max_height = height
                visible.add(coords)
                    
        # reverse
        max_height = -1
        for i in range(len(grid)-1, -1, -1):
            height = grid[i,j]
            coords = str([i,j])
            if height > max_height:
                max_height = height
                visible.add(coords)

    return len(visible)


def score(a, b, grid):
    scores = []
    min_height = grid[a,b]
    #up
    max_height = -1
    score = 0
    for i in range(a-1, -1, -1):
        if grid[i,b] < min_height:
            score += 1
        else:
            score += 1
            break
    scores.append(score)
    #down
    max_height = -1
    score = 0
    for i in range(a+1, len(grid)):
        if grid[i,b] < min_height:
            score += 1
        else:
            score += 1
            break
    scores.append(score)
    #left
    max_height = -1
    score = 0
    for j in range(b-1, -1, -1):
        if grid[a,j] < min_height:
            score += 1
        else:
            score += 1
            break
    scores.append(score)
    #right
    max_height = -1
    score = 0
    for j in range(b+1, len(grid[0])):
        if grid[a,j] < min_height:
            score += 1
        else:
            score += 1
            break
    scores.append(score)
    curr_score = scores[0] * scores[1] * scores[2] * scores[3]
    
    return curr_score


def find_most_scenic(grid):
    all_scores = zeros(grid.shape, int)
    for a in range(len(grid)):
        for b in range(len(grid[0])):
            all_scores[a,b] = score(a,b,grid)

    return max(all_scores.flatten())


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    grid = np_array([[int(char) for char in line] for line in contents])
    test_grid = np_array([[int(char) for char in line] for line in test])

    assert check_visible(test_grid) == 21, 'failed part 1 test'
    print(f'Part 1: {check_visible(grid)}')
    
    assert find_most_scenic(test_grid) == 8, 'failed part 2 test'
    print(f'Part 2: {find_most_scenic(grid)}')


if __name__ == '__main__':
    __main__()
