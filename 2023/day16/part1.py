from collections import deque

with open("input.txt", "r") as f:
    data = f.read().splitlines()

# so far board problems have been tough using only string manipulation
board = {
    complex(i, j): col
    for j, row in enumerate(data)
    for i, col in enumerate(row.strip())
}

# "The beam enters in the top-left corner from the left and heading to the right"
# 1, -1, j, -j = right, left, down, up
initial = (complex(-1, 0), complex(1, 0))  # position, unit velocity
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
            # beams.append((pos, vel))
            beams.append((pos, -vel))
            # break
        elif cell == "-":
            vel = -1
            # beams.append((pos, vel))
            beams.append((pos, -vel))
            # break
        elif cell == "/":
            vel = -complex(vel.imag, vel.real)
        elif cell == "\\":
            vel = complex(vel.imag, vel.real)
        elif cell is None:
            break

print(len(set(x for x, _ in energized)) - 1)
