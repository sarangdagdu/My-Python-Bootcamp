print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You are at the start and you need to choose a either left or right to start\n").lower()
if direction == "left":
    print("Good Choice!\n")
    swim = input("You\'re across a river and there is no boat to take to to the other side. "
                 "Do you want to wait here for someone to arrive or you want to swim across?\n").lower()
    if swim == "wait":
        print("A boat came by and dropped at the doorstep of a creepy gateway.\n")
        door = input("There are 3 doors in front of you. Red, Blue and Yellow. One of these have the treasure."
                     " Make your choice\n").lower()

        if door == "yellow":
            print("You made it! Now Break open the box and enjoy!\n")
        elif door == "red":
            print("A Dragon smoked you alive!\n")
        else:
            print("You were attacked by wolves! Bye Bye\n")

    else:
        print("You served yourself as breakfast to a hungry Shark! Sorry!\n")

else:
    print("Oops! You stepped on a landmine blowing up the island!\n")