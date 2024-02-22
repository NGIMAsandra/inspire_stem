#this is a program to calculate the  hirepurchase
# date : 21/2/2024
#name : Sandra

import math

#find the hire purchase

cash_p = float(input("Enter the cash price:"))
dep = float(input("Enter the deposit:"))
months = float(input("Enter the number the number of months:"))
inst =float(input("Enter the instalments :")) 

h_p = dep +( months * inst )

print("The hire purchase is :",h_p)