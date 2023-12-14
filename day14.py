FILE = "input.txt"

PLATFORMS = {}
CYCLES = int(1e9)

def rotate_platform(pf):
    return [[pf[i][j] for i in range(len(pf))][::-1] for j in range(len(pf[0]))]


def let_it_roll(pf):
    round_rocks = [(x, y) for x in range(len(pf)) for y in range(len(pf[x])) if pf[x][y] == 'O']

    for rock_x, rock_y in round_rocks:
        moved_rock_x = rock_x
        
        while moved_rock_x > 0 and pf[moved_rock_x-1][rock_y] == '.':
            moved_rock_x -= 1
        
        if moved_rock_x != rock_x:
            pf[moved_rock_x][rock_y] = 'O'
            pf[rock_x][rock_y] = '.'
    
    return pf


def cycle(pf):
    for _ in range(4):
        pf = rotate_platform(let_it_roll(pf))

    return pf


if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        platform = [list(line) for line in map(str.strip, file.readlines())]

        rolled_platform = let_it_roll(platform)
        
        print("Part 1:", sum(line.count('O') * (len(platform) - i) for i, line in enumerate(rolled_platform)))

    # part two 
    with open(FILE) as file:
        platform = [list(line) for line in map(str.strip, file.readlines())]
        
        pattern_start = 0
        pattern_length = 1
        
        for i in range(CYCLES):
            slug = tuple(map(tuple, platform))

            if slug in PLATFORMS:
                pattern_start = PLATFORMS[slug]
                pattern_length = i - pattern_start
                break
            
            platform = cycle(platform)
            PLATFORMS[slug] = i
        
        for _ in range((CYCLES - pattern_start) % pattern_length):
            platform = cycle(platform)
        
        print("Part 2:", sum(line.count('O') * (len(platform) - i) for i, line in enumerate(platform)))
