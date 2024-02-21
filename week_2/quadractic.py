# program to solve quadratic equations
#date: 20/2/2024
#name: sandra

a =float(input("Enter the co efficient of first term :"))
b =float(input("Enter the co efficient of second term :"))
c =float(input (" Enter the constant"))
d = (b**2)- 4 * a * c
x_1 = (-b + math.sqrt (d) )/ 2 * a
x_2 = (-b - math.sqrt (d) )/ 2 * a
print (" The equation of the soluton is :" , x_1 )
print (" The equation of the soluton is :" , x_2 )