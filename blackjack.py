import random

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
length = len(cards)
card1 = cards[random.randint(0, length-1)]
card2 = cards[random.randint(0, length-1)]
print(f"Your cards: [{card1}, {card2}]")
total = card1 + card2
comp_card = cards[random.randint(0, length-1)]
print(f"Computer's first card: {comp_card}")
another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

