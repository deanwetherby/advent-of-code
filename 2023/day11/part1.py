import itertools
import re

with open("input.txt", "r") as f:
    data = f.read().splitlines()

expansion = {"rows": [], "cols": []}
universe = []
for row, line in enumerate(data):
    galaxies = re.finditer(r"#", line)
    galaxies = [galaxy.span() for galaxy in galaxies]
    if not galaxies:
        expansion["rows"].append(row)
    for galaxy in galaxies:
        universe.append((galaxy[0], row))

rotated_data = ["".join(i)[::-1] for i in zip(*data)]
for col, line in enumerate(rotated_data):
    galaxies = re.finditer(r"#", line)
    galaxies = [galaxy.span() for galaxy in galaxies]
    if not galaxies:
        expansion["cols"].append(col)

total_distances = 0
for ga, gb in itertools.combinations(universe, 2):
    d = abs(ga[0] - gb[0]) + abs(ga[1] - gb[1])
    for c in expansion["cols"]:
        if min([ga[0], gb[0]]) < c < max([ga[0], gb[0]]):
            d += 1
    for r in expansion["rows"]:
        if min([ga[1], gb[1]]) < r < max([ga[1], gb[1]]):
            d += 1
    total_distances += d

print(total_distances)
