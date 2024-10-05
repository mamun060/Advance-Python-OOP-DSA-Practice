# class are blueprint of creating objects
# __init__(): the initialize constructor
# __str__(): the string representator 

class Raju:
    # having an empty class definition like this, would raise an error without the pass statement
    pass

class Student:
    def __init__(self, roll, reg, name, city):
        self.roll = roll
        self.reg = reg
        self.name = name
        self.city = city
    
    # f-string called to formatted string literals
    def info(self):
        print(f"Hello I am {self.name}")

    def __str__(self):
        return f"Name: {self.name} - Roll: {self.roll} - Reg: {self.reg} - City: {self.city}"

#create object for access class property from MyClass class
obj = Student(21,115602,"Md AL Mamun" , "Cumilla")
obj2 = Student(22,115603,"Mst Aysha Akter" , "Dhaka")


print(obj)
print(obj2)


