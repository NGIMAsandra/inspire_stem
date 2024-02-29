My_man = { "make": "tall","colour" : "light" , "weight" :"778" , "year" : "2005" }
print (My_man["make"])
print (My_man["colour"])
print (My_man["weight"])
print (My_man["year"])
#to chnage values
My_man["colour"] = "red"
My_man["year"] = "2021"
del My_man["colour"]


for key,value in My_man.items() :
    print (key)
    print("\t")
    print(value)
My_man ["size"] = "12000mm x 5000mm"
print(My_man)


print(My_man)
my_deskmate = My_man.copy
print(my_deskmate)