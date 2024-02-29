My_laptop = { "make": "HP","colour" : "grey" , "weight" :"2.4" , "year" : "2020" }
print (My_laptop["make"])
print (My_laptop["colour"])
print (My_laptop["weight"])
print (My_laptop["year"])
#to chnage values
My_laptop["colour"] = "red"
My_laptop["year"] = "2021"
del My_laptop["colour"]


for key,value in My_laptop.items() :
    print (key)
    print("\t")
    print(value)
My_laptop ["size"] = "12000mm x 5000mm"
print(My_laptop)