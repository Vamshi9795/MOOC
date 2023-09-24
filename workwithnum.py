# Pre-task

# Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.

# Sample output
# Please type in integer numbers. Type in 0 to finish.
# Number: 5
# Number: 22
# Number: 9
# Number: -2
# Number: 0
# Part 1: Count

# After reading in the numbers the program should print out how many numbers were typed in. The zero at the end should not be included in the count.

# You will need a new variable here to keep track of the numbers typed in.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# Part 2: Sum

# The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation.

# The program should now print out the following:

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34
# Part 3: Mean

# The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation. You may assume the user will always type in at least one valid non-zero number.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34
# The mean of the numbers is 8.5
# Part 4: Positives and negatives

# The program should also print out statistics on how many of the numbers were positive and how many were negative. The zero at the end should not be included in the calculation.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34
# The mean of the numbers is 8.5
# Positive numbers 3
# Negative numbers 1
conut = 0
sumo = 0
mean = 0
while True:
    try:
        a = float(input(" Enter the number :"))
        #  used to take the input
        if a == 0:  
            print(f" the numbers entered is {conut}")  
            break
        if a > 0:
            print(f" The positve numbers are { conut}")
        if a < 0:
            print(f" The negative numbers are { conut}")
        conut = (conut + 1)
        # #  pre tasl
        # #  used to count the numbers entered
        sumo = sumo + a
        #  # task 2
        mean = sumo/conut
        # #  task 3
        
        
        
        
        
        
        
        
        
      
    except ValueError:
        print(" Invalid input \n Input should only be numeric number")
print(f" the sum of numbers is { sumo }")
print(f" the mean of numbers is { mean }")
