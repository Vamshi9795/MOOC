# <!-- Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2).

# Sample output
# Upper limit: 27
# Base: 3
# 1
# 3
# 9
# 27
# Sample output
# Upper limit: 1234567
# Base: 10
# 1
# 10
# 100
# 1000
# 10000
# 100000
# 1000000 -->
try:
    upper = int(input(" Enter the upper limit: "))
    base = int(input(" Eenter the base: "))
    number = 1
    while number <= upper:
        print(number)
        number *=base 
        
    
    

except ValueError:
    print(" Enter a valid input")