import random
from typing import final

import string_utils

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_list = random.sample(letters,nr_letters)
number_list = random.sample(numbers,nr_numbers)
symbol_list = random.sample(symbols,nr_symbols)

seq_pass = ''
shuffled_pass = ''

for each_char in letter_list:
    seq_pass = seq_pass + each_char

for each_char in symbol_list:
    seq_pass = seq_pass + each_char

for each_char in number_list:
    seq_pass = seq_pass + each_char

list_sa = list(seq_pass)
random.shuffle(list_sa)

for each_char in list_sa:
    shuffled_pass = shuffled_pass + each_char

print(f"Your sequential password is: {seq_pass}")
print(f"Your shuffled password is: {shuffled_pass}")
