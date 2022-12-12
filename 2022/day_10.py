from utils import parse_input

def part_1(contents):
    x = 1
    cycle = 0
    strengths = []

    for line in contents:
        if line == 'noop':
            cycle += 1
            strengths.append(x*cycle)
        else:
            num = int(line.split()[1])
            for _ in range(2):
                cycle += 1
                strengths.append(x*cycle)
            x += num

    return strengths


def part_2_cycle(x, line, output):
    if len(line)+1 in range(x, x+3):
        line.append('▮')
    else:
        line.append(' ')
        
    if len(line) == 40:
        output.append(line)
        line = []
        
    return line, output


def part_2(contents):
    x = 1
    sprite = 1
    curr_crt = []
    output = []
    
    for line in contents:
        if line == 'noop':
            curr_crt, output = part_2_cycle(x, curr_crt, output)
        elif line.startswith('addx'):
            num = int(line.split()[1])
            for _ in range(2):
                curr_crt, output = part_2_cycle(x, curr_crt, output)
            x += num
    
    for line in output:
        print(''.join(line))


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    print(f'Part 1: {sum(part_1(contents)[19::40])}')

    print('Part 2:')
    part_2(contents)


if __name__ == '__main__':
    __main__()
