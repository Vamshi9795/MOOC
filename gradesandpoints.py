# The table below outlines the grade boundaries on a certain university course. Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

# points	grade
# < 0	impossible!
# 0-49	fail
# 50-59	1
# 60-69	2
# 70-79	3
# 80-89	4
# 90-100	5
# > 100	impossible!
# Some examples:

# Sample output
# How many points [0-100]: 37
# Grade: fail
# Sample output
# How many points [0-100]: 76
# Grade: 3
# Sample output
# How many points [0-100]: -3
# Grade: impossible!

points = int(input(" please enter the number of points received "))
if points>= 90 and points<= 100:
    print(" you received grade = 5")
elif points>= 80 and points<=89:
    print(" you received a grade = 4 ")
elif points>= 70 and points<=79:
    print(" you received a grade = 3 ")
elif points>= 60 and points<=69:
    print(" you received a grade = 2 ")
elif points>= 50 and points<=59:
    print(" you received a grade = 1 ")
elif points>0 and points<=49:
    print(" you received a grade = fail")
elif points<0 or points>100:
    print(" its impossible to get these points")
else:
    print(" enter value is not intger")
    
print(" Thanks for using the grade calculator ")