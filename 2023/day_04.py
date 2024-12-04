from utils import parse_input


def part_1(contents):
    points = []
    for card in contents:
        winning_numbers = card.split(':')[1].split('|')[0].split()
        numbers = card.split(':')[1].split('|')[1].split()
        num_match = sum([num in winning_numbers for num in numbers])
        if num_match > 0:
            points.append(2**(num_match-1))
    return sum(points)


def part_2(contents):
    # start with 1 of each card
    number_of_cards = [1]*len(contents)

    for i, card in enumerate(contents):
        # find number of matching numbers
        winning_numbers = card.split(':')[1].split('|')[0].split()
        numbers = card.split(':')[1].split('|')[1].split()
        num_match = sum([num in winning_numbers for num in numbers])
        
        # add the copies of cards
        # as many as there are instances of current card
        for j in range(num_match):
            if i+j+1 >= len(number_of_cards):
                break
            number_of_cards[i+j+1] += number_of_cards[i]

    return sum(number_of_cards)


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==13, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test)
    assert test_2_result==30, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()