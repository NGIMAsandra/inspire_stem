#program for if function
#date :26/2/2024
#name : sandra 
age = 17
if age > 18:
    print ("You are allowed to drive")

salary = 45000
if salary > 30000 and salary < 50000:
    salary = salary * 0.1 + salary
    print (salary)

    county = "nyeri"
if county == "nyeri" or county == "kisii":
     print (" You get a bursary")

grade =70
if grade >= 84 and grade <= 90 :
    print ("You win a calculator")
elif  grade >= 50 and grade <= 83:
    print("you win a mathematical set ")
else :
    print("You get nothing")