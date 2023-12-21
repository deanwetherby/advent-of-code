
# the example from part1 is the infinite grid pattern
with open("example.txt") as f:
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

