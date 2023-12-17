from queue import PriorityQueue

with open("input.txt") as f:
    data = f.read().splitlines()

board = {
    complex(i, j): int(col)
    for j, row in enumerate(data)
    for i, col in enumerate(row.strip())
}


def a_star(board: dict[complex, int], start: complex, goal: complex) -> int:
    open = PriorityQueue()
    open.put((0, 0, start, complex(1, 0)))
    open.put((0, 1, start, complex(0, 1)))

    nodes_visited = 2
    closed = set()
    while not open.empty():
        val, _, cur, dir = open.get()

        if cur == goal:
            return val
        if (cur, dir) in closed:
            continue
        closed.add((cur, dir))

        for d in 1j / dir, -1j / dir:
            for i in range(4, 11):
                new_pos = cur + d * i
                if board.get(new_pos) is not None:
                    v = sum(board[cur + d * (j + 1)] for j in range(i))
                    nodes_visited += 1
                    open.put(
                        (val + v, nodes_visited, new_pos, d)
                    )

print(a_star(board, [*board][0], [*board][-1]))
