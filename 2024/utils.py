def parse_input(day):
    with open(f'inputs/{day}.txt', 'r') as file:
        contents = file.readlines()
    contents = [line.replace('\n', '') for line in contents]

    with open(f'inputs/{day}_test.txt', 'r') as file:
        test = file.readlines()
    test = [line.replace('\n', '') for line in test]

    return contents, test
