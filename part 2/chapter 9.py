#CLASS METHODS

#CLASS ATTRIBUTES

"""
class Animal:
    species = "Mammal"  # Class attribute
    name = "Generic Animal"  # Class attribute


    @classmethod
    def show_info(cls):
        print(f"{cls.name} is a {cls.species}")

p=Animal()

p.name = "Dog"  # Instance attribute
p.species = "Canine"  # Instance attribute


#NOW EVEN AFTER CHANGING THE INSTANCE ATTRIBUTES, TjjHE CLASS METHOD WILL STILL REFER TO THE CLASS ATTRIBUTES BECAUSE IT IS A CLASS METHOD
# This will print the class attributes

p.show_info()

"""

#property Decorator

# it allows us to define methods in a class that can be accessed like attributes
# it is used to manage the access to instance attributes
class Person:
    def __init__(self, name, age):
        self._name = name  # Using a single underscore to indicate a protected attribute
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0: 
            raise ValueError("Age cannot be negative")
        self._age = value

# Example usage
p = Person("Alice", 30)
print(p.name)  # Accessing the name property
p.name = "Bob"  # Setting a new name
print(p.name)  # Accessing the updated name property
print(p.age)  # Accessing the age property
p.age = 35  # Setting a new age
print(p.age)  # Accessing the updated age property

# another example
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Using a single underscore to indicate a protected attribute

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * (self._radius ** 2)
    
# Example usage
c = Circle(5)
print(c.radius)  # Accessing the radius property
c.radius = 10  # Setting a new radius
print(c.radius)  # Accessing the updated radius property
print(c.area)  # Accessing the area property, which is calculated based on the radius
# The area property is read-only, as it does not have a setter method
# This allows us to calculate the area dynamically based on the radius
# print(c.area)  # Uncommenting this line will raise an error because area is read-only
# c.area = 100  # This will raise an AttributeError because area is read-only
# The property decorator allows us to define methods that can be accessed like attributes,
# providing a clean and intuitive interface for managing instance attributes.
# It also allows us to enforce validation rules when setting values, ensuring that the object's state remains valid.
# This is particularly useful for encapsulating the logic related to attribute access and modification, making the code more maintainable and less error-prone.     
# The property decorator is a powerful feature in Python that enhances the way we work with class attributes and methods.
# It allows us to define methods that can be accessed like attributes, providing a clean and intuitive interface for managing instance attributes.
# It also allows us to enforce validation rules when setting values, ensuring that the object's state remains valid.
