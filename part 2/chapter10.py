#operator overloading in python 

# This code demonstrates how to use operator overloading in Python by defining a class with a custom addition method.
#operators in python can be overloaded using dunder methods like __add__, __sub__, etc.
#these methos are called when a given operator is used on the objects 
class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n +num.n
    
    def __sub__(self, num):
        return self.n - num.n
    
    def __mul__(self, num):
        return self.n * num.n
    
    def __truediv__(self, num):
        return self.n / num.n
    
    def __str__(self):
        return f"Number: {self.n}"

    def __len__(self):
        return self.n
    

n= number(5)
m= number(10)
print(n+m)
print(n-m)
print(n*m)
print(n/m)
print(n)  # This will call the __str__ method
print(len(n))  # This will call the __len__ method, returning the value of n
