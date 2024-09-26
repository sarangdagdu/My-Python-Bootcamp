import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)

user_hand = random.sample(cards,2)
print(f"Your final hand : {user_hand}, final score {sum(user_hand)}")

dealer_hand = random.sample(cards,1)
print(f"Computer's first card : {dealer_hand}, final score {sum(dealer_hand)}")

choice = input("Type y to get another card, type 'n' to pass:\n")
