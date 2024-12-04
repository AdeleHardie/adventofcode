from utils import parse_input


def hand_value1(cards):
    counts = [cards.count(card) for card in set(cards)]
    if 5 in counts:
        value = 7
    elif 4 in counts:
        value = 6
    elif 3 in counts and 2 in counts:
        value = 5
    elif 3 in counts:
        value = 4
    elif counts.count(2) == 2:
        value = 3
    elif 2 in counts:
        value = 2
    else:
        value = 1
    
    return value


def remap_cards(hand, joker):
    if joker:
        card_map = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
    else:
        card_map = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    hand_remap = []
    for card in hand:
        if card in card_map:
            hand_remap.append(card_map[card])
        else:
            hand_remap.append(int(card))
    return hand_remap


def compare_cards(hand1, hand2, joker):
    hand1_remap = remap_cards(hand1, joker)
    hand2_remap = remap_cards(hand2, joker)

    for c1, c2 in zip(hand1_remap, hand2_remap):
        if c1 > c2:
            return True
        elif c2 > c1:
            return False


def part_1(contents):
    ranking = [0]
    values = [hand_value1(contents[0].split()[0])]

    for i in range(1, len(contents)):
        # compute card values
        cards = contents[i].split()[0]
        value = hand_value1(cards)
        values.append(value)

        added = False
        # find spot in rankings
        for j, idx in enumerate(ranking):
            value2 = values[idx]
            # if current hand better, keep going
            if value > value2:
                continue
            # if the same value, compare cards
            if value == value2:
                higher_card = compare_cards(cards, contents[idx].split()[0], False)
                # continue if hand is higher
                if higher_card:
                    continue
            # when reach hand that is not higher
            # insert index into ranking
            ranking.insert(j, i)
            added = True
            break
        # if was the highest card, append
        if not added:
            ranking.append(i)

    winnings = []
    for i, idx in enumerate(ranking):
        winnings.append(int(contents[idx].split()[1])*(i+1))
        
    return sum(winnings)


def hand_value2(cards):
    # replace all Js
    joker_count = cards.count('J')
    cards = cards.replace('J', '')

    # count all cards
    counts = [cards.count(card) for card in set(cards)]
    counts.sort(reverse=True)
    if len(counts) > 0:
        counts[0] += joker_count
    else:
        counts = [5]
    if 5 in counts:
        value = 7
    elif 4 in counts:
        value = 6
    elif 3 in counts and 2 in counts:
        value = 5
    elif 3 in counts:
        value = 4
    elif counts.count(2) == 2:
        value = 3
    elif 2 in counts:
        value = 2
    else:
        value = 1

    return value


def part_2(contents):
    ranking = [0]
    values = [hand_value2(contents[0].split()[0])]

    for i in range(1, len(contents)):
        # compute card values
        cards = contents[i].split()[0]
        value = hand_value2(cards)
        values.append(value)

        added = False
        # find spot in rankings
        for j, idx in enumerate(ranking):
            value2 = values[idx]
            # if current hand better, keep going
            if value > value2:
                continue
            # if the same value, compare cards
            if value == value2:
                higher_card = compare_cards(cards, contents[idx].split()[0], True)
                # continue if hand is higher
                if higher_card:
                    continue
            # when reach hand that is not higher
            # insert index into ranking
            ranking.insert(j, i)
            added = True
            break
        # if was the highest card, append
        if not added:
            ranking.append(i)

    winnings = []
    for i, idx in enumerate(ranking):
        winnings.append(int(contents[idx].split()[1])*(i+1))
        
    return sum(winnings)


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==6440, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test)
    assert test_2_result==5905, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()