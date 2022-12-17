import numpy as np
from utils import parse_input
import time

rocks = np.array([[[0,0], [1,0], [2,0], [3,0]],
                 [[1,2], [0,1], [1,1], [2,1], [1,0]],
                 [[2,2], [2,1], [0,0], [1,0], [2,0]],
                 [[0,3], [0,2], [0,1], [0,0]],
                 [[0,1], [1,1], [0,0], [1,0]]])


class Chamber:
    def __init__(self, wind):
        self.contents = []
        self._process_wind(wind)
        self.x = 7


    def _process_wind(self, wind):
        self.wind = []
        for val in wind:
            if val == '>':
                self.wind.append(np.array([1,0]))
            else:
                self.wind.append(np.array([-1,0]))

    def get_wind(self):
        result = self.wind[self.wind_idx]
        self.wind_idx = (self.wind_idx+1)%len(self.wind)
        return result

    def add_rock(self, rock):
        for coord in rock:
            self.resting_rocks.append(list(coord))
        # only care about the most recent rocks
        self.resting_rocks = self.resting_rocks[-1000:]

    def setup_rock(self, rock):
        vec = np.array([2, self.y+3])
        new_rock = rock + vec
        return new_rock

    def move_rock(self, rock, vec):
        new_rock = rock + vec
        # check for outside grid
        if any(new_rock[:,0]<0) or any(new_rock[:,0]>=self.x) or any(new_rock[:,1]<0):
            return rock, True
        # check for clashes with other rocks
        if any([list(coord) in self.resting_rocks for coord in new_rock]):
            return rock, True
        return new_rock, False

    def find_period(self, i):
        floor = ''
        for y in range(self.y-1, self.y-6, -1):
            for x in range(7):
                if [x,y] in self.resting_rocks:
                    floor += '#'
                else:
                    floor += '.'
        state = (floor, i%5, self.wind_idx)
        if state in self.states:
            i_period = i - self.states[state][1]
            y_period = self.y - self.states[state][0]
            return floor, i_period, y_period
        else:
            self.states[state] = (self.y, i)

    def recreate_floor(self, floor):
        # add top rock coordinates for checking
        floor_chunk = [floor[i:i+7] for i in range(0, len(floor), 7)]
        for y, level in enumerate(floor_chunk):
            for x, val in enumerate(level):
                # if rock there
                if val == '#':
                    self.resting_rocks.append([x, self.y-(y+1)])

    def rocks_fall(self, num):
        # reset state
        self.y = 0
        self.resting_rocks = []
        self.states = {}
        self.wind_idx = 0

        cycle = False
        down_vec = np.array([0,-1])
        i = 0
        while i < num:
            # get rock to fall
            rock = rocks[i%5]
            # setup rock starting position
            rock = self.setup_rock(rock)
            falling = True
            while falling:
                # wind blows
                wind = self.get_wind()
                wind_rock, rejected = self.move_rock(rock, wind)
                # fall down
                down_rock, rejected = self.move_rock(wind_rock, down_vec)
                # check if still falling
                if rejected:
                    falling = False
                # new rock position
                rock = down_rock
            # add resting coordinates
            self.add_rock(down_rock)
            # update max height
            self.y = max(max(down_rock[:,1])+1, self.y)
            #find cycle
            if i > 10 and not cycle:
                result = self.find_period(i)
                if result is not None:
                    floor, i_period, y_period = result
                    # jump to i
                    iters = ((num - i) // i_period)
                    i += i_period*iters
                    self.y += y_period*iters
                    self.recreate_floor(floor)
                    cycle = True
            # next iteration
            i += 1

        return self.y  


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))

    test_c = Chamber(test[0])
    c = Chamber(contents[0])

    start_time = time.time()
    #assert test_c.rocks_fall(2022) == 3068, 'failed part 1 test'
    print(f'Part 1: {c.rocks_fall(2022)}')
    print(time.time()-start_time)

    start_time = time.time()
    #assert test_c.rocks_fall(1000000000000) == 1514285714288, 'failed part 2 test'
    print(f'Part 2: {c.rocks_fall(1000000000000)}')
    print(time.time()-start_time)


if __name__ == '__main__':
    __main__()
