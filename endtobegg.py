# Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

# An example of expected behaviour:

# Sample output
# Please type in a string: hiya
# a
# y
# i
# h

# Ask the user for input
user_input = input("Please type in a string: ")

# Initialize an index variable to the last character in the string
index = len(user_input) - 1

# Print each character from the end to the beginning using a while loop
while index >= 0:
    print(user_input[index])
    index -= 1
