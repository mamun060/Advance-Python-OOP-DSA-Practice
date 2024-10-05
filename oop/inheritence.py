# Inheritance allows us to define a class that inherits all the methods and properties from another class.

class University:
    def __init__(self, uname, ulocation):
        self.uname = uname
        self.ulocation = ulocation
    
    def display(self):
        return f"{self.uname} - {self.ulocation}"
    

#child class
class Student(University):
    def __init__(self, name, roll, depertment , university_name , university_location ):
        super().__init__(university_name, university_location)
        self.name = name
        self.roll = roll
        self.department = depertment
    
    def info(self):
        return f"{self.name} - {self.roll} - {self.department} -"


# create object for student class and student class also access to the university class
obj1 = University("MIST", "Dhaka")
obj = Student("Md AL Mamun", 21, "CSE", "DIU", "Satarkul, Dhaka")

print(obj1.display())
print(obj.info(), obj.display())
