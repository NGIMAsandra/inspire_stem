#this is a class  nthat distributes cars 
class car :
 def __init__ (self , model , make , year_of_prod ,colour , horse_power , fuel_capcity) :
    self.model = model
    self.make = make
    self.year_of_prod = year_of_prod
    self.colour =  colour
    self.horse_power = horse_power
    self.fuel_capacity = fuel_capcity
    
 def print_make(self , make):
        print("The car is of {0}that make" , format(self,make))
 def set_make(self,make) :
     self.make = make 
 def get_make(self) :
    return self.make
 
     

My_car = car("impala" , "chevrolet" , "1969" , "2500bc" ,"lilac", "360hp")

friends_car = car("note" , "nissan" , "2014", "654bc" ,"grey", "760hp")