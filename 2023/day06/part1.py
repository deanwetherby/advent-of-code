with open("input.txt", "r") as f:
    data = f.read().splitlines()

times = map(int, data[0].split()[1:])
distances = map(int, data[1].split()[1:])

prod = 1
for t, d in zip(times, distances):
    ct = 0
    for i in range(t):
        dist = (t - i) * i
        if dist > d:
            ct += 1
    prod *= ct

print(prod)
