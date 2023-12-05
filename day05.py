import re

FILE = "input.txt"

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        seeds, *info_maps = [[*map(int, re.findall('\d+', part))] for part in file.read().split('\n\n')]
        info_maps = [[(info_map[i], info_map[i+1], info_map[i+2]) for i in range(0, len(info_map), 3)] for info_map in info_maps]
        locations = []
        for seed in seeds:
            for info_map in info_maps:
                for (d, s, r) in info_map:
                    if seed in range(s, s+r):
                        seed = seed-s+d
                        break
            locations.append(seed)
        print("Part 1:", min(locations))

    # part two 
    # not efficient, but I got the correct solution...
    with open(FILE) as file:
        seeds, *info_maps = [[*map(int, re.findall('\d+', part))] for part in file.read().split('\n\n')]
        info_maps = [[(info_map[i], info_map[i+1], info_map[i+2]) for i in range(0, len(info_map), 3)] for info_map in info_maps]
        seed_ranges = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]
        location = -1
        cur_seed = location
        while not any(a <= cur_seed < b for (a, b) in seed_ranges):
            location += 1
            cur_seed = location
            for info_map in info_maps[::-1]:
                for (d,s,r) in info_map:
                    if d <= cur_seed < d+r:
                        cur_seed = cur_seed-d+s
                        break
        print("Part 2:", location)