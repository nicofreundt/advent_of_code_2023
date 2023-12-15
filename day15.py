import re
from collections import defaultdict

FILE = "input.txt"

BOXES = defaultdict(list)

def HASH(step):
    cur_val = 0
    for c in step:
        cur_val += ord(c)
        cur_val *= 17
        cur_val %= 256
    return cur_val

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        print("Part 1:", sum(map(HASH, file.readline().split(','))))

    # part two 
    with open(FILE) as file:
        for part in file.readline().split(','):
            label, operation, focal_length = re.search('([a-z]+)(-|=)(\d+|$)', part).groups()
            box = HASH(label)
            filtered_box = [*filter(lambda slot: slot[0] == label, BOXES[box])]
            if operation == '=':
                if len(filtered_box) == 0:
                    BOXES[box].append((label, focal_length))
                else:
                    BOXES[box].insert(BOXES[box].index(filtered_box[0]), (label, focal_length))
                    BOXES[box].remove(filtered_box[0])
            if operation == '-' and len(filtered_box) > 0:
                BOXES[box].remove(filtered_box[0])
        print("Part 2:", sum((k+1)*int(slot[1])*(i+1) for k, list in BOXES.items() for i, slot in enumerate(list) if len(list) > 0))