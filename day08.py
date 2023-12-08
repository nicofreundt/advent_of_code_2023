import re
import numpy as np
from multiprocessing import Pool, freeze_support

FILE = "input.txt"


if __name__ == "__main__":
    freeze_support()
    # part one
    with open(FILE) as file:
        instructions, _, *nodes = map(str.strip, file.readlines())
        nodes = {(matches:=re.findall('[A-Z]{3}', node))[0]: (matches[1], matches[2]) for node in nodes}
        instructions = [[0, 1][c == 'R'] for c in instructions]
        path_length = 0
        cur_node = ('AAA', nodes.get('AAA'))
        while cur_node[0] != 'ZZZ':
            next_instruction = instructions[(path_length) % len(instructions)]
            path_length += 1
            next_node = cur_node[1][next_instruction]
            cur_node = (next_node, nodes.get(next_node))
        print("Part 1:", path_length)
        
    # part two 
    with open(FILE) as file:
        instructions, _, *nodes = map(str.strip, file.readlines())

        nodes = {(matches:=re.findall('[A-Z0-9]+', node))[0]: (matches[1], matches[2]) for node in nodes}
        instructions = [[0, 1][c == 'R'] for c in instructions]

        cur_nodes = [(k, v) for k, v in nodes.items() if k.endswith('A')]
        
        def get_path_length(cur_node):
            cur_path = 0
            while not cur_node[0].endswith('Z'):
                next_instruction = instructions[(cur_path) % len(instructions)]
                cur_path += 1
                next_node = cur_node[1][next_instruction]
                cur_node = (next_node, nodes.get(next_node))
            return cur_path

        def process_path_lengths(func, arr, n_processors):
            with Pool(processes=n_processors) as pool:
                return pool.map(func, arr)

        path_lengths = process_path_lengths(get_path_length, cur_nodes, 12)
        
        # LCM of path lengths is equal to the path length, where all nodes end with 'Z'
        print("Part 2:", np.lcm.reduce(path_lengths))