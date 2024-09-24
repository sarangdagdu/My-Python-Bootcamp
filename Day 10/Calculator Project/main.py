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

should_continue = True
num_1 = float(input("What's the first number?:\n"))

while should_continue == True:

    operation = input("Pick an Operation:\n")
    num_2 = float(input("What's the next number?:\n"))

    result = operations[operation](num_1,num_2)
    print(f"{num_1} {operation} {num_2} = {result}")

    continue_prompt = input((f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n"))

    if bool(continue_prompt) == True:
        should_continue = False

        operation = input("Pick an Operation:\n")
        num_2 = float(input("What's the next number?:\n"))

        temp_result = operations[operation](result,num_2)
        print(f"{result} {operation} {num_2} = {temp_result}")
    else:
        print("\n*50")



