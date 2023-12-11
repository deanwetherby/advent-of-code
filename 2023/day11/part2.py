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
    min_x, max_x = min(ga[0], gb[0]), max(ga[0], gb[0])
    min_y, max_y = min(ga[1], gb[1]), max(ga[1], gb[1])
    d = max_x - min_x + max_y - min_y
    d += sum([1_000_000 - 1  for c in expansion["cols"] if min_x < c < max_x])
    d += sum([1_000_000 - 1 for r in expansion["rows"] if min_y < r < max_y])
    total_distances += d

print(total_distances)
