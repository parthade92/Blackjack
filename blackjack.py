import random
import time


print(logo)
# p_count = 1
# c_count = 1
player_total = 0
comp_total = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
length = len(cards)
player = []
comp = []
for i in range(0, 2):
    player.append(cards[random.randint(0, length - 1)])
print(f"Your cards: {player}")
player_total = sum(player)
print(f"Your Total: {player_total}")
if player_total == 21:
    print("Blackjack, You win")
    exit(0)
comp.append(cards[random.randint(0, length - 1)])
comp_total = sum(comp)
print(f"Computer's first card: {comp}")
another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
while another_card == 'y':
    if player_total > 21:
        print(f"Dealer Wins.")
        exit(0)
    else:
        player.append(cards[random.randint(0, length - 1)])
        print(f"Your cards: {player}")
        player_total = sum(player)
        print(f"Your Total: {player_total}")
        if player_total > 22:
            print(f"Dealer Wins.")
            exit(0)
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
while another_card == 'n' and comp_total < 22:
    comp.append(cards[random.randint(0, length - 1)])
    print(comp)
    comp_total = sum(comp)
    print(f"Dealer Total: {comp_total}")
    if player_total < comp_total < 22:
        print("Dealer Wins.")
        exit(0)
    elif comp_total > 22:
        print("You Win")
        exit(0)
    elif comp_total == player_total:
        print("Draw.")
        exit(0)
    elif comp_total == 21:
        print("Dealer Wins.")
        exit(0)
    time.sleep(2)
