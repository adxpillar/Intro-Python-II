"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [i for i in range(1, 6)]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Let's first produce a list with just 0 - 9

# def cube(x):
#     return x**3

y = [i**3 for i in range(10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [string.upper() for string in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

# the input function's output always comes through as strings 
x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
# Since the values from x are strings, we need to cast them to integers 
# so that we can check if the number is even or odd 
y = [i for i in x if int(i) % 2 == 0]

print(y)