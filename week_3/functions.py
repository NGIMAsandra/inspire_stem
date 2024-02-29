# a block of code running together as a unit

def print_name():
    print("My name is Sandra")

#calling the function
print_name()
print_name()
print_name()


def print_details(name , age , ID , Gender):
    print("I am {0} ,{1} years old. my ID number is {2}. My gender is S{3}".format(name ,age ,ID , Gender))

print_details("Sandra" ,"18", "12345" , "female")
