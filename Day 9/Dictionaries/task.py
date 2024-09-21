programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# Accessing a specific key
print(programming_dictionary["Loop"])
# Adding something to a dictionary
programming_dictionary["test"] = "This is a test addition."
print(programming_dictionary)

# Emptying a dictionary
# programming_dictionary = {}
print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])