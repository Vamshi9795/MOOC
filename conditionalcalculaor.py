# Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.

# Some examples of expected behaviour:

# Sample output
# Number 1: 10
# Number 2: 17
# Operation: add

# 10 + 17 = 27
# Sample output
# Number 1: 4
# Number 2: 6
# Operation: multiply

# 4 * 6 = 24
# Sample output
# Number 1: 4
# Number 2: 6
# Operation: subtract
# 4 - 6 = -2
a = float(input(" Enter the first number : "))
b = float(input(" Enter the second number : "))
operation = input(" enter the operation you want to use : ")
if operation == "add":
    print(f" the addition of two numbers is : { a + b}")
if operation == "multiply":
    print(f" the multiplication of two numbers is : { a * b}")
if operation == "substract":
    print(f" the substraction of two numbers is : { a - b}")
if operation == "divide":
    print(f" the division of two numbers is : { a // b}")
if operation != "add, multiply, divide, substact":
    print(" ")

