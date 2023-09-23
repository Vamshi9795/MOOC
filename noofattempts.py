# Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. The program should then print out the number of times the user tried different codes.

# Sample output
# PIN: 3245
# Wrong
# PIN: 1234
# Wrong
# PIN: 0000
# Wrong
# PIN: 4321
# Correct! It took you 4 attempts
# If the user gets it right on the first try, the program should print out something a bit different:

# Sample output
# PIN: 4321
# Correct! It only took you one single attempt!

a = int(input(" Enter the pin "))
#  used to take the input from the user
attemps = 0
# since we are counting attempts we made the initial attempts to 0
print(" entered pin in:",a)
# chceking to print the entered input
while True:
    b = int(input(" Repeat the pin"))
    #  used ot take input for the pin to enter again so we can compare

