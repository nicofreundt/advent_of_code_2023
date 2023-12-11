from collections import defaultdict
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def find_shortest_paths(matrix, multiplier):
    rows = len(matrix)
    cols = len(matrix[0])
    nodes = []
    graph = defaultdict(dict)
    
    empty_rows = 0
    for i in range(rows):
        if len(set(matrix[i])) == 1:
            empty_rows += 1
        else:
            empty_cols = 0
            for j in range(cols):
                if len(set(matrix[x][j] for x in range(rows))) == 1:
                    empty_cols += 1
                else:
                    if matrix[i][j] == '#':
                        nodes.append((i + (empty_rows * multiplier), j + (empty_cols * multiplier)))
    
    for src in nodes:
        for dest in nodes:
            if src != dest:
                graph[src][dest] = float('inf')
    
    for src in nodes:
        for dest in nodes:
            if src != dest:
                src_i, src_j = src
                dest_i, dest_j = dest
                distance = abs(dest_i - src_i) + abs(dest_j - src_j)
                graph[src][dest] = distance
    
    shortest_paths = {}
    for src in nodes:
        shortest_paths[src] = dijkstra(graph, src)
    
    return shortest_paths

if __name__ == "__main__":
    # Part one
    with open('input.txt') as file:
        input_matrix = [[c for c in line.strip()] for line in file.readlines()]

        shortest_paths = find_shortest_paths(input_matrix, 1)
        distinct_paths = {}
        
        for src in shortest_paths:
            for dest, distance in shortest_paths[src].items():
                distinct_paths[''.join(f"({a}, {b})" for a, b in sorted([src, dest]))] = distance

        print("Part 1:", sum(distinct_paths.values()))

    # Part two
    with open('input.txt') as file:
        input_matrix = [[c for c in line.strip()] for line in file.readlines()]

        shortest_paths = find_shortest_paths(input_matrix, 999999)
        distinct_paths = {}
        
        for src in shortest_paths:
            for dest, distance in shortest_paths[src].items():
                distinct_paths[''.join(f"({a}, {b})" for a, b in sorted([src, dest]))] = distance
        
        print("Part 2:", sum(distinct_paths.values()))
