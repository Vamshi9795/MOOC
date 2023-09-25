# lease write a program which prints out all the even numbers between two and thirty, using a loop. Print each number on a separate line.

# The beginning of your output should look like this:
try:
    number = 2 
    while number < 30 :
        number+=1
        if number % 2 == 0:
            print(number)
            number+=1
except ValueError:
    print(" Enter the valid numberic integer input")