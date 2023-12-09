import re

from itertools import cycle

with open("input.txt", "r") as f:
    data = f.read().splitlines()

steps, _, *nodes = data

d = {}
for node in nodes:
    key, left, right = re.findall(r"([A-Z]+)", node)
    d[key] = (left, right)

START = "AAA"
END = "ZZZ"
ct = 0
key = START
for step in cycle(steps):
    key = d[key][0] if step == "L" else d[key][1]
    ct += 1
    if key == END:
        break

print(ct)
