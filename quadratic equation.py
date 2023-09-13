# Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. The quadratic formula expressed with the Python sqrt function is as follows:

# x = (-b ± sqrt(b²-4ac))/(2a).

from math import sqrt
a = float(input(" Enter the value of a : "))
b = float(input(" Enter the value of b : "))
c = float(input(" Enter the value of c : "))
x1 = (-b - sqrt(b**2 - 4 * a * c))/2*a
x2 = (-b + sqrt(b**2 - 4 * a * c))/2*a

print(f"the roots are {x1} and {x2} ")