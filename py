class Person:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        self.__age = age

    # Getter for address
    def get_address(self):
        return self.__address

    # Setter for address
    def set_address(self, address):
        self.__address = address

# Example usage
person = Person("Kristine", 22, "Camdas, Baguio City")
print(person.get_name())  # Output: Kristine
person.set_age(31)
print(person.get_age())   # Output: 22
print(person.get_address()) #Output: Camdas, Baguio City
