#@property=decorator used to define a method as a property(can be accessed like an attribute)
#Benefit:Add additinal logic when read,write or delete attributes
#gives you getter , setter , and deleter methods
#helps with data validation
#helps with extensibility

class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height

    @property
    def width(self):
        return self._width      #._width is a private attribute,it is not accessible from outside

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self,new_width):
       if new_width>0:
        self._width=new_width
       else:
        print("width must be positive")

    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._height=new_height
        else:
            print("height must be positive")

    @width.deleter
    def width(self):
        del self._width
        print("width deleted")      #del keyword is used to delete attributes

    @height.deleter
    def height(self):
        del self._height
        print("height deleted")

        
    
rectangle=Rectangle(10,5)
rectangle.width=20
rectangle.height=10
print(rectangle.width)
print(rectangle.height)