import heapq

FILE = "input.txt"
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_min_heat_loss(grid, validate):
    queue = [(0, 0, 0, -1, -1)]
    loss_map = {}

    while queue:
        past_loss, x, y, cur_dir, dir_count = heapq.heappop(queue)

        if (x, y, cur_dir, dir_count) in loss_map:
            continue
        
        loss_map[(x, y, cur_dir, dir_count)] = past_loss
        
        for new_dir, (dx, dy) in enumerate(DIRECTIONS):
            new_x, new_y = x + dx, y + dy
            new_dir_count = 1 if new_dir != cur_dir else dir_count + 1

            not_reverse = (new_dir + 2)%4 != cur_dir

            is_valid = validate(cur_dir, new_dir, dir_count, new_dir_count)
            in_range = 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])

            if is_valid and not_reverse and in_range:
                heapq.heappush(queue, (past_loss + grid[new_x][new_y], new_x, new_y, new_dir, new_dir_count))

    min_heat_loss = float('inf')
    
    for _, loss in filter(lambda k: k[0][0] == len(grid)-1 and k[0][1] == len(grid[0])-1, loss_map.items()):
        min_heat_loss = min(min_heat_loss, loss)
    
    return min_heat_loss

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        grid = [[*map(int, line.strip())] for line in file.readlines()]
        print("Part 1:", get_min_heat_loss(grid, lambda *x: x[3] <= 3))

    # part two 
    with open(FILE) as file:
        grid = [[*map(int, line.strip())] for line in file.readlines()]
        print("Part 2:", get_min_heat_loss(grid, lambda cur_dir, new_dir, dir_count, new_dir_count: new_dir_count <= 10 and (new_dir == cur_dir or dir_count >= 4 or dir_count == -1)))