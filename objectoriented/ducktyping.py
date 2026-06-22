#"Duck typing" = Another way to achieve polymorphism bsedides inheritance
#                objects bmust have the minimum attributes and methods
#                "if it looks ilike a duck,quack like a duck,it must be a duck"

class Animal:
    alive=True

class Dog(Animal):
    def speak(self):
        print("woof woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class Car:
    alive=False
    def speak(self):
        print("beep beep")

animals = [Dog(), Cat(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)
    