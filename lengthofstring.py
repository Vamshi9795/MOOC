# Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

# Some examples of expected behaviour:

# Sample output
# Please type in string 1: hey
# Please type in string 2: hiya
# hiya is longer
# Sample output
# Please type in string 1: howdy doody
# Please type in string 2: hola
# howdy doody is longer
# Sample output
# Please type in string 1: hey
# Please type in string 2: bye
# The strings are equally long

str1 = input(" Enter the first word: ") # used to take the input
str2 = input(" Enter the second word: ") # used to take the input
while True:
    if len(str1) > len(str2):
        print(f" {str1} is longer cause it has {len(str1)- len(str2)} words more then {str2} ") # used to calulate the length and print the output
        break
    elif len(str1) < len(str2):
        print(f" {str2} is longer cause it has {len(str2)- len(str1) } words more than {str1} ") # used to calulate the length and print the output
