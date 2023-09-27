# Please write a program which prints out a line of hash characters, the width of which is chosen by the user.

# Sample output
# Width: 3
# ###
# Sample output
# Width: 8
# ########

a = "#"
try:
    b = int(input(" ENter the width: "))
    print(a*b)
except ValueError:
    print(" Enter a numeric width")