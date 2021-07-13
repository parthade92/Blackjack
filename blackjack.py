import random as r

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
length = len(cards)
card1 = cards[r.randint(0, length-1)]
card2 = cards[r.randint(0, length-1)]
print(f"Your cards:\n [{card1} , {card2}]")
sum = card1 + card2
