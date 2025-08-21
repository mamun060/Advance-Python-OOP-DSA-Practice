class Student:
    def __init__(self, name, roll, reg):
        self.name = name
        self.roll = roll
        self.reg = reg

    def display(self):
        print(f"name: {self.name} \n roll: {self.roll} \n reg: {self.reg}")



student1 = Student("John Doe", 123, "REG001")
student2 = Student("Jane Smith", 456, "REG002")
student3 = Student("Alice Johnson", 789, "REG003")

student1.display()
student2.display()
student3.display()