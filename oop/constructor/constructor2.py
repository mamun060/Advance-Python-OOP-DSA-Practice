# Non perameterize constructor
class Employee:
    count = 0
    def __init__(self):
        Employee.count += 1
    def display(self, name):
        print(f"Total Employees: {Employee.count} - {name}")

emp1 = Employee()
emp1.display("John Doe")

emp2 = Employee()
emp2.display("Jane Smith")

emp3 = Employee()
emp3.display("Alice Johnson")
