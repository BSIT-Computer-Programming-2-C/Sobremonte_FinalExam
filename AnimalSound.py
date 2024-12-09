from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def makeSound(self):
        pass

class Dog(Animal):
    def makeSound(self):
        return "Woof!"

class Cat(Animal):
    def makeSound(self):
        return "Meow!"

# Demonstrating polymorphism
def animal_sound(animal):
    print(animal.makeSound())

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling makeSound on each
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
