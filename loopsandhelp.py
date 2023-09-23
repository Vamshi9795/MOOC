# Loops and helper variables

# Let's make the PIN checking example a bit more realistic. This version gives the user only three attempts at typing in a PIN.

# The program uses two helper variables. The variable attempts keeps track of how many times the user has typed in a PIN. The variable success is set to either True or False based on whether the user is successful in signing in.

# attempts = 0

# while True:
#     code = input("Please type in your PIN: ")
#     attempts += 1

#     if code == "1234":
#         success = True
#         break

#     if attempts == 3:
#         success = False
#         break

#     # this is printed if the code was incorrect AND there have been less than three attempts
#     print("Incorrect...try again")

# if success:
#     print("Correct PIN entered!")
# else:
#     print("Too many attempts...")
# Sample output
# Please type in your PIN: 0000
# Incorrect...try again
# Please type in your PIN: 1234
# Correct PIN entered!
# Sample output
# Please type in your PIN: 0000
# Incorrect...try again
# Please type in your PIN: 9999
# Incorrect...try again
# Please type in your PIN: 4321
# Too many attempts..