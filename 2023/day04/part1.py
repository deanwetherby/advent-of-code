import math
import re

with open("input.txt", "r") as f:
    data = f.read().splitlines()

WINNING_NUMBER_INDEX = 10
scratch_pile_score = 0
for i, card in enumerate(data):
    numbers = re.findall(r"\d+(?!\d*:)", card)
    winning_numbers = numbers[:WINNING_NUMBER_INDEX]
    other_numbers = numbers[WINNING_NUMBER_INDEX:]
    num_winners = sum(num in other_numbers for num in winning_numbers)
    scratch_pile_score += math.pow(2, num_winners-1) if num_winners > 0 else 0

print(scratch_pile_score)