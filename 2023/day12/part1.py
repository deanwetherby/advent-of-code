import functools
import re


@functools.cache
def arrangement(condition: str, *regexes: re.Pattern) -> int:
  if not regexes:
    return "#" not in condition

  matches = 0
  idx = 0
  first, rest = regexes[0], regexes[1:]
  while (match := first.search(condition[idx:])) and "#" not in condition[:idx + match.start()]:
    matches += arrangement(condition[idx + match.end() - 1:], *rest)
    idx += match.start() + 1

  return matches


with open("input.txt", "r") as f:
    data = f.read().splitlines()

total = 0
for line in data:
    condition, groupings = line.split()
    groups = list(map(int, groupings.split(",")))
    regexes = [re.compile(f"[.?][#?]{{{int(g)}}}[.?]") for g in groups]
    total += arrangement(f".{condition}.", *regexes)

print(total)
