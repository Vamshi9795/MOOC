# lease write a program which prints out all the even numbers between two and thirty, using a loop. Print each number on a separate line.

# The beginning of your output should look like this:
try:
    number = int(input(" Enter the numbers : "))
    while 30 < number > 20:
        if number % 2:
            print(" even")
            break
except ValueError:
    print(" Enter the valid numberic integer input")