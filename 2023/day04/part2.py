import re

with open("input.txt", "r") as f:
    data = f.read().splitlines()

card_instances = [0] * len(data)
WINNING_NUMBER_INDEX = 10
for i, card in enumerate(data):
    card_instances[i] += 1
    numbers = re.findall(r"\d+(?!\d*:)", card)
    winning_numbers = numbers[:WINNING_NUMBER_INDEX]
    other_numbers = numbers[WINNING_NUMBER_INDEX:]
    num_winners = sum(num in other_numbers for num in winning_numbers)
    for winner in range(num_winners):
        card_instances[i + winner + 1] += card_instances[i]

print(sum(card_instances))
