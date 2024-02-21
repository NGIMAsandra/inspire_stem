#this is a program to get the surface area of a cylinder
#date: 20/2/2024
#name :sandra

radius =float(input ("Enter the radius of the cylinder:"))
height = float(input ("Enter the height of the cylinder:"))
pi = float (3.142)
diameter = float(radius*2)

surface_area = float((2 * pi *radius**2) + (diameter * pi * height))
print (" The surface area of the cylinder is:" ,surface_area)