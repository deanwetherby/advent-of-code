
with open("input.txt", "r") as f:
    data = f.read().splitlines()

for row, line in enumerate(data):
    s_idx = line.find('S')
    if s_idx > -1:
        start_pos = (s_idx, row)
        break

move_list = []
cur_pos = start_pos
cur = "S"

# find the first move using the 4 connected component approach
cn, cs, ce, cw = [False] * 4
cn = data[cur_pos[1]-1][cur_pos[0]] in "|7F"
cs = data[cur_pos[1]+1][cur_pos[0]] in "|LJ"
cw = data[cur_pos[1]][cur_pos[0]-1] in "-LF"
ce = data[cur_pos[1]][cur_pos[0]+1] in "-7J"
cur_moves = [cn, cs, ce, cw]
possible_moves = list(filter(lambda i: cur_moves[i], range(len(cur_moves))))

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)
pipes = {
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
    "F": [SOUTH, EAST],
    "L": [NORTH, EAST],
    "7": [SOUTH, WEST],
    "J": [NORTH, WEST],
}
pipe_list = [NORTH, SOUTH, EAST, WEST]
first_move = [m for m, b in zip(pipe_list, cur_moves) if b]

for k, v in pipes.items():
    if first_move[0] in v:
        cur = k

prev_move = first_move[0]
complete = False
while not complete:
    possible_moves = pipes.get(cur).copy()
    if prev_move == NORTH:
        SOUTH in possible_moves and possible_moves.remove(SOUTH)
    elif prev_move == SOUTH:
        NORTH in possible_moves and possible_moves.remove(NORTH)
    elif prev_move == EAST:
        WEST in possible_moves and possible_moves.remove(WEST)
    elif prev_move == WEST:
        EAST in possible_moves and possible_moves.remove(EAST)

    move = possible_moves[0]
    cur_pos = (cur_pos[0] + move[0], cur_pos[1] + move[1])
    cur = data[cur_pos[1]][cur_pos[0]]
    prev_move = move
    move_list.append(cur)
    if cur == "S":
        complete = True

print(len(move_list) / 2)
