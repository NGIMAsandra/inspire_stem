#the nth term
a = int(input("Enter the value of a: "))
r = int(input("Enter the value of r: "))
n = int(input("Enter the value of n: "))

t_n = a * r**(n-1)
print( "the nth term is :",t_n)

#the sum of the n terms
a = int(input("Enter the value of a: "))
r = int(input("Enter the value of r: "))
n = int(input("Enter the value of n: "))
 
if(r>1):
  S_n = (a*(r**n))/(r-1)
else:
  S_n = (a*(r**n))/(1-r)
 
print("Sum of n terms: ",S_n)
