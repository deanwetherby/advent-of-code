import re
from itertools import cycle
from math import gcd


with open("input.txt", "r") as f:
    data = f.read().splitlines()

steps, _, *nodes = data

d = {}
for node in nodes:
    key, left, right = re.findall(r"([A-Z]+)", node)
    d[key] = (left, right)

solutions = []
start_keys = [k for k in d if k.endswith("A")]
for key in start_keys:
    ct = 0
    for step in cycle(steps):
        key = d[key][0] if step == "L" else d[key][1]
        ct += 1
        if key.endswith("Z"):
            break
    solutions.append(ct)

lcm = 1
for solution in solutions:
    lcm = lcm*solution//gcd(lcm, solution)

print(lcm)
