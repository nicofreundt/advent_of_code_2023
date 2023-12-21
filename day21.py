import math

FILE = "input.txt"
DIRECTIONS = [*zip(x:=[-1, 0, 1, 0], x[::-1])]

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        grid = [[c for c in line.strip()] for line in file.readlines()]
        start = (math.floor(len(grid)/2), math.floor(len(grid[0])/2))
        
        end_plots = set()
        visited_plot_states = []
        
        steps = [(0, start)]
        max_steps = 64
        
        while steps:
            i, (x, y) = steps.pop(0)
        
            print(f"Part 1: step {i} of {max_steps}", end="\r")
        
            if (i, (x, y)) in visited_plot_states:
                continue
        
            visited_plot_states.append((i, (x, y)))
        
            if i >= max_steps:
                end_plots.add((x, y))
                continue
        
            for dx, dy in DIRECTIONS:
                next_x = x + dx
                next_y = y + dy
        
                if grid[next_x][next_y] != '#':
                    steps.append((i+1, (next_x, next_y)))
        
        print("\33[2K", end="\r")
        print("Part 1:", len(end_plots))

    # part two 
    with open(FILE) as file:
        grid = [[c for c in line.strip()] for line in file.readlines()]
        start = (math.floor(len(grid)/2), math.floor(len(grid[0])/2))
        # TODO: 26501365 steps in infinite grid
        print("Part 2:", "...")
