radius =float(input ("Enter the radius of the cylinder:"))
height = float(input ("Enter the height of the cylinder:"))
pie = float (3.142)
Diameter = float(radius*2)

surface_area = float((2 * pie *radius**2) + (Diameter * pie * height))
print (" The surface area of the cylinder is:" ,surface_area)