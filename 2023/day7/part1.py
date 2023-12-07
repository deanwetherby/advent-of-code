from collections import Counter


with open("input.txt", "r") as f:
    data = f.read().splitlines()
d = dict(h.split() for h in data)

tr = str.maketrans("TJQKA", "ABCDE")

def sort_key(hand):
    """ Sorts by rank (five of a kind down to high card)
    and then by card value by position with the character translation
    """
    return sorted(Counter(hand).values(), reverse=True), hand.translate(tr)

sorted_keys = sorted(d, key=sort_key)
winnings = sum(i * int(d[key]) for i, key in enumerate(sorted_keys, 1))
print(winnings)
