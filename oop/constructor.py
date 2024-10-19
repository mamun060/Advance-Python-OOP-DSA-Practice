#Default constructor 
class University:
    def __init__(self):
        self.university = "Dhaka International University"
    
    def display_university(self):
        print(f"University: {self.university}")

#Parameterized constructor
class Student:
    # defince constructor method
    def __init__(self, name, roll, reg):
        self.name = name
        self.roll = roll 
        self.reg = reg

    def display(self):
        print(f"Student Name: {self.name} - Roll: {self.roll} - Reg: {self.reg}")
    

#create object
university = University()
university.display_university()

student1 = Student("Mamun" , 21 , 115602)
student1.display()
