
def find_mirror(pattern):
    for i in range(len(pattern)):
        if sum(c != d for l,m in zip(pattern[i-1::-1], pattern[i:])
                for c,d in zip(l, m)) == 1:
              return 100 * i
    rotated_data = [''.join(p) for p in [*zip(*pattern)]]
    for i in range(len(rotated_data)):
        if sum(c != d for l,m in zip(rotated_data[i-1::-1], rotated_data[i:])
                for c,d in zip(l, m)) == 1: 
              return i
    return 0

with open("input.txt", "r") as f:
    data = f.read()

patterns = [pattern.split() for pattern in data.split("\n\n")]
print(sum([find_mirror(pattern) for pattern in patterns]))
