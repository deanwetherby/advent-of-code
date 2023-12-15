from functools import reduce

print(sum(reduce(lambda v, c: ((v + ord(c)) * 17) % 256, step, 0) for step in open("input.txt").read().split(",")))
