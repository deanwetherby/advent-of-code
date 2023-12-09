
import re

not_important_chars = "0123456789."

with open("input.txt", "r") as f:
    data = f.read().splitlines()

part_numbers = []
for data_idx, line in enumerate(data):
    new_digits = []

    for num in re.finditer(r"\d+", line):
        pre, post = "", ""
        pre_idx = num.start() - 1 if num.start() > 0 else 0
        post_idx = num.end() + 1

        if data_idx > 0:
            pre = data[data_idx-1][pre_idx:post_idx]

        cur = data[data_idx][pre_idx:post_idx]

        if data_idx < len(data) -1:
            post = data[data_idx+1][pre_idx:post_idx]

        part_check = "".join([pre, cur, post])
        if any(elem not in not_important_chars for elem in part_check):
            part_numbers.append(num.group())

print(sum([int(pn) for pn in part_numbers]))
