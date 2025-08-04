#INHERITENC AND OOPS
# Inheritance allows a class to inherit attributes and methods from another class.
# It promotes code reusability and establishes a relationship between classes.
# Single Inheritance
"""
#inheritence 
class Employee:
    company = "Google"
    salary = 100000
    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    
    def getLanguage(self):
        print(f"The language is {self.language} and company is {self.company} and salary is {self.salary}")


# Create an instance of Programmer
p = Programmer()
p.getLanguage()
p.showDetails()

# This will print the details of the programmer and inherited properties from Employee class
# it is called single inheritance
# """

#MULTIPLE INHERITANCE
"""
class Person:
    def __init__(self, name):
        self.name = name
    def showName(self):
        print(f"Name: {self.name}")

class Employee:
    company = "Google"
    salary = 100000
    def showDetails(self):
        print("This is an employee")

class Programmer(Employee, Person):
    language = "Python"
    
    def getLanguage(self):
        print(f"The language is {self.language} and company is {self.company} and salary is {self.salary} and name is {self.name}")

#this will print the details of the programmer and inherited properties from Employee and Person class
p = Programmer("Alice")
p.getLanguage()
"""

#multiple level inheritance
"""
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def yelp(self):
        print("Puppy yelps")

# This will print the details of the puppy and inherited properties from Dog and Animal class
p = Puppy()
p.speak()
p.bark()
p.yelp()

"""
