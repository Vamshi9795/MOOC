# Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

# An example of expected behaviour:

# Sample output
# Please type in a string: hiya
# a
# y
# i
# h

a = input(" Enter the string")
index = 0
while True:
    print(a[index])
    index += 1