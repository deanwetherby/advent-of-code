from functools import reduce


def lookup(val: int, mapping: str) -> int:
    _, *ranges = mapping.split("\n")
    for r in ranges:
        dst, src, n = map(int, r.split())
        if src <= val < src + n:
            return val - src + dst
    else:
        return val


seeds, *maps = open("input.txt").read().split("\n\n")

seeds = seeds.split()[1:]
locations = []
for seed in seeds:
    locations.append(reduce(lookup, maps, int(seed)))

print(min(locations))
