
with open("input.txt", "r") as f:
    data = f.read().splitlines()

rotated_data = [''.join(p) for p in [*zip(*data)]]

total = 0
for col in rotated_data:
    rolled_col = "#".join("".join(sorted(s, reverse=True)) for s in col.split("#"))
    partial = 0
    for i, c in enumerate(rolled_col):
        partial += len(rolled_col) - i if c == "O" else 0
    total += partial

print(total)
