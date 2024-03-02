#this is a program that uses functions to calculate the volume of certain shapes
#date :29/2/2024
#name : SandraNgima
pi = 3.142
shape = ("cube" , "cylinder", "cone" , "sphere")
shape = input("Enter the shape ")
if shape == "sphere" :
    radius =float(input ("Enter the radius of the sphere:"))
    volume_of_the_sphere = float (4 / 3 * pi* radius**3 ) 
    print( "the volume of the sphere is:",volume_of_the_sphere)
elif shape == "cube" :
    side = float(input("Enter the measurements of the cube :"))
    volume_of_the_cube = float(side *side *side) 
    print("the volume of the cube is:" ,volume_of_the_cube) 
elif shape == "cylinder" :
   radius =float(input ("Enter the radius of the cylinder:"))
   height = float(input ("Enter the height of the cylinder:"))
   volume_of_cylinder = float(pi * radius * radius * height)
   print("the volume of the cylinder is:" ,volume_of_cylinder )
elif shape == "cone" :
    radius =float(input ("Enter the radius of the cone:"))
    height = float(input ("Enter the height of the cone:")) 
    volume_of_cone =  pi / 3 * height * radius**2
    print("the volume of the cone is:",volume_of_cone)
else :
    print ("WRONG SHAPE!")

  