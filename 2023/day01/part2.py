from enum import Enum


class Digit(Enum):
    zero = "z0o"
    one = "o1e"
    two = "t2o"
    three = "t3e"
    four = "f4r"
    five = "f5e"
    six = "s6x"
    seven = "s7n"
    eight = "e8t"
    nine = "n9e"


with open("input.txt") as f:
    lines = f.read().splitlines()

sum = 0
for line in lines:
    # in line, replace string numbers with the number and then continue
    for digit in Digit:
        line = line.replace(digit.name, digit.value)

    num = [c for c in line if c.isdigit()]
    two_digit = int(num[0] + num[-1])
    sum += two_digit

print(sum)
