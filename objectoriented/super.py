#super=Function used in a child class to call a method from a parent class (superclass)
#         It is used to access the parent class's methods and attributes
#         Aloows you to extend the functionality of the inherited methods
class Shapes:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled

    def describe(self):
        print(f"color:{self.color},filled:{self.filled}")

class Circle(Shapes):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius=radius

    def describe(self):
        print(f"It is a circle with Area:{pow(self.radius,2)*3.14} and radius:{self.radius}")
        super().describe()    #it calls the parent class method

class Square(Shapes):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width=width

    def describe(self):
        print(f"It is a square with Area:{pow(self.width,2)} and width:{self.width}")
        super().describe()
    

class Triangle(Shapes):
    def __init__(self,color,filled,side1,side2,side3):
        super().__init__(color,filled)
        self.side1=side1
        self.side2=side2
        self.side3=side3

    def describe(self):
        print(f"It is a triangle with Area:{(self.side1+self.side2+self.side3)/2} and sides:{self.side1},{self.side2},{self.side3}")
        super().describe()

circle=Circle("red",True,10)
print(circle.color)
print(circle.filled)
print(circle.radius)

Square=Square("red",True,10)
print(Square.color)
print(Square.filled)
print(Square.width)

Triangle=Triangle("red",True,10,10,10)
print(Triangle.color)
print(Triangle.filled)
print(Triangle.side1)
print(Triangle.side2)
print(Triangle.side3)

circle.describe()
Square.describe()           #they use the child method of area function
Triangle.describe()
    