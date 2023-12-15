from collections import defaultdict
from functools import reduce

with open("input.txt", "r") as f:
    data = f.read()


def f(step: str):
    return reduce(lambda v, c: ((v + ord(c)) * 17) % 256, step, 0)


boxes = defaultdict(dict)
for step in data.split(","):
    if "=" in step:
        label, i = step.split("=")
        boxes[f(label)][label] = int(i)
    else:
        label = step[:-1]
        boxes[f(label)].pop(label, None)

print(
    sum((i + 1) * (j + 1) * l for i in boxes for j, l in enumerate(boxes[i].values()))
)
