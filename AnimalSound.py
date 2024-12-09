from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def makeSound(self):
        pass

class Dog(Animal):
    def makeSound(self):
        "Implement the makeSound method for Dog."
        return "Woof!"

class Cat(Animal):
    def makeSound(self):
        "Implement the makeSound method for Cat."
        return "Meow!"

# Demonstrating polymorphism
def animal_sound(animal):
    "Takes an Animal object and print its sound."
    print(animal.makeSound())

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling makeSound on each
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
