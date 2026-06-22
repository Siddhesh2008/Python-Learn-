#Polymorphism = Allows different objects to have the same method name, but different behaviors
#two ways to implement polymorphism
#1.inheritance
#2.Duck typing

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*pow(self.radius,2)

class Square(Shape):
    def __init__(self,width):
        self.width=width
    def area(self):
        return pow(self.width,2)

class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def area(self):
        return (self.side1+self.side2+self.side3)/2
    
class Pizza(Circle):
        def __init__(self,toppings,radius):
            super().__init__(radius)
            self.toppings=toppings

shapes=[Circle(4),Square(5),Triangle(5,6,7),Pizza("pepperoni",5)]

for shape in shapes:
    print(shape.area())