from utils import parse_input


class Troop:
    def __init__(self):
        self._monkeys = []
        self.divisor = 1

    def __getitem__(self, idx):
        return self._monkeys[idx]

    def add(self, monkey, idx):
        self._monkeys.insert(idx, monkey)

    def mod(self):
        # get common divisor
        if self.divisor == 1:
            for monkey in self._monkeys:
                self.divisor *= monkey.divisor

        for monkey in self._monkeys:
            for i, item in enumerate(monkey.items):
                monkey.items[i] = item % self.divisor

    def round(self, worry=None):
        # normalise all items
        self.mod()

        for monkey in self._monkeys:
            items, recipients = monkey.take_turn(worry)
            for item, idx in zip(items, recipients):
                self._monkeys[idx].catch(item)

    def get_monkey_business(self):
        handled = [monkey.num_handled for monkey in self._monkeys]
        handled.sort(reverse=True)
        return handled[0]*handled[1]


class Monkey:
    def __init__(self, description):
        self.idx = int(description[0].split()[-1][:-1])
        self.items = [int(item.replace(',', '')) for item in description[1].split()[2:]]
        self.operation = description[2].replace('  Operation: new = ', '')
        self.divisor = int(description[3].split()[-1])
        self.results = [int(line.split()[-1]) for line in description[4:]]
        self.num_handled = 0

    def run_operation(self, item):
        parts = self.operation.split()
        
        if parts[2] == 'old':
            num = item
        else:
            num = int(parts[2])
        if parts[1] == '+':
            return item + num
        elif parts[1] == '*':
            return item * num

    def test(self, item):
        if item % self.divisor == 0:
            return self.results[0]
        else:
            return self.results[1]

    def take_turn(self, worry=None):
        toss = []
        to_monkey = []
        for item in self.items:
            self.num_handled += 1
            item = self.run_operation(item)
            if worry is not None:
                item = item // worry
            toss.append(item)
            to_monkey.append(self.test(item))
        self.items = []

        return toss, to_monkey

    def catch(self, item):
        self.items.append(item)


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    contents = '_'.join(contents).split('__')

    # part 1
    troop = Troop()
    for description in contents:
        monkey = Monkey(description.split('_'))
        troop.add(monkey, monkey.idx)
    for _ in range(20):
        troop.round(3)
    print(f'Part 1: {troop.get_monkey_business()}')

    # part 2
    # reset troop
    troop = Troop()
    for description in contents:
        monkey = Monkey(description.split('_'))
        troop.add(monkey, monkey.idx)
    for _ in range(10000):
        troop.round()
    print(f'Part 2: {troop.get_monkey_business()}')


if __name__ == '__main__':
    __main__()
