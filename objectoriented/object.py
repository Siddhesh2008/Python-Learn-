#object=A "bundle" related attributes (variables) and methods (function)          
# ex. phone,cup,book
# you need "class" to create many objects

#class= a template for creating objects

class Car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

    def drive(self):
        print(f"vroom vroom {self.color} {self.model}")
    def stop(self):
        print(f"brake {self.color} {self.model}")
    def describe(self):
        print(f"{self.color} {self.model} {self.year}")


car1=Car("BMW",2018,"red",True)
car2=Car("Audi",2019,"blue",False)
car3=Car("Mercedes",2020,"black",True)

print(car1.model,car1.year,car1.color,car1.for_sale)    #"." is used to access attributes
print(car2.model,car2.year,car2.color,car2.for_sale)

car1.stop()
car2.drive()
car3.describe()

                                                                                             