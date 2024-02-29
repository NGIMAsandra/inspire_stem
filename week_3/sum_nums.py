def sum_num(x,y):
    return x+y
z = sum_num(10 ,20)
print(z)

def prod_num(x,y):
    return x*y
print(prod_num(5,16))

def print_odd(first_number , last_number):
    for i in range(first_number ,last_number):
        print(i % 2)

print_odd(0,15)