class Student:
    def __init__(self, name, age):
        self.__name = name # private attribute
        self.__age = age # private attribute
    
    def display(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

    def __output(self):
        return f"Name: {self.__name}, Age: {self.__age}"


student1 = Student("Alice", 20)
student1.__output() # not accessible from outsite of class
student1.display() # public method it's accessible from outsite

# now check the accessibility from outsite of the class
# print(student1.__name)  # AttributeError: 'Student' object has no attribute '__name'
# print(student1.__age)   # AttributeError: 'Student' object has no attribute '__age'