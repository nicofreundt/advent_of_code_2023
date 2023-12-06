import re

FILE = "input.txt"

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        times, distances = [[*map(int, re.findall('\d+', line))] for line in file.readlines()]
        min_times = 1
        for time, distance in zip(times, distances):
            min_time = 0
            while (time - min_time) * min_time <= distance:
                min_time += 1
            min_times *= time + 1 - 2*min_time
        print(min_times)
        

    # part two 
    with open(FILE) as file:
        times, distances = [re.findall('\d+', line) for line in file.readlines()]
        time = int("".join(times))
        distance = int("".join(distances))
        min_time = 0
        while (time - min_time) * min_time <= distance:
            min_time += 1
        print(time + 1 - 2*min_time)
