class Employee:

    def __init__(self,name,position):
        self.name=name
        self.position=position

    def get_info(self):
        return f"Name: {self.name}, Position: {self.position}"
    
    @staticmethod
    def is_valid_postion(position):
        valid_positions=["manager","developer","tester"]
        return position in valid_positions
employee1=Employee("John","manager")
employee2=Employee("Jane","developer")
employee3=Employee("Bob","tester")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
    
print(Employee.is_valid_postion("manager"))