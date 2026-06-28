#multiple inheritance=inheritance from more than one parent class C(A,B)

#multilevel inheritance=inherit from  a parent which inherits from another parent
                          # C(B)<-B(A)<-A
class Animal:
    def __init__(self,name):
        self.name=name
        

    def eat(self):
        print(f"The {self.name} is eating")

    def sleep(self):
        print(f"The {self.name} is sleeping")
class Prey(Animal):
    def flee(self):
        print(f"The {self.name} flees")
                                  #parents
class Predator(Animal):
    def hunt(self):
        print(f"The {self.name} hunts")

class Rabbit(Prey):
    pass

class  Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

hawk=Hawk("Tweety")
fish=Fish("Nemo")
rabbit=Rabbit("Bunny")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
rabbit.eat()
rabbit.sleep()