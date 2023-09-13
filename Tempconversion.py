# Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

# The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.

# Two examples of expected behaviour:

# Sample output
# Please type in a temperature (F): 101
# 101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius

# Please type in a temperature (F): 21
# 21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
# Brr! It's cold in here!

a = float(input(" Please type is a temperature (F): "))
# converting F into Celsius using formula C/100 = (F-32)/180
# now we need Fahrenheit to celsius C = ((F-32)/9)*5
b = ((a-32)/9)*5
print(f" {a} degrees Fahrenheit equals to {b} degree Celsius")
if b <0:
    print(" Brr! It's cold in here!")