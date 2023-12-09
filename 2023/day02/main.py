with open("input.txt", "r") as f:
    data = f.read().splitlines()

d = {}
for line in data:
    game_no, game_data = line.split(":")
    game_idx = int(game_no[5:])
    game_set = game_data.split(";")
    d[game_idx] = []
    for gs in game_set:
        color_counts = gs.split(",")
        gsd = {}
        for color_count in color_counts:
            count, color = color_count.strip().split(" ")
            gsd[color] = int(count)
        d[game_idx].append(gsd)


TARGET_RED = 12
TARGET_GREEN = 13
TARGET_BLUE = 14

id_ct = 0
prd_ct = 0
for i, v in d.items():
    results = []

    for st in v:
        if (
            st.get("green", 0) <= TARGET_GREEN
            and st.get("red", 0) <= TARGET_RED
            and st.get("blue", 0) <= TARGET_BLUE
        ):
            results.append(True)
        else:
            results.append(False)

    if all(results):
        id_ct += i

    max_red = max(s.get("red", 0) for s in v)
    max_green = max(s.get("green", 0) for s in v)
    max_blue = max(s.get("blue", 0) for s in v)

    prd_ct += max_red * max_green * max_blue

print(id_ct)
print(prd_ct)
