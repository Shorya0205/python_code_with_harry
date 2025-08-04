#practice 

#1. Create a class 2d vector and use it to create another class representing a 3d vector
"""

class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"Vector2D: i={self.i}, j={self.j}")
class Vector3D(Vector2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"Vector3D: i={self.i}, j={self.j}, k={self.k}")
# Example usage
v2d = Vector2D(3, 4)
v3d = Vector3D(1, 2, 3)
v2d.show()
v3d.show()

"""

#2create a class employee and add salary and increment properties to it and writea method salary_increment that returns the
# incremented salary using properties

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Using a single underscore to indicate a protected attribute

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    @property
    def increment(self):
        return self._salary * 0.1  # Example increment of 10%

    def salary_increment(self):
        return self._salary + self.increment
# Example usage
emp = Employee("John Doe", 50000)
print(f"Initial Salary: {emp.salary}")
emp.salary = 60000  # Setting a new salary
print(f"Updated Salary: {emp.salary}")
print(f"Salary Increment: {emp.salary_increment()}")

