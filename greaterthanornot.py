# <!-- Please write a program which asks for two integer numbers. The program should then print out whichever is greater. If the numbers are equal, the program should print a different message.

# Some examples of expected behaviour:

# Sample output
# Please type in the first number: 5
# Please type in another number: 3
# The greater number was: 5
# Sample output
# Please type in the first number:: 5
# Please type in another number: 8
# The greater number was: 8
# Sample output
# Please type in the first number: 5
# Please type in another number: 5
# The numbers are equal! -->

a = int(input(" enter the first number :"))
b = int(input(" Enter the second number :"))
#  used to get input for the integers
if a > b:
    print(" the greater number is ", a)
elif a < b:
    print(" the greater number is ", b)
else:
    print(" both numbers are equlal")
    