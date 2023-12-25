import ast

#  create a tuple from string user input

my_tuple = tuple(input('Enter space-separated words: ').split())

print(my_tuple)

# -------------------------------

#  create a tuple from integer user input

user_input = input('Enter space-separated integers: ')

my_tuple = tuple(int(item) for item in user_input.split())

print(my_tuple)
