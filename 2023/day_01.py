from utils import parse_input


digits = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}


def part_1(calibration):
    val = 0
    for line in calibration:
        number = ''
        for char in line:
            if char.isnumeric():
                number += char
                break
        for char in line[::-1]:
            if char.isnumeric():
                number += char
                break
        val += int(number)
    return val


def part_2(contents):
    value = 0
    for idx, line in enumerate(contents):
        numbers = []
        for i in range(len(line)):
            for j in range(i+1,len(line)+1):
                maybe_number = line[i:j]
                if maybe_number in digits:
                    numbers.append(digits[maybe_number])
                    break
                elif maybe_number.isnumeric():
                    numbers.append(maybe_number)
                    break
        value += int(f'{numbers[0]}{numbers[-1]}')
    return value


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==142, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test2 = ['two1nine',
             'eightwothree',
             'abcone2threexyz',
             'xtwone3four',
             '4nineeightseven2',
             'zoneight234',
             '7pqrstsixteen']
    test_2_result = part_2(test2)
    assert test_2_result==281, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()