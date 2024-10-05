# In single inheritence only one parent and child class

class Organization:
    def __init__(self, oname, olocation):
        self.oname = oname
        self.olocation = olocation

    def organization(self):
        return f"{self.oname} - {self.olocation}"

# child class
class Employee(Organization):
    def __init__(self, ename, ephone, salary, oname, olocation):
        super().__init__(oname, olocation)
        self.ename = ename
        self.ephone = ephone
        self.salary = salary
    
    def display(self):
        return f"{self.ename} - {self.ephone} - {self.salary} - "


#User input class property values
# Get user input for employee details
ename = input("Enter employee name: ")
ephone = input("Enter employee phone: ")
salary = input("Enter employee salary: ")
oname = input("Enter organization name: ")
olocation = input("Enter organization location: ")

# Create object for Employee class
classInfo = Employee(ename, ephone, salary, oname, olocation)
print(classInfo.display() , classInfo.organization() )
