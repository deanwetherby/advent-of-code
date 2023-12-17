from collections import deque

with open("input.txt", "r") as f:
    data = f.read().splitlines()

# so far board problems have been tough using only string manipulation
board = {
    complex(i, j): col
    for j, row in enumerate(data)
    for i, col in enumerate(row.strip())
}


def energize(initial: tuple[complex, complex]) -> int:
    beams = deque([initial])
    energized = set()
    while beams:
        pos, vel = beams.popleft()
        while not (pos, vel) in energized:
            energized.add((pos, vel))
            pos += vel
            cell = board.get(pos)
            if cell == "|":
                vel = 1j
                beams.append((pos, -vel))
            elif cell == "-":
                vel = -1
                beams.append((pos, -vel))
            elif cell == "/":
                vel = -complex(vel.imag, vel.real)
            elif cell == "\\":
                vel = complex(vel.imag, vel.real)
            elif cell is None:
                break
    return len(set(x for x, _ in energized)) - 1


DOWN = complex(0, 1)
UP = complex(0, -1)
RIGHT = complex(1, 0)
LEFT = complex(-1, 0)

width, height = len(data), len(data[0])
# top edge going down
start_beams = [(complex(-1, i), DOWN) for i in range(width)]
# bottom edge going up
start_beams.extend([(complex(height, i), UP) for i in range(width)])

# left edge going right
start_beams.extend([(complex(-1, i), RIGHT) for i in range(height)])
# right edge going left
start_beams.extend([(complex(width, i), LEFT) for i in range(height)])

print(max(map(energize, start_beams)))
