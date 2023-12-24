with open("input.txt") as f:
    data = f.read().splitlines()

board = {
    complex(i, j): col
    for i, row in enumerate(data)
    for j, col in enumerate(row.strip())
}

NORTH = -1
SOUTH = 1
WEST = -1j
EAST = 1j

pipes = {
    "S": (NORTH, EAST, SOUTH, WEST),
    "F": (SOUTH, EAST),
    "L": (NORTH, EAST),
    "7": (SOUTH, WEST),
    "J": (NORTH, WEST),
    "|": (NORTH, SOUTH),
    "-": (EAST, WEST),
    ".": (),
}

# find the start position
start = list(board.keys())[list(board.values()).index("S")]
path = {start}

neighbors = {n: {n+d for d in pipes[c]} for n, c in board.items()}

# follow the closed path until we reach the beginning
q: set = neighbors[start]
while q:
    node = q.pop()
    # add this node to the path
    path |= {node}
    # add neighbors to the queue that aren't in the path
    q |= (neighbors[node] - path)
    # queue will eventually become empty
    if not q:
        print("finished loop")

total = 0
for p in set(board) - path:
    count = 0
    for i in range(int(p.imag)):
        m = p.real + i * 1j
        if m in path and board[m] in "|JLS":
            count += 1
    total += count % 2

print(total)        
