#class method=allow operatrions relateed to the class itself
#             take (cls) as the first argument,which reprsents the class itself
#instance methods=allow operations related to the instance of the class
#static methods=allow operations related to the class itself
#class methods=best for class-level data or require access to the class itself

class Student:

    count=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1

    #INSTANCE METHOD
    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"
    
    #CLASS METHOD
    @classmethod
    def get_count(cls):
        return cls.count

student1=Student("John",3.5)
student2=Student("Jane",4.0)

print(student1.get_info())
print(student2.get_info())
print(Student.get_count())