# Please write a program which asks the user for an integer number. If the number is divisible by three, the program should print out Fizz. If the number is divisible by five, the program should print out Buzz. If the number is divisible by both three and five, the program should print out FizzBuzz.

# Some examples of expected behaviour:

# Sample output
# Number: 9
# Fizz
# Sample output
# Number: 7
# Sample output
# Number: 20
# Buzz
# Sample output
# Number: 45
# FizzBuzz

number = int(input(" enter a number "))
if number%3 == 0 and number%5 == 0:
    print(" fizzbuzz")
elif number%3 == 0:
    print(" fizz")
elif number%5 == 0:
    print("buzz")
else:
    print(" the number is not divisible by both 3 and 5")