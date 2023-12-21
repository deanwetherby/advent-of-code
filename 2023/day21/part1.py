
with open("input.txt") as f:
    data = f.read().splitlines()

board = {
    complex(i, j): col
    for j, row in enumerate(data)
    for i, col in enumerate(row.strip())
}

DOWN = complex(0, 1)
UP = complex(0, -1)
RIGHT = complex(1, 0)
LEFT = complex(-1, 0)

start = list(board.keys())[list(board.values()).index("S")]

new_starts = set()
new_starts.add(start)

for _ in range(64):
    n = set()
    for pos in new_starts:
        for d in [UP, DOWN, LEFT, RIGHT]:
            p = pos + d
            if board.get(p) and board.get(p) != "#":
                n.add(p)
    new_starts = n

print(len(new_starts))
