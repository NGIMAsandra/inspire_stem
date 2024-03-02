#this is a program that uses functions to calculate the suraface area of certain shapes
#date :29/2/2024
#name : SandraNgima
import math
pi = 3.142
shape = ("cube" , "cylinder", "cone" , "sphere")
shape = input("Enter the shape ")
if shape == "sphere" :
    radius =float(input ("Enter the radius of the sphere:"))
    surface_area_of_the_sphere = float (4 * pi* radius**2 ) 
    print( "the surafce area of the sphere is:",surface_area_of_the_sphere)
elif shape == "cube" :
    side = float(input("Enter the measurements of the cube :"))
    surface_area_of_the_cube = float(side *side *6) 
    print("the surface area of the cube is:" ,surface_area_of_the_cube) 
elif shape == "cylinder" :
   radius =float(input ("Enter the radius of the cylinder:"))
   diameter = float(radius * 2)
   height = float(input ("Enter the height of the cylinder:"))
   surface_area_of_cylinder = float((2 * pi *radius**2) + (diameter * pi * height))
   print("the suraface area of the cylinder is:" ,surface_area_of_cylinder )
elif shape == "cone" :
    radius =float(input ("Enter the radius of the cone:"))
    height = float(input ("Enter the height of the cone:")) 
    surface_area_of_cone =  float(pi * radius *(radius + math.sqrt(height**2 + radius **2))) 
    print("the surface area of the cone is:",surface_area_of_cone)
else :
    print ("WRONG SHAPE!")

  