FILE = "input.txt"

PIPES = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)],
    'F': [(0, 1), (1, 0)],
}

def is_valid_pipe(point):
    is_pipe = 0 <= point[0] < len(matrix) and 0 <= point[1] < len(matrix[0]) and matrix[point[0]][point[1]] in PIPES.keys()
    return is_pipe

def is_loop(cur, next):
    cur_pipe = matrix[cur[0]][cur[1]]
    next_pipe = matrix[next[0]][next[1]]
    if cur_pipe == 'S':
        # consider all neighbours possible
        paths = PIPES.get(next_pipe)
        next_to_cur = any(pos == cur for pos in [(next[0] + path[0], next[1] + path[1]) for path in paths])
        return next_to_cur
    else:
        # consider just two neighbours possible
        next_paths = PIPES.get(next_pipe)
        cur_paths = PIPES.get(cur_pipe)
        next_to_cur = any(pos == cur for pos in [(next[0] + path[0], next[1] + path[1]) for path in next_paths])
        cur_to_next = any(pos == next for pos in [(cur[0] + path[0], cur[1] + path[1]) for path in cur_paths])
        return next_to_cur and cur_to_next
    
def get_neighbours(cur):
    return list(filter(lambda x: is_valid_pipe(x) and is_loop(cur, x), [
            (cur[0] - 1, cur[1]), 
            (cur[0] + 1, cur[1]), 
            (cur[0], cur[1] - 1), 
            (cur[0], cur[1] + 1)
        ]))

def shoelace_formula(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += (vertices[i][0] * vertices[j][1]) - (vertices[j][0] * vertices[i][1])
    return abs(area) / 2

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        matrix = [line.strip() for line in file.readlines()]
        
        start_line = [*filter(lambda line: 'S' in line, matrix)][0]
        start = (matrix.index(start_line), start_line.index('S'))
        
        neighbours = get_neighbours(start)
        loop = [start, *neighbours]
        cur_pipe = loop[1]
        
        while True:
            next_neighbours = get_neighbours(cur_pipe)
            if start in next_neighbours and len(loop) > 3:
                break
            next_neighbour = [*filter(lambda x: x not in loop, next_neighbours)]
            if len(next_neighbour) == 0:
                break
            cur_pipe = next_neighbour[0]
            loop.append(cur_pipe)
        
        print("Part 1:", len(loop)//2)

    # part two 
    with open(FILE) as file:
        matrix = [line.strip() for line in file.readlines()]
        
        start_line = [*filter(lambda line: 'S' in line, matrix)][0]
        start = (matrix.index(start_line), start_line.index('S'))
        
        neighbours = get_neighbours(start)
        loop = [start, neighbours[0]]
        cur_pipe = loop[1]

        while True:
            next_neighbours = get_neighbours(cur_pipe)
            if start in next_neighbours and len(loop) > 2:
                break
            next_neighbour = [*filter(lambda x: x not in loop, next_neighbours)]
            if len(next_neighbour) == 0:
                break
            cur_pipe = next_neighbour[0]
            loop.append(cur_pipe)

        print("Part 2:", int(shoelace_formula(loop) - (len(loop)//2) + 1))
