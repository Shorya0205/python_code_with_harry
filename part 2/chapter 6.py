#PRctice set1
#CREATE A CLASS "PROGRAMMER" FOR STORING INFORMATION OF FEW PROGRAMMERS WORKING AT MICROSOFT

class Programmer:
   company = "Microsoft"
   def __init__(self, name, age, salary):
         self.name = name
         self.age = age
         self.salary = salary


p= Programmer("Alice", 30, 80000)
q= Programmer("Bob", 25, 60000)
r= Programmer("Charlie", 28, 70000)
print(f"Name: {p.name}, Age: {p.age}, Salary: {p.salary}, Company: {p.company}")
print(f"Name: {q.name}, Age: {q.age}, Salary: {q.salary}, Company: {q.company}")
print(f"Name: {r.name}, Age: {r.age}, Salary: {r.salary}, Company: {r.company}")
# This will print the details of the student created


#2.wap of class calculator which is capable of finding the square, cube, square root and cube root of a number
class calculator:

    def __init__ (self,n):
         self.n = n

    def square (self):
         print(f"The square is {self.n*self.n}")     

    def cube(self):
         print(f"The cube is {self.n*self.n*self.n}")

    def squareroot (self):
         print(f"The square root is {self.n**1/2}") 


a=calculator(4)
a.square()
a.cube()
a.squareroot()

