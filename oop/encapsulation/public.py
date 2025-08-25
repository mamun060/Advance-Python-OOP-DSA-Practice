class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

student1 = Student("Alice", 20)
student1.display()
print(student1.name)
print(student1.age)  # Accessing public attribute