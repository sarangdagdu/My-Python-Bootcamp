def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = { "+":add,"-":subtract,"*":multiply,"/":divide}

# print(operations["*"](5,4))

should_continue = False
num_1 = float(input("What's the first number?:\n"))

operation = input("Pick an Operation:\n")
num_2 = float(input("What's the next number?:\n"))

result = operations[operation](num_1,num_2)
print(f"{num_1} {operation} {num_2} = {result}")

print(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n")
should_continue = input()
