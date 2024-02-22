#strings in python
#date:22/2/2024
#name: Sandra

city = "nairobi"
print(city[0])# n
print(city[1])# a
print(city[2])# i
print(city[3])# r
print(city[4])# o
print(city[5])# b
print(city[6])# i


#convert to upper case

print (city)
print (city.upper())
print("\n")#prints a new line

name = "SANDRA"
print(name)
print(name.lower())#converts to lowercase
print("\n")

town = "     Naivasha"
print(town)
print("\t")#new tab
print(town.strip())

#add two strips
f_name= "Sandra"
s_name= "Ngima"
full_name = f_name + s_name
print (full_name)


#replacing strings
fruit="orange"
print(fruit.replace('o','y'))

subject = "pysical,sciences"
print(subject.split(","))

age = 30
height = 1.2
print("I am {0} years old and {1} meters tall" .format(age , height))