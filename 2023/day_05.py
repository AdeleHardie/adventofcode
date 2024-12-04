from utils import parse_input


def parse_maps(contents):
    seeds = [int(seed) for seed in contents[0].split(':')[1].split()]
    maps = []
    current = []

    for line in contents[3:]:
        # line describes new map
        if ':' in line:
            maps.append(current)
            current = []
        elif line != '':
            values = [int(val) for val in line.split()]
            current.append([values[1], values[1]+values[2], values[0]-values[1]])
    maps.append(current)

    return seeds, maps


def map_seeds(seed, maps):
    for map in maps:
            # go over each range in map
            for limits in map:
                if limits[0] <= seed < limits[1]:
                    # if within limit
                    # add modifier for that range
                    seed = seed + limits[2]
                    break
    return seed


def part_1(contents):
    seeds, maps = parse_maps(contents)
    locations = []

    for seed in seeds:
        # go over each mapping
        for map in maps:
            # go over each range in map
            for limits in map:
                if limits[0] <= seed < limits[1]:
                    # if within limit
                    # add modifier for that range
                    seed = seed + limits[2]
                    break
        locations.append(seed)

    return min(locations)


def part_2(contents):
    seeds, maps = parse_maps(contents)

    # convert seed ranges
    ranges = []
    for i in range(0, len(seeds), 2):
        ranges.append([seeds[i], seeds[i]+seeds[i+1]-1])

    # remap ranges
    for map in maps:
        new_ranges = []
        for r in ranges:
            for limits in map:
                # if fully within map range
                if limits[0]<=r[0]<limits[1] and limits[0]<=r[1]<limits[1]:
                    new_ranges.append([r[0]+limits[2], r[1]+limits[2]])
                    r = None
                    break
                # if some less than range
                elif limits[0]>r[0] and limits[0]<=r[1]<limits[1]:
                    new_ranges.append([limits[0]+limits[2], r[1]+limits[2]]) # add mapped portion
                    r = [r[0], limits[0]-1] # leave unmapped portion to check other maps
                # if some more than range
                elif limits[0]<=r[0]<limits[1] and limits[1]<r[1]:
                    new_ranges.append([r[0]+limits[2], limits[1]-1+limits[2]]) # add mapped portion
                    r = [limits[1], r[1]]
                # if some more and some less than range
                elif r[0]<limits[0] and r[1]>limits[1]:
                    new_ranges.append([limits[0]+limits[2], limits[1]-1+limits[2]]) # add mapped portion
                    # keep checking one range, add the other to be checked later
                    r = [r[0], limits[0]-1]
                    ranges.append([limits[1], r[1]])
                # if completely outside map range
                # check with other maps
            if r is not None:
                new_ranges.append(r)
        # replace with remapped seed ranges
        ranges = new_ranges

    location_range_starts = [r[0] for r in ranges]
    return min(location_range_starts)


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    test_1_result = part_1(test)
    assert test_1_result==35, f'failed part 1 test with result {test_1_result}'
    print('Part 1:')
    print(part_1(contents))

    test_2_result = part_2(test)
    assert test_2_result==46, f'failed part 2 test with result {test_2_result}'

    print('Part 2:')
    print(part_2(contents))


if __name__ == '__main__':
    __main__()