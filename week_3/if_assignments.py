#this is a program of the if program
#date :26/2/2024
#name : sandra

employee_name = input("Enter your name :")
age = input("Enter your age:")
salary =int(input("Enter your salary :"))
bonus =int(input("Enter your bonus :"))

print("Name:",employee_name)
print("age:",age)
print("salary:",salary)
print("bonus",bonus)

if salary <= 100000 :
    salary = salary * 0.3 + salary
    print (salary)
elif salary <= 150000 :
    salary = salary * 0.15 + salary 
    print(salary)
else :
    salary = salary * 0.05 + salary
    print(salary) 