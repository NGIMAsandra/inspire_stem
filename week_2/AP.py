#the nth term
a = float(input("Enter the first term"))
d = float(input("Enter the common difference"))
n = float(input("Enter the number of terms"))

n_terms = (a + d * ( n -1))
print("The nth  term of the sequence is :" , n_terms)

#the sum of the numbers
a = int(input("Enter the value of a: "))
d = int(input("Enter the value of d: "))
n = int(input("Enter the value of n: "))
 
S_n = (n/2)*(2*a + (n-1)*d)
print("Sum of first n terms: ", S_n)
