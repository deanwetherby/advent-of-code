
with open("input.txt", "r") as f:
    data = f.read().splitlines()


def prev_in_sequence(sequence: list[int]) -> list[int]:
    if all(elem == 0 for elem in sequence):
        return [0] + sequence
    diff_seq = list(map(lambda x, y: y-x, sequence[:-1], sequence[1:]))
    return [sequence[0] - prev_in_sequence(diff_seq)[0]] + sequence

ct = 0
for d in data:
    di = list(map(int, d.split()))
    ct += prev_in_sequence(di)[0]

print(ct)
