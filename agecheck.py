# Please write a program which asks for the user's age. If the age is not plausible, that is, it is under 5 or something that can't be an actual human age, the program should print out a comment.

# Have a look at the examples of expected behaviour below to figure out which comment is applicable in each case.

# Sample output
# What is your age? 13
# Ok, you're 13 years old
# Sample output
# What is your age? 2
# I suspect you can't write quite yet...
# Sample output
# What is your age? -4
# That must be a mistake

a = int(input(" enter whats your age in years :? "))
if a>=5 and a<=100:
    print(f"OK, you are {a}  years old")
if a<5 and a>0:
    print(" I suspect you cant write yet")
if a>100 or a<0:
    print(" This must be a mistake you shouldn't exist")