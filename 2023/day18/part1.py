
with open("input.txt") as f:
    data = f.read().splitlines()

dig_path = []
for line in data:
    dig_path.append(line.split(" "))

movement = {
    "R": complex(1, 0),
    "L": complex(-1, 0),
    "U": complex(0, -1),
    "D" : complex(0, 1)
}

def build_board(path: list[list[str]]) -> tuple[dict, int, int]:
    pos = complex(0, 0)
    board = {pos: "#"}
    for move in path:
        dir = move[0]
        amount = move[1]
        for _ in range(int(amount)):
            pos = pos + movement.get(dir)
            board[pos] = "#"
    max_y = int(max((y.imag for y in board.keys())) + 1)
    max_x = int(max((x.real for x in board.keys())) + 1)
    for x in range(max_x):
        for y in range(max_y):
            p = complex(x, y)
            if board.get(p) is None:
                board[p] = "."
    return board, max_x, max_y


def display_board(board, max_x, max_y):
    cur = complex(0, 0)
    for _ in range(max_y):
        for x in range(max_x):
            print(board.get(cur + x), end="")
        print()
        cur = cur + 1j
    print()

# DEBUG
# board, x, y = build_board(dig_path)
# print(display_board(board, x, y))

# we really just want the vertices of the polygon along the dig path
# not the entire complex board
vertices = [complex(0,0)]
boundary = 0
for p in dig_path:
    mv = p[0]
    amount = int(p[1])
    boundary += amount
    vertices.append(vertices[-1] + (amount * movement.get(mv)))


def picks(area: int, boundary: int) -> int:
    return area - boundary // 2 + 1


def shoelace(vertices: list[complex]) -> int:
    """Shoelace formula
    Args:
        vertices: list of closed loop vertices
    Returns:
        area: integer
    """
    sum1, sum2 = 0, 0
    for i in range(len(vertices) - 1):
        sum1 = sum1 + vertices[i].real * vertices[i+1].imag
        sum2 = sum2 + vertices[i].imag * vertices[i+1].real
    return abs(sum1 - sum2) / 2


area = shoelace(vertices)
interior = picks(area, boundary)
print(boundary + interior)
