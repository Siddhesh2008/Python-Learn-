#Inheritance=Allows a class to inherit attributes and methods from another class
#helps with copde reusability and extensibility
#class Child(parent)

class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("RUFF! RUFF!")
   
class Cat(Animal):
    def speak(self):
        print("MEOW! MEOW!")
class Mouse(Animal):
    def speak(self):
        print("Squeak! Squeak!")

dog=Dog("Fido")
cat=Cat("Whiskers")  
mouse=Mouse("Mickey")

print(cat.name)
cat.eat()
cat.sleep()
cat.speak()