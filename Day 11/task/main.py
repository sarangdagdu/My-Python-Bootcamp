import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)

play = input("Do you want to play a game of BlackJack? Type 'y' or 'n' :\n")
game_over = False

if play == 'y':
    user_hand = random.sample(cards,2)
    print(f"Your final hand : {user_hand}, final score {sum(user_hand)}")

    dealer_hand = random.sample(cards,1)
    print(f"Computer's first card : {dealer_hand}, final score {sum(dealer_hand)}")

while not game_over:
    choice = input("Type y to get another card, type 'n' to pass:\n")
    if(choice == 'y'):
        user_hand.extend(random.sample(cards,1))
        if sum(user_hand) > 21:
            game_over = True
    else:
        dealer_hand.extend(random.sample(cards, 1))

print(user_hand)
print(dealer_hand)