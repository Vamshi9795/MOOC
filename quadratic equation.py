from math import sqrt
a = float(input(" Enter the value of a : "))
b = float(input(" Enter the value of b : "))
c = float(input(" Enter the value of c : "))
x1 = (-b - sqrt(b**2 - 4 * a * c))/2*a
x2 = (-b + sqrt(b**2 - 4 * a * c))/2*a

print(f"the roots are {x1} and {x2} ")