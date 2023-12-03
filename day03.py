import re

FILE = "input.txt"

def isAdjacent(matrix, i, j):
    hasNeighbour = False
    max_y = min(j+2, len(matrix[i]))
    max_x = min(i+2, len(matrix))
    min_y = max(j-1, 0)
    min_x = max(i-1, 0)
    neighbours = [matrix[x][y] for x in range(min_x, max_x) for y in range(min_y, max_y) if not (x, y) == (i, j)]
    if any(neighbour not in '0123456789.' for neighbour in neighbours):
        hasNeighbour = True
    return hasNeighbour

def get_gear_ratio(matrix, numbers, i, j):
    max_y = min(j+2, len(matrix[i]))
    max_x = min(i+2, len(matrix))
    min_y = max(j-1, 0)
    min_x = max(i-1, 0)
    neighbours = [(x, y) for x in range(min_x, max_x) for y in range(min_y, max_y) if not (x, y) == (i, j)]
    possible_numbers = [[(x[0], i) for i in range(x[1], y[1]+1)] for (x, y) in numbers]
    adjacent_numbers = [*filter(lambda x: any(y in neighbours for y in x), possible_numbers)]
    if len(adjacent_numbers) == 2:
        number_values = [int(''.join(matrix[number[0][0]][number[0][1]:number[-1][1]+1])) for number in adjacent_numbers]
        return number_values[0] * number_values[1]
    else:
        return 0

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        matrix = [line.strip() for line in file.readlines()]
        numbers = [[(i, x.start(0)), (i, x.end(0)-1)] for i, line in enumerate(matrix) for x in re.finditer('\d+', line)]
        answer = sum([int("".join(matrix[a[0]][a[1]:b[1]+1])) for [a, b] in numbers if any(isAdjacent(matrix, a[0], y) for y in range(a[1], b[1] + 1))])
        print("Part 1:", answer)

    # part two 
    with open(FILE) as file:
        matrix = [line.strip() for line in file.readlines()]
        numbers = [[(i, x.start(0)), (i, x.end(0)-1)] for i, line in enumerate(matrix) for x in re.finditer('\d+', line)]
        possible_gears = [(i, x.end(0) - 1) for i, line in enumerate(matrix) for x in re.finditer('\*', line)]
        print("Part 2:", sum(get_gear_ratio(matrix, numbers, gear[0], gear[1]) for gear in possible_gears))