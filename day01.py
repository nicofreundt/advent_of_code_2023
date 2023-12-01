import re

FILE = "input.txt"

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        document = file.readlines()
        calibration_values = [int((matches:=re.findall('\d', line))[0] + matches[-1]) for line in document]
        print(sum(calibration_values))
    
    # part two
    with open(FILE) as file:
        digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        digits_ext = digits + [f"{i}" for i in range(1, 10)]
        document = [[i if f"{i}".isnumeric() else f"{digits.index(i) + 1}" for i in re.findall(f"(?=({'|'.join(digits_ext)}))", line)] for line in file.readlines()]
        calibration_values = [int(line[0] + line[-1]) for line in document]
        print(sum(calibration_values))
