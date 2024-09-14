import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock, paper, scissors]

print("Lets play Rock, Paper, Scissors\n")
user_input = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))

if user_input >= 3 or user_input < 0:
    print("You typed an invalid number. You lose!")
else:
    print(f"You entered {user_input}")
    print(list[user_input])
    computer_choice = random.randint(0, 2)

    print(f"Computer choice is {computer_choice}")
    print(list[computer_choice])

    if user_input == 0 and computer_choice == 2:
        print("You win")
    elif user_input == 0 and computer_choice == 1:
        print("You lose")
    elif user_input == 1 and computer_choice == 0:
        print("You win")
    elif user_input == 1 and computer_choice == 2:
        print("You lose")
    elif user_input == 2 and computer_choice == 1:
        print("You win")
    elif user_input == 2 and computer_choice == 0:
        print("You lose")
    else:
        print("It is a tie")

