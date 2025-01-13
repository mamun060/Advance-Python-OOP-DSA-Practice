# Inheritance means inherite from successor 
class Employee:
    def __init__(self, employeeID, name, address, phone):
        self.id = employeeID
        self.name = name
        self.address = address
        self.phone =  phone

    def display(self):
        print(self.name) 

employeeOne = Employee(1001, "Mamun", "cumilla", "+8801953103206")
employeeOne.display()