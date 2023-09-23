# Please write a program which asks the user for a year, and prints out the next leap year.

# Sample output
# Year: 2023
# The next leap year after 2023 is 2024
# If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

# Sample output
# Year: 2024
# The next leap year after 2024 is 2028
a = int(input(" Enter the year : "))
print(a)
count = 0
if (a%4 == 0 and a%100 != 0) or (a%400 == 0):
    print(f" The entered year is a leap year the next leap year is {a+4}")
else:
    nextyear =  4 - (a % 4)
    next_leap_year = a + nextyear
    print(f" the entered year is not a leap year \n The next leap year after {a} is {next_leap_year}")