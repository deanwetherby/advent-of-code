
def find_mirror(pattern):
    for i in range(len(pattern) - 1):
        if all(pattern[i-j] == pattern[i + j + 1]
               for j in range(min(i+1, len(pattern) - i - 1))):
            return 100 * (i + 1)

    rotated_data = [''.join(p) for p in [*zip(*pattern)]]
    for i in range(len(rotated_data) - 1):
        if all(rotated_data[i-j] == rotated_data[i + j + 1]
               for j in range(min(i+1, len(rotated_data) - i - 1))):
            return (i + 1)


with open("input.txt", "r") as f:
    data = f.read()

patterns = [pattern.split() for pattern in data.split("\n\n")]
print(sum([find_mirror(pattern) for pattern in patterns]))
