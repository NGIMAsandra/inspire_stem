#proram to show employee record
# date : 21/2/2024
#name : Sandra

employee_name = input("Enter your name :")
age = input("Enter your age:")
salary =int(input("Enter your salary :"))
bonus =int(input("Enter your bonus :"))

print("Name:",employee_name)
print("age:",age)
print("salary:",salary)
print("bonus",bonus)

new_salary =salary + (salary *30/100 )
new_bonus = bonus - 5000

print("Your name is ",employee_name)
print("age",age)
print("Your new salary is:",new_salary)
print("Your new bonus is:" ,new_bonus)