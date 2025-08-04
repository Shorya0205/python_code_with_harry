#OBJECT ORIENTED PROGRAMMING IN PYTHON
#CLASSES
#CLASS IS A BLUEPRINT FOR CREATING OBJECTS
#IT IS A TEMPLATE FOR CREATING OBJECTS
class Employee:
    no_of_leaves = 8
    salary = 100
    company = "Google"
    def get_info(self):print(f"Leaves are {self.no_of_leaves} and salary is {self.salary} and company is {self.company}")
        
    @staticmethod
    def greet():
        print("Hello, welcome to the Employee class!")
    # Static method can be called without creating an object
    # It does not require 'self' as the first parameter

harry = Employee()
print(harry.salary)
print(harry.no_of_leaves)
print(harry.company)

harry.salary = 300
print(harry.salary)
#this is a object attribute or instance attribute, it will not change the class attribute
print(Employee.salary)  # This will still print the class attribute

Employee.get_info(harry)  # Calling the method with the object

# You can also call the method directly from the class
harry.get_info()  # This will also work, as the method is defined in the class

# Calling the static method
Employee.greet()  # This will print the greeting message

# You can also call the static method using the object
harry.greet()  # This will also print the greeting message


#INIT CONSTRUCTOR
#INIT is a special method that is called when an object is created
#It is used to initialize the attributes of the object
# IT APPLIES WITHOUT THE NEED TO CALL THE METHOD

class student:
    def __init__(self):
        print("I am a constructor")
              
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Student {self.name} of age {self.age} is created")

harry= student("Harry", 20)
