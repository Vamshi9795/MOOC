# Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.

# Some examples of expected behaviour:

# Sample output
# Person 1:
# Name: Alan
# Age: 26
# Person 2:
# Name: Ada
# Age: 27
# The elder is Ada
# Sample output
# Person 1:
# Name: Bill
# Age: 1
# Person 2:
# Name: Jean
# Age: 1
# Bill and Jean are the same age

person1_age = int(input(" Enter the age of person1 :"))
person1_name = (input(" Enter the name of person1 :"))
person2_age = int(input(" Enter the age of person2 :"))
person2_name = (input(" Enter the name of person2 :"))
#  statemet to input the name and age of the persons
if person2_age > person1_age:
    print(f" { person2_name } is elder than { person1_name} ")
elif person1_age > person2_age:
    print(f" { person1_name } is elder than { person2_name} ")
else:
    print(f" { person1_name} and {person2_name} are of same age")

print(" the programe has ended !")