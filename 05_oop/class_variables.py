#class variables = variables shared by all instances of a class
#defined outside the constructor
#allow you to share data among all the objects created from the class

class Student:

    class_year="2023"          #this is called a class variable
    num_students=0

    def __init__(self,name,age):
        self.name=name               #these are called instance variables
        self.age=age
        Student.num_students+=1          #since num_students is defined as class variable we should use the class name

student1=Student("John",20)
student2=Student("Jane",21)
student3=Student("Bob",22)
student4=Student("Alice",23)

print(student1.name,student1.age)
print(student2.name,student2.age)
print(Student.class_year)
print(Student.num_students)


print(f"My Graduating Class Of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)