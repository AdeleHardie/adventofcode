from utils import parse_input


def run_HASH(input):
    value = 0
    for char in input:
        value += ord(char)
        value = (value*17)%256
    
    return value


def get_lens(input):
    if '=' in input:
        label = input.split('=')[0]
        action = 'add'
        focal = int(input.split('=')[1])
    else:
        label = input[:-1]
        action = 'remove'
        focal = None

    return label, action, focal


def add_lens(box, label, focal):
    for i, lens in enumerate(box):
        if lens[0] == label:
            box[i] = (label, focal)
            return box
    
    box.append((label, focal))
    return box


def remove_lens(box, label):
    for i, lens in enumerate(box):
        if lens[0] == label:
            del box[i]

    return box


def get_focusing_power(boxes):
    total = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            total += (i+1)*(j+1)*lens[1]

    return total


def part_1(contents):
    contents = contents[0].split(',')

    total = 0
    for input in contents:
        total += run_HASH(input)

    return total


def part_2(contents):
    contents = contents[0].split(',')
    boxes = [[]] * 256

    for input in contents:
        label, action, focal = get_lens(input)
        idx = run_HASH(label)
        box = boxes[idx].copy()
        # add lens
        if action == 'add':
            boxes[idx] = add_lens(box, label, focal)
        # remove lens
        elif action == 'remove':
            boxes[idx] = remove_lens(box, label)

    focusing_power = get_focusing_power(boxes)

    return focusing_power


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==1320, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test)
    assert test_2_result==145, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()