class Employee:
    def __init__(self, name, position, salary, department):
        self.name = name
        self.position = position 
        self.salary = salary 
        self.department = department
    

employee1 = Employee("Alice", "Software Engineer", 80000, "Engineering")

print(f"Name: {employee1.name}\nPosition: {employee1.position}\nSalary: ${employee1.salary}\nDepartment: {employee1.department}")