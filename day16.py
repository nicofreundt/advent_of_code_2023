import sys
sys.setrecursionlimit(50000)

FILE = "input.txt"

DIRECTIONS = {
    'RIGHT': (0, 1),
    'LEFT': (0, -1),
    'UP': (-1, 0),
    'DOWN': (1, 0)
}

def bounce_around(contraption, x, y, dir, path):
    if (dir, (x, y)) in VISITED:
        return path
    else:
        VISITED.append((dir, (x, y)))

    if x not in range(0, len(contraption)) or y not in range(0, len(contraption[0])):
        return path[:-1]

    if contraption[x][y] == '.':
        next = (x+DIRECTIONS[dir][0], y+DIRECTIONS[dir][1])
        path += bounce_around(contraption, next[0], next[1], dir, [next])
    else:
        if contraption[x][y] == '|':
            if dir in ['RIGHT', 'LEFT']:
                next_dir_one = 'UP'
                next_one = (x+DIRECTIONS[next_dir_one][0], y+DIRECTIONS[next_dir_one][1])
                next_dir_two = 'DOWN'
                next_two = (x+DIRECTIONS[next_dir_two][0], y+DIRECTIONS[next_dir_two][1])
                path += bounce_around(contraption, next_one[0], next_one[1], next_dir_one, [next_one])
                path += bounce_around(contraption, next_two[0], next_two[1], next_dir_two, [next_two])
            elif dir in ['UP', 'DOWN']:
                next = (x+DIRECTIONS[dir][0], y+DIRECTIONS[dir][1])
                path += bounce_around(contraption, next[0], next[1], dir, [next])
        elif contraption[x][y] == '-':
            if dir in ['UP', 'DOWN']:
                next_dir_one = 'RIGHT'
                next_one = (x+DIRECTIONS[next_dir_one][0], y+DIRECTIONS[next_dir_one][1])
                next_dir_two = 'LEFT'
                next_two = (x+DIRECTIONS[next_dir_two][0], y+DIRECTIONS[next_dir_two][1])
                path += bounce_around(contraption, next_one[0], next_one[1], next_dir_one, [next_one])
                path += bounce_around(contraption, next_two[0], next_two[1], next_dir_two, [next_two])
            elif dir in ['RIGHT', 'LEFT']:
                next = (x+DIRECTIONS[dir][0], y+DIRECTIONS[dir][1])
                path += bounce_around(contraption, next[0], next[1], dir, [next])
        elif contraption[x][y] == '\\':
            if dir == "RIGHT":
                dir = 'DOWN'
                next = (x+DIRECTIONS[dir][0], y+DIRECTIONS[dir][1])
                path += bounce_around(contraption, next[0], next[1], dir, [next])
            elif dir == "LEFT":
                dir = 'UP'
                next = (x+DIRECTIONS[dir][0], y+DIRECTIONS[dir][1])
                path += bounce_around(contraption, next[0], next[1], dir, [next])
            elif dir == "UP":
                dir = 'LEFT'
                next = (x+DIRECTIONS[dir][0], y+DIRECTIONS[dir][1])
                path += bounce_around(contraption, next[0], next[1], dir, [next])
            elif dir == "DOWN":
                dir = 'RIGHT'
                next = (x+DIRECTIONS[dir][0], y+DIRECTIONS[dir][1])
                path += bounce_around(contraption, next[0], next[1], dir, [next])
        elif contraption[x][y] == '/':
            if dir == "RIGHT":
                dir = 'UP'
                next = (x+DIRECTIONS[dir][0], y+DIRECTIONS[dir][1])
                path += bounce_around(contraption, next[0], next[1], dir, [next])
            elif dir == "LEFT":
                dir = 'DOWN'
                next = (x+DIRECTIONS[dir][0], y+DIRECTIONS[dir][1])
                path += bounce_around(contraption, next[0], next[1], dir, [next])
            elif dir == "UP":
                dir = 'RIGHT'
                next = (x+DIRECTIONS[dir][0], y+DIRECTIONS[dir][1])
                path += bounce_around(contraption, next[0], next[1], dir, [next])
            elif dir == "DOWN":
                dir = 'LEFT'
                next = (x+DIRECTIONS[dir][0], y+DIRECTIONS[dir][1])
                path += bounce_around(contraption, next[0], next[1], dir, [next])
    return path


if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        matrix = [line.strip() for line in file.readlines()]
        
        start = (0, 0)
        
        VISITED = []
        
        print("Part 1:", len([*filter(lambda x: 0 <= x[0] < len(matrix) and 0 <= x[1] < len(matrix[0]),set(bounce_around(matrix, 0, 0, 'RIGHT', [start])))]))

    # part two 
    with open(FILE) as file:
        matrix = [line.strip() for line in file.readlines()]
        
        starts = [(0, y) for y in range(0, len(matrix[0]))]
        
        starts += [(len(matrix) - 1, y) for y in range(0, len(matrix[0]))]
        starts += [(y, 0) for y in range(0, len(matrix))]
        starts += [(y, len(matrix[0]) - 1) for y in range(0, len(matrix))]
        
        max_path = 0
        
        for i, start in enumerate(starts):
            print(f"Part 2: {i/len(starts)*100:.2f}%", end="\r")
            
            VISITED = []
            
            if start[0] == 0:
                direction = 'DOWN'
            elif start[0] == len(matrix) - 1:
                direction = 'UP'
            elif start[1] == 0:
                direction = 'RIGHT'
            else:
                direction = 'LEFT'
            
            max_path = max(max_path, len([*filter(lambda x: 0 <= x[0] < len(matrix) and 0 <= x[1] < len(matrix[0]),set(bounce_around(matrix, start[0], start[1], direction, [start])))]))
        
        print("\33[2K", end="\r")
        print("Part 2:", max_path)
