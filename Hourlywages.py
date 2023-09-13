# <!-- Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

# Sample output
# Hourly wage: 8.5
# Hours worked: 3
# Day of the week: Monday
# Daily wages: 25.5 euros
# Sample output
# Hourly wage: 12.5
# Hours worked: 10
# Day of the week: Sunday
# Daily wages: 250.0 euros -->
list = [ "monday", "tuesday" , "wednesday", "thursday", "friday", "saturday", "sunday"]
a = float(input(" Please enter the houlry wage : "))
b = float(input(" Please enter the number of hours worked : "))
c = input(" please enter day of the week : ")
if list[0:5]:
    print(f" The daily wage is { a * b} ")
if list[6]:
    print(f" The daily wage is { (2*a) * b} ")
    
    

