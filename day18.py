import re

FILE = "input.txt"

def shoelace_formula(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += (vertices[i][0] * vertices[j][1]) - (vertices[j][0] * vertices[i][1])
    return abs(area) // 2

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        dig_plan = [dig.strip().split() for dig in file.readlines()]

        start = (0, 0)
        dig_path = [start]
        
        for dir, dist, color in dig_plan:
            dist = int(dist)
        
            if dir == 'R':
                end = (start[0], start[1]+dist)
            elif dir == 'L':
                end = (start[0], start[1]-dist)
            elif dir == 'U':
                end = (start[0]-dist, start[1])
            else:
                end = (start[0]+dist, start[1])
        
            dig_path.append(end)
            start = end
        
        path_len = sum(int(dist) for _, dist, _ in dig_plan)
        print("Part 1:", shoelace_formula(dig_path[:-1]) + path_len // 2 + 1)

    # part two 
    with open(FILE) as file:
        dig_plan = [dig.strip().split() for dig in file.readlines()]
        dig_plan = [re.findall("#([a-z0-9]{5})([0-3])", color)[0] for _, _, color in dig_plan]

        start = (0, 0)
        dig_path = [start]

        for dist, dir in dig_plan:
            dist = int(dist, 16)
            
            if dir == '0':
                end = (start[0], start[1]+dist)
            elif dir == '1':
                end = (start[0]+dist, start[1])
            elif dir == '2':
                end = (start[0], start[1]-dist)
            else:
                end = (start[0]-dist, start[1])
            
            dig_path.append(end)
            start = end

        path_len = sum(int(dist, 16) for dist, _ in dig_plan)
        print("Part 2:", shoelace_formula(dig_path[:-1]) + path_len // 2 + 1)