class Dog:
    def __init__(self, name):
        self.name = name
    def displayDog(self):
        print(f"Dog's name is {self.name}")

class Labrador(Dog): # single inheritance
    def __init__(self, name, sound, color):
        super().__init__(name)  # Inherit name from Dog
        self.sound = sound
        self.color = color
    def display(self):
        print(f"name is - {self.name}, Labrador's sound is {self.sound} and color is {self.color}")


# Create object

labrador = Labrador("Max", "Bark", "Yellow")
labrador.display()
labrador.displayDog()  # Call method from parent class