FILE = "input.txt"

def get_differences(nums):
    differences = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    if all(d == 0 for d in differences):
        return [nums[0], *nums, nums[-1]]
    else:
        next_differences = get_differences(differences)
        return [nums[0] - next_differences[0], *nums, nums[-1] + next_differences[-1]]

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        print("Part 1:", sum(get_differences([*map(int, line.split(' '))])[-1] for line in file.readlines()))

    # part two 
    with open(FILE) as file:
        print("Part 2:", sum(get_differences([*map(int, line.split(' '))])[0] for line in file.readlines()))
