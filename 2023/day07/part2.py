from collections import Counter


with open("input.txt", "r") as f:
    data = f.read().splitlines()
d = dict(h.split() for h in data)

#"J" is now the worst card for comparisons
tr = str.maketrans("TJQKA", "A0CDE")

def sort_key(hand):
    """ Sorts by rank (five of a kind down to high card)
    and then by card value by position with the character translation
    """
    # need to find the best cards to match the wildcard with
    c = Counter(hand.replace("J", ""))
    try:
        best_card = max(c, key=c.get)
    except ValueError:
        print(hand) # JJJJJ
        best_card = "0"

    wildcard_hand = hand.replace("J", best_card)
    return sorted(Counter(wildcard_hand).values(), reverse=True), hand.translate(tr)


sorted_keys = sorted(d, key=sort_key)
winnings = sum(i * int(d[key]) for i, key in enumerate(sorted_keys, 1))
print(winnings)
