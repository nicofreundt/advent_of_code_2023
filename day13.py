FILE = "input.txt"

def rotate_pattern(pattern):
    return [[pattern[i][j] for i in range(len(pattern))][::-1] for j in range(len(pattern[0]))]

def get_mirror_size(pattern, max_fault=0):
    for i in range(1, len(pattern)):
        max_size = min(i, len(pattern) - i)
        first_half = ''.join(''.join(line) for line in pattern[i-max_size:i])
        second_half = ''.join(''.join(line) for line in pattern[i:i+max_size][::-1])
        if sum(a != b for a, b in zip(first_half, second_half)) == max_fault:
            return i
    return 0

def check_pattern(pattern, max_fault=0):
    mirror_size = 0

    mirror_size += get_mirror_size(pattern, max_fault) * 100
    mirror_size += get_mirror_size(rotate_pattern(pattern), max_fault)

    return mirror_size

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        patterns = [pattern.split('\n') for pattern in file.read().split('\n\n')]

        total_mirrorness = sum(check_pattern(pattern) for pattern in patterns)
        
        print("Part 1:", total_mirrorness)

    # part two 
    with open(FILE) as file:
        patterns = [pattern.split('\n') for pattern in file.read().split('\n\n')]

        total_mirrorness = sum(check_pattern(pattern, max_fault=1) for pattern in patterns)
        
        print("Part 2:", total_mirrorness)
