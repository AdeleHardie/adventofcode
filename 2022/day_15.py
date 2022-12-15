from utils import parse_input


def print_grid(sensors, beacons, impossible):
    minc = min(min(sensors), min(beacons), min(impossible))
    maxc = max(max(sensors), max(beacons), max(impossible))
    #grid = []
    for y in range(minc[1], maxc[1]+1):
        line = []
        for x in range(minc[0], maxc[0]+1):
            pos = (x, y)
            if pos in sensors:
                line.append('S')
            elif pos in beacons:
                line.append('B')
            elif pos in impossible:
                line.append('#')
            else:
                line.append(' ')
        print(line)



def get_dist(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])


def no_beacons(sensor, beacon):
    no_beacons = set()
    dist = get_dist(sensor, beacon)

    for i in range(-dist, dist+1):
        y = sensor[1]+i
        xmin, xmax = 0, (dist-abs(i))+1
        for x in range(xmin, xmax):
            no_beacons.add((sensor[0]-x, y))
            no_beacons.add((sensor[0]+x, y))

    return no_beacons
        

def parse_grid(contents):
    sensors = {}
    beacons = set()

    for line in contents:
        parts = line.split()
        sensor = (int(parts[2].split('=')[1][:-1]), int(parts[3].split('=')[1][:-1]))
        beacon = (int(parts[8].split('=')[1][:-1]), int(parts[9].split('=')[1]))
        sensors[sensor] = get_dist(sensor, beacon)
        beacons.add(beacon)

    return sensors, beacons


def along_x(sensors, beacons, y):
    # find range sensor
    y_distances = {}
    for sensor in sensors:
        if abs(sensor[1]-y) <= sensors[sensor]:
            y_distances[sensor] = abs(sensor[1]-y)
    x_vals = {sensor: sensor[0] for sensor in sensors}
    closest_sensor = min(y_distances, key=y_distances.get)
    rightmost_sensor = max(x_vals, key=x_vals.get)
    minx = closest_sensor[0]-sensors[closest_sensor]
    maxx = rightmost_sensor[0]+sensors[rightmost_sensor]+1

    no_beacons = []
    for x in range(minx, maxx):
        pos = (x, y)
        if pos not in beacons:
            for sensor in sensors:
                distance = get_dist(pos, sensor)
                if distance <= sensors[sensor]:
                    no_beacons.append(pos)
                    break

    return no_beacons



def within_limits(sensors, beacons, limits):
    y = 0
    while y <= limits:
        x = 0
        print(' '*100, end='\r')
        while x <= limits:
            print(x, y, end='\r')
            pos = (x, y)
            seen = True
            if (pos not in beacons) and (pos not in sensors):
                for sensor in sensors:
                    distance = get_dist(pos, sensor)
                    if distance <= sensors[sensor]:
                        seen = False
                        x = sensors[sensor] - abs(pos[1]-sensor[1]) + sensor[0]
                        break
            else:
                seen = False
            if seen:
                print(' '*100)
                return pos[0]*4000000 + pos[1]
            x += 1
        y += 1

def part1(contents, y):
    sensors, beacons = parse_grid(contents)
    no_beacons = along_x(sensors, beacons, y)

    return len(no_beacons)


def part2(contents, limits):
    sensors, beacons = parse_grid(contents)
    freq = within_limits(sensors, beacons, limits)

    return freq


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))

    assert part1(test, 10)==26, 'failed part 1 test'
    #print(f'Part 1: {part1(contents, 2000000)}')

    assert part2(test, 20) == 56000011, 'failed part 2 test'
    print(f'Part 2: {part2(contents, 4000000)}')


if __name__ == '__main__':
    __main__()
