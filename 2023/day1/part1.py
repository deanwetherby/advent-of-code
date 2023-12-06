
with open("input.txt") as f:
    lines = f.read().splitlines()

sum = 0
for line in lines:
    num = [c for c in line if c.isdigit()]
    two_digit = int(num[0] + num[-1])
    sum += two_digit

print(sum)
