class Person:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address

    # Getter for name
    def get_name(self):
        """return the name of the user"""
        return self.__name

    # Setter for name
    def set_name(self, name):
         """set the name of the user"""
        self.__name = name

    # Getter for age
    def get_age(self):
         """return the age of the user"""
        return self.__age

    # Setter for age
    def set_age(self, age):
        """set the age of the user"""
        self.__age = age

    # Getter for address
    def get_address(self):
        """return the address of the user"""
        return self.__address

    # Setter for address
    def set_address(self, address):
        """set the address of the user"""
        self.__address = address

# Example usage
person = Person("Kristine", 22, "Camdas, Baguio City")
print(person.get_name())  # Output: Kristine
person.set_age(31)
print(person.get_age())   # Output: 22
print(person.get_address()) #Output: Camdas, Baguio City
