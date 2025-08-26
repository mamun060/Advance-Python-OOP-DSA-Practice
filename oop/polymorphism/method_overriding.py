# Polymorphism using method overriding
# Method overriding is a feature that allows a subclass to provide a specific 
# implementation of a method that is already defined in its superclass.
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.sound()