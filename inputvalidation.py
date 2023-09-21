# Please write a program which asks the user for integer numbers.

# If the number is below zero, the program should print out the message "Invalid number".

# If the number is above zero, the program should print out the square root of the number using the Python sqrt function.

# In either case, the program should then ask for another number.

# If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

# Below you'll find a reminder of how the sqrt function is used. Remember to import it in the beginning of the program.

# # sqrt function will not work without this line in the beginning of the program
# from math import sqrt

# print(sqrt(9))
# Sample output
# 3.0
# An example of expected behaviour of your program:

# Sample output
# Please type in a number: 16
# 4.0
# Please type in a number: 4
# 2.0
# Please type in a number: -3
# Invalid number
# Please type in a number: 1
# 1.0
# Please type in a number: 0
# Exiting...
from math import sqrt

while True:
        try:
            a = int(input(" Enter the number: ")) 
            # USed to take the input from the user
            if a < 0:
                print(" Inavild input")
            #  used to check if its less than 0 if it is it will print invalid input but will still be in the loop
            elif a > 0:
                print(f" The square root of the number is {sqrt(a)}")
                #  a > 0 so prints the square root
            else:
                print(" Exiting the loop")
                break  
            # a == 0 then exits the loop
        except ValueError:
            print(" Enter a valid numberic input")