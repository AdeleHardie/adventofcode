from utils import parse_input


def part_1(contents, rules):
    possible_games = []
    for game in contents:
        game = game.split(':')
        game_id = int(game[0].split()[1])

        possible = True
        # go over cubes shown
        grabs = game[1].strip().split(';')
        for grab in grabs:
            # all cubes shown
            cubes = grab.strip().split(',')
            for cube in cubes:
                # colour and number
                values = cube.split()
                # check if possible according to rules
                if int(values[0]) > rules[values[1]]:
                    possible = False
        if possible:
            possible_games.append(game_id)
    return sum(possible_games)


def part_2(contents):
    powers = []

    for game in contents:
        fewest_cubes = {'red': 0, 'green': 0, 'blue': 0}
        # go over cubes shown
        grabs = game.split(':')[1].strip().split(';')
        for grab in grabs:
            # all cubes shown
            cubes = grab.strip().split(',')
            for cube in cubes:
                # colour and number
                values = cube.split()
                # adjust minimum number possible
                if fewest_cubes[values[1]] < int(values[0]):
                    fewest_cubes[values[1]] = int(values[0])
        # compute powers of the game
        powers.append(fewest_cubes['red']*fewest_cubes['blue']*fewest_cubes['green'])

    return sum(powers)


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test, {'red': 12, 'green': 13, 'blue': 14})
    assert test_1_result==8, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents, {'red': 12, 'green': 13, 'blue': 14}))

    test2 = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
             'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
             'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
             'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
             'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
    test_2_result = part_2(test2)
    assert test_2_result==2286, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()