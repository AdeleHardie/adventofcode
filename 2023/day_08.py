from utils import parse_input
from math import lcm


def process_map(map):
    directions = map[0]
    nodes = {}
    for node in map[2:]:
        name = node.split('=')[0].strip()
        connections = node.split('=')[1][2:-1].split(', ')
        nodes[name] = connections

    return directions, nodes


def part_1(contents):
    directions, nodes = process_map(contents)

    steps = 0
    current_node = 'AAA'

    while current_node != 'ZZZ':
        direction = directions[steps%len(directions)]
        if direction == 'L':
            current_node = nodes[current_node][0]
        elif direction == 'R':
            current_node = nodes[current_node][1]
        steps += 1

    return steps


def part_2(contents):
    directions, nodes = process_map(contents)

    # find all nodes ending with 'A'
    starting_nodes = [node for node in nodes if node.endswith('A')]

    node_steps = []
    for node in starting_nodes:
        steps = 0
        while not node.endswith('Z'):
            direction = directions[steps%len(directions)]
            if direction == 'L':
                node = nodes[node][0]
            elif direction == 'R':
                node = nodes[node][1]
            steps += 1
        node_steps.append(steps)

    common = 1
    for steps in node_steps:
        common = lcm(common, steps)

    return common 


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==6, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test2 = ['LR',
             '',
             '11A = (11B, XXX)',
             '11B = (XXX, 11Z)',
             '11Z = (11B, XXX)',
             '22A = (22B, XXX)',
             '22B = (22C, 22C)',
             '22C = (22Z, 22Z)',
             '22Z = (22B, 22B)',
             'XXX = (XXX, XXX)']
    test_2_result = part_2(test2)
    #assert test_2_result==6, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()