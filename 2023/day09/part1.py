
with open("input.txt", "r") as f:
    data = f.read().splitlines()


def next_in_sequence(sequence: list[int]) -> list[int]:
    if all(elem == 0 for elem in sequence):
        return sequence + [0]
    diff_seq = list(map(lambda x, y: y-x, sequence[:-1], sequence[1:]))
    return sequence + [sequence[-1] + next_in_sequence(diff_seq)[-1]]

ct = 0
for d in data:
    di = list(map(int, d.split()))
    ct += next_in_sequence(di)[-1]

print(ct)
