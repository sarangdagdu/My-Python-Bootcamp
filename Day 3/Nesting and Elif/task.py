print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter your age\n"))

    if age < 12:
        bill = 5
        print ("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth Tickets are $7")
    else:
        bill = 12
        print("Adult Tickets are $12")

    get_photo = (input("Do ypu want a photo? y / n \n"))
    if get_photo == "y":
        bill += 3

    print(f"Your total bill is {bill} ")
else:
    print("Sorry you have to grow taller before you can ride.")
