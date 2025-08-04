#Super Keyword
"""
The super() function is used to call methods from a parent class.
It is particularly useful in the context of inheritance.
"""

class Animal:
    def __init__(self):
        print("Animal speaks")
    def speak(self):
        print("Animal speaks")
    
class Dog(Animal):
    def __init__(self):
        super().__init__()
        super().speak()
        print("Dog barks")
    def bark(self):
        print("Dog barks")    

class Puppy(Dog):
    def __init__(self):
        super().__init__()
        super().bark()
        print("Puppy yelps")
    def yelp(self):
        print("Puppy yelps")

p= Puppy()
p.yelp()
