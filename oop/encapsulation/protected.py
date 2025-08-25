class Student:
    def __init__(self, name, age):
        self._name = name #protected attribute
        self._age = age # protected attribute 
    
    def display(self):
        print(f"Name: {self._name}, Age: {self._age}") 

student1 = Student("Alice", 20)
student1.display()

#Now check the protected attributes
print(student1._name)
print(student1._age)

# Accessing protected attributes, but convention holo na kora
# Protected attributes should not be accessed directly outside the class
# Protected attributes gula only sub class or base class a use kora uchit
