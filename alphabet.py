# <!-- Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

# You may assume the letters will be either all uppercase, or all lowercase.

# Some examples of expected behaviour:

# Sample output
# 1st letter: x
# 2nd letter: c
# 3rd letter: p
# The letter in the middle is p
# Sample output
# 1st letter: C
# 2nd letter: B
# 3rd letter: A
# The letter in the middle is B -->
# a= input(" enter the letter: ").lower()
# b = input(" enter the letter: ").lower()
# c = input(" enter the letter: ").lower()

# elif numbere3 > number2 and number2 < numbere1:
#     print( " the middle one is :", number1)
# a = input("Enter the letter: ").lower()
# b = input("Enter the letter: ").lower()
# c = input("Enter the letter: ").lower()

# if a > b:
#     if a < c:
#         print(f"The middle one is {a}")
#     elif b > c:
#         print(f"The middle one is {b}")
#     else:
#         print(f"The middle one is {c}")
# else:
#     if a > c:
#         print(f"The middle one is {a}")
#     elif b < c:
#         print(f"The middle one is {b}")
#     else:
#         print(f"The middle one is {c}")

a= input(" enter the letter: ").lower()
b = input(" enter the letter: ").lower()
c = input(" enter the letter: ").lower()
if a>b and a >c:
    if b>c:
        print("the middle one is ",b)
    else:
        print(" the middle one is ",c)
elif b>c and b>a:
    if a>c:
        print("the middle one is ",a)
    else:
        print(" the middle one is ",c)
elif c>a and c>b:
    if a>b:
        print("the middle one is ",b)
    else:
        print(" the middle one is ",a)
else:
    print(" all the letters are the same")
        

        
    
